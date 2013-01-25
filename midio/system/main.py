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
# or add the line init_uart_clock=13020833 to change 115200 into .5Mbs 
serialport = serial.Serial("/dev/ttyAMA0", 115200)


# Create an instance of the PyScope class
print "opening frame buffer"
screen = fullfb.init()


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
patch = patches[1]

print len(patches)
num = 0

serialport.flushInput()

while 1:

    count += 1
    if count > 2 : count = 0
    
    s = serialport.readline()
    s = s.rstrip()
    array = s.split(',')
#    print array
#    print len(array)

    # basic parse next command
    if len(array) == 1:
        if array[0] == "n" :
            num += 1
            if num == len(patches) : num = 0
            patch = patches[num]

    # basic parse of knob array
    size = 1
    if len(array) == 4 :
        if array[0] == "k" :
            if array[1].isdigit() :
                size = int(array[1])
    
    print serialport.inWaiting()
    
    if count == 0:
        patch.draw(screen, size)
        pygame.display.flip()



time.sleep(1)


print "Quit"
