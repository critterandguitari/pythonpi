import os
import pygame
import time
import random
import serial
import struct
import fullfb


#add the line init_uart_clock=2441406  to /boot/config.txt to make 38400 into 31250
#serialport = serial.Serial("/dev/ttyAMA0", 38400, timeout=0.5)
serialport = serial.Serial("/dev/ttyAMA0", 38400)



# Create an instance of the PyScope class
screen = fullfb.init()

print "opening frame buffer"


print "loading patches"
import imp
patches = []
patches.append(imp.load_source('p1','../patches/p1.py'))
patches.append(imp.load_source('p2','../patches/p2.py'))


count = 0
while 1:

    count += 1
    if count > 30 : count = 0
    print count
    
    patches[0].loop(screen)

    pygame.display.flip()



time.sleep(1)


print "Quit"
