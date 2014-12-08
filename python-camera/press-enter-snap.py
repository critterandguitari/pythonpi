
import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    count = 1
    while True :
        raw_input("press enter take pic")
        camera.capture("../jpegs/" + str(count) + ".jpg")
        count += 1
         
