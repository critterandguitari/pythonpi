import os
import pygame
import time
import random
import serial
import fullfb
import glob
import hardware
import imp

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


while 1:

    #print serialport.inWaiting()    
    # get serial line and parse it
    s = serialport.readline()
    s = s.rstrip()
    vsynth.parse_serial(s)

    if vsynth.next_patch: 
        num += 1
        if num == len(patches) : num = 0
        patch = patches[num]


    if vsynth.clear_screen:
        screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255))) 
        pygame.display.flip()

 
    # basic parse note on command
    if vsynth.note_on:
        print "doin it"
        patch.draw(screen, vsynth)
        pygame.display.flip()

    # clear all the events
    vsynth.clear_flags()

time.sleep(1)


print "Quit"
