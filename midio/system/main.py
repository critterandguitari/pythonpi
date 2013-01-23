import os
import pygame
import time
import random
import serial
import fullfb
import glob

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]


#add the line init_uart_clock=2441406  to /boot/config.txt to make 38400 into 31250
#serialport = serial.Serial("/dev/ttyAMA0", 38400, timeout=0.5)
serialport = serial.Serial("/dev/ttyAMA0", 38400)



# Create an instance of the PyScope class
screen = fullfb.init()

print "opening frame buffer"


print "loading patches..."

import imp

patches = []

patch_folders = get_immediate_subdirectories('../patches/')

for patch_folder in patch_folders :
    patch_name = str(patch_folder)
    patch_path = '../patches/'+patch_name+'/'+patch_name+'.py'
    print patch_path
    patches.append(imp.load_source(patch_name, patch_path))


count = 0
patch = None 
patch = patches[0]

print len(patches)
num = 0
while 1:

    count += 1
    print count
    if count > 100 :
        count = 0
        num += 1
        if num == len(patches) : num = 0
        patch = patches[num]
    
    patch.draw(screen)

    pygame.display.flip()



time.sleep(1)


print "Quit"
