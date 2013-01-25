import os
import time
import serial

serialport = serial.Serial("/dev/ttyAMA0", 38400)


serialport.flushInput()
while 1:
     
    s = serialport.readline()
    s = s.rstrip()
    array = s.split(',')
    #print array

    
    # basic parse next command
    if len(array) == 1:
        if array[0] == "sd" :
            print "shut d"
            os.system("sudo shutdown -h now")
   
