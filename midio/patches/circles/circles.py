import os
import pygame
import time
import random
import pygame.gfxdraw

def setup():
    print "setting up random circles ..."

def draw(screen, mvp):
    if mvp.quarter_note :
        #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        color = (random.randrange(0,25), random.randrange(0,25), random.randrange(0,25))
        screen.fill(color) 
          

    if mvp.note_on :
        x=random.randrange(0,70)  + mvp.knob2 // 2
        y=random.randrange(0,40)  + mvp.knob3 // 2
        size = mvp.knob1
        color = (random.randrange(200,250), random.randrange(100,250), random.randrange(100,255))
        #color = pygame.Color.hsva( (float(mvp.knob3) / 1024) * 360, 100, 100, 50)#(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        #color = Color.hsva( 20, 100, 100, 50)#(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = mvp.knob1 // 50
        if width == 0 : width = 1
        if width > size : width = size
        pos = (x,y)#pygame.mouse.get_pos()
        pygame.draw.circle(screen,color,pos,size, 0)
        time.sleep(.05)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
#        pygame.gfxdraw.filled_circle(screen, x, y, size, color)
