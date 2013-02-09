import os
import pygame
import time
import random

count = 0

TRANSPARENT = (255,255,255)
bg = pygame.Surface((656,416))
mask = pygame.Surface((656,416))
mask.set_colorkey(TRANSPARENT)
mask.fill((0,0,0))

def draw(screen, vsynth):
    
    global bg, mask, count
    
    count += 1
    if count > (vsynth.knob3 // 10)  : count = 0

    if vsynth.clear_screen or count == 0:
        mask.fill((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))

    x=random.randrange(0,656)
    y=random.randrange(0,400)
    y1=random.randrange(0,400)
    x1=random.randrange(0,656)
    size = random.randrange(0,200)
    width = vsynth.knob2#random.randrange(100,255)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.line(bg, color, [x, y], [x1, y1], width)
    rect = bg.get_rect()
    screen.blit(bg, rect)
    
    x=random.randrange(0,700)  
    y=random.randrange(0,400)  
    size = vsynth.knob1
    pos = (x,y)
    pygame.draw.circle(mask,TRANSPARENT,pos,size, 0)
    rect = mask.get_rect()
    screen.blit(mask, rect)
    
    #time.sleep(.1)


