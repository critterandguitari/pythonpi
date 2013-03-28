import smf
import sys
import time
import serial
from datetime import datetime
import time


#serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

#add the line init_uart_clock=2441406  to /boot/config.txt to make 38400 into 31250
serialport = serial.Serial("/dev/ttyAMA0", 38400, timeout=0.5)

def send_note_off(ch, note, vel) :
    channel = 1
    status = int(0x80) | int(ch - 1)
    serialport.write(chr(status))
    serialport.write(chr(note & 0x7f))
    serialport.write(chr(vel & 0x7f))
    serialport.flush()

def send_note_on(ch, note, vel) :
    channel = 1
    status = int(0x90) | int(ch - 1) 
    serialport.write(chr(status))
    serialport.write(chr(note & 0x7f))
    serialport.write(chr(vel & 0x7f))
    serialport.flush()

def play_event(e, track) :
    if (int(e.midi_buffer[0]) >> 4) == int(0x9) :
        if int(e.midi_buffer[2]) > 0:
#            print("at: " + str(e.time_seconds) + " note on")
            send_note_on(track, int(e.midi_buffer[1]), 100)
        if int(e.midi_buffer[2]) == 0:
#            print("at: " + str(e.time_seconds) + " note off")
            send_note_off(track, int(e.midi_buffer[1]), 0)
    if (int(e.midi_buffer[0]) >> 4) == int(0x8) :
#        print("at: " + str(e.time_seconds) + " note off")
        send_note_off(track, int(e.midi_buffer[1]), 0)



# mute all the tracks
for i in range(1,5) :
    for k in range (0, 127) :
        send_note_off(i, k, 0)
        #print "sending note off: " + str(i) + ", "+str(k)

time.sleep(5)
print "playing ..."

filename = sys.argv[1]
#tracknum = int(sys.argv[2])

print("opening file '%s'..." % filename)
f = smf.SMF(filename)

#print ("first")
#print (t.events.next().decode())

t1 = f.tracks[1]
t2 = f.tracks[2]
t3 = f.tracks[3]
t4 = f.tracks[4]

e1 = t1.events.next()
e2 = t2.events.next()
e3 = t3.events.next()
e4 = t4.events.next()

start_time = time.time()
while True :
    if (e1.time_seconds) < (time.time() - start_time) :
        play_event(e1, 1)
        e1 = t1.events.next()
    if (e2.time_seconds) < (time.time() - start_time) :
        play_event(e2, 2)
        e2 = t2.events.next()
    if (e3.time_seconds) < (time.time() - start_time) :
        play_event(e3, 3)
        try :
            e3 = t3.events.next()
        except StopIteration :
            pass
    if (e4.time_seconds) < (time.time() - start_time) :
        play_event(e4, 4)
        try :
            e4 = t4.events.next()
        except StopIteration:
            pass


