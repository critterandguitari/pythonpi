import os
import pygame
import time
import random
import pygame.gfxdraw

def setup():
    print "setting up random circles ..."

def draw(screen, vsynth):
    if vsynth.note_on :
        x=random.randrange(0,700)
        y=random.randrange(0,400)
        size = vsynth.knob2
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = vsynth.knob1 // 50
        if width == 0 : width = 1
        if width > size : width = size
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,color,pos,size, 0)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
#        pygame.gfxdraw.filled_circle(screen, x, y, size, color)
