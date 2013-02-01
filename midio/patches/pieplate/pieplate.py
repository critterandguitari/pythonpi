import os
import pygame
import time
import random
import pygame.gfxdraw

def setup():
    print "setting up random pies ..."

def draw(screen, vsynth):
    if vsynth.note_on :
        pierad=random.randrange(0,360) #radius/Radians?
        x=random.randrange(0,700)
        y=random.randrange(0,400)
        size = vsynth.knob2
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = vsynth.knob1 // 50
        if width == 0 : width = 1
        if width > size : width = size
        pygame.gfxdraw.pie(screen, x, y, pierad, 5, 50, color)
#        pygame.draw.circle(screen,color,[x,y],size, 0)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
#        pygame.gfxdraw.filled_circle(screen, x, y, size, color)

#pgyame.gfxdraw.pie(surface, x, y, r, start, end, color): return None
