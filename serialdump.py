import os
import time
import serial

serialport = serial.Serial("/dev/ttyAMA0", 38400)


while 1:

    #s = serialport.read(1)
    print serialport.readline()

