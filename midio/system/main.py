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
fb = fullfb()

time.sleep(1)

