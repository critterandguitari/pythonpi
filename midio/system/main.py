import os
import pygame
import time
import random
import serial
import fullfb
import glob
import hardware
import imp
import socket

# setup a UDP socket for recivinng data from other programs
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(0)

# TODO :  make helper module, include functions like these :
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]


# add the line init_uart_clock=13020833 to change 115200 into .5Mbs 
print "init serial port"
serialport = serial.Serial("/dev/ttyAMA0", 115200)

print "opening frame buffer"
screen = fullfb.init()

print "loading patches..."
patches = []
patch_folders = get_immediate_subdirectories('../patches/')

for patch_folder in patch_folders :
    patch_name = str(patch_folder)
    patch_path = '../patches/'+patch_name+'/'+patch_name+'.py'
    print patch_path
    patches.append(imp.load_source(patch_name, patch_path))

# set initial patch
patch = None 
num = 0
patch = patches[num]

# run setup functions if patches have them
for patch in patches :
    try :
        patch.setup()
    except AttributeError :
        print "no setup found"
        continue 

# flush serial port
serialport.flushInput()

#create vsynth object
vsynth = hardware.HardwareInput()

buf = ''
line = ''

vsynth.clear_flags()

while 1:
    #print serialport.inWaiting()    
    # get serial line and parse it, TODO hmmm could this miss lines?  (only parses most recent, but there could be more in serial buffer)
    if False: #serialport.inWaiting() > 0:
        buf = buf + serialport.read(serialport.inWaiting())
        if '\n' in buf :
            lines = buf.split('\n')
            for l in lines :
                vsynth.parse_serial(l)
            #line = lines[-2]
            buf = lines[-1]

    # ... or parse lines from UDP instead
    try :
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        buf = buf + data
        if '\n' in buf :
            lines = buf.split('\n')
            for l in lines :
                vsynth.parse_serial(l)
                print l
            buf = lines[-1]
    except :
        pass


    if vsynth.next_patch: 
        num += 1
        if num == len(patches) : num = 0
        patch = patches[num]


    if vsynth.quarter_note : 
#        screen.fill ((0,0,0))
#        pygame.display.flip()
        print "some note" 


    if vsynth.clear_screen:
        #screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255))) 
        screen.fill( (0,0,0)) 
        pygame.display.flip()

    vsynth.note_on = True
    patch.draw(screen, vsynth)
    pygame.display.flip()

    # clear all the events
    vsynth.clear_flags()
    #time.sleep(.01)

time.sleep(1)


print "Quit"
