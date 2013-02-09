import os
import pygame
import time
import random

size = 400


def draw(screen, mvp):
    global size
    size -= 2
    if size < 2:
        size = 400
    x = screen.get_rect().centerx
    y = screen.get_rect().centery
    #size = mvp.knob2
    c = int(size * mvp.knob2) & 0xff #random.choice([0, 255])
    c2 = (c << 4) & 0xf0
    color = (c, 255 - c2, c2)
    pygame.draw.circle(screen,color,[x,y],size)
    time.sleep(.1)


    
        
