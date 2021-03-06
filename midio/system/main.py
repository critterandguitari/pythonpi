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
import traceback
import sys

from pygame.locals import *


pygame.init()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OSDBG = (0,0,255)

# OSD stuff
font = pygame.font.SysFont(None, 32)
notemsg = font.render('...', True, WHITE, OSDBG)



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


# TODO :  don't make a list of moduels, just make a list of their names, and select them from  sys.modules
print "loading patches..."
patches = []
patch_folders = get_immediate_subdirectories('../patches/')

for patch_folder in patch_folders :
    patch_name = str(patch_folder)
    patch_path = '../patches/'+patch_name+'/'+patch_name+'.py'
    print patch_path
    try :
        patches.append(imp.load_source(patch_name, patch_path))
    except Exception, e:
        print traceback.format_exc()

# set initial patch
patch = None 
num = 0
patch = patches[num]

# run setup functions if patches have them
# TODO: setup needs to get passed screen for things like setting sizes
for patch in patches :
    try :
        patch.setup()
    except AttributeError :
        print "no setup found"
        continue 

# flush serial port
serialport.flushInput()

#create mvp object
mvp = hardware.HardwareInput()

buf = ''
line = ''

mvp.clear_flags()

error = ''


while 1:
    #print serialport.inWaiting()    
    # get serial line and parse it, TODO hmmm could this miss lines?  (only parses most recent, but there could be more in serial buffer)
    if serialport.inWaiting() > 0:
        buf = buf + serialport.read(serialport.inWaiting())
        if '\n' in buf :
            lines = buf.split('\n')
            for l in lines :
                mvp.parse_serial(l)
            buf = lines[-1]

    # ... or parse lines from UDP instead
    try :
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        buf = buf + data
        if '\n' in buf :
            lines = buf.split('\n')
            for l in lines :
                mvp.parse_serial(l)
     #           print l
            buf = lines[-1]
    except :
        pass


    # TODO :  update this to use sys.modules (see above, and below...)
    if mvp.next_patch: 
        num += 1
        if num == len(patches) : num = 0
#        patch = patches[num]


    if mvp.quarter_note : 
#        screen.fill ((0,0,0))
#        pygame.display.flip()
        print "some note" 


    if mvp.clear_screen:
        #screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255))) 
        screen.fill( (0,0,0)) 
        pygame.display.flip()

    mvp.note_on = True

    # set patch
    # TODO: setup has to be called too (maybe )
    if mvp.set_patch :
        print "setting: " + mvp.patch
        try :
            patch = sys.modules[mvp.patch]
            error = ''
        except KeyError:
            error = "Module " +mvp.patch+ " is not loaded, probably it has errors"

    # reload
    # TODO: setup has to be called too
    if mvp.reload_patch :
        # delete the old
        if mvp.patch in sys.modules:  
            del(sys.modules[mvp.patch]) 
        print "deleted module, reloading"
        patch_name = mvp.patch
        patch_path = '../patches/'+patch_name+'/'+patch_name+'.py'
        try :
            patch = imp.load_source(patch_name, patch_path)
            error = ''
            print "reloaded"
        except Exception, e:
            error = traceback.format_exc()
          #  formatted_lines = traceback.format_exc().splitlines()
          #  print formatted_lines[-3]
          #  print formatted_lines[-1]
    
    mvp.note_on = True
    
    try :
        patch.draw(screen, mvp)
        #error = ''
    except Exception, e:
        #print traceback.format_exc()
        error = traceback.format_exc()

    
    # osd
    if mvp.osd :
        pygame.draw.rect(screen, OSDBG, (0, screen.get_height() - 40, screen.get_width(), 40))
        font = pygame.font.SysFont(None, 32)
        text = font.render('patch: ' + str(patch.__name__), True, WHITE, OSDBG)
        text_rect = text.get_rect()
        text_rect.x = 50
        text_rect.centery = screen.get_height() - 20
        screen.blit(text, text_rect)
       
        if mvp.note_on :
            notemsg = font.render('note on', True, WHITE, OSDBG)
        
        text_rect = notemsg.get_rect()
        text_rect.x = screen.get_width() - 100
        text_rect.centery = screen.get_height() - 20
        screen.blit(notemsg, text_rect)

        # osd, errors
        i = 0
        for errorline in error.splitlines() :
            errormsg = font.render(errorline, True, WHITE, RED) 
            text_rect = notemsg.get_rect()
            text_rect.x = 50
            text_rect.y = 20 + (i * 32)
            screen.blit(errormsg, text_rect)
            i += 1

       


    pygame.display.flip()

    if mvp.quit :
        sys.exit()
    
    # clear all the events
    mvp.clear_flags()
    #time.sleep(.01)

time.sleep(1)


print "Quit"
