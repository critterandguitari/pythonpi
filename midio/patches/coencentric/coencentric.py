import os
import pygame
import time
import random

offsetx = offsety = 200

def test(t):
    print t

def draw(screen, s):
    global offsetx, offsety 
    offsetx -= 1
    #offsety += 1
    x = screen.get_rect().centerx
    y = screen.get_rect().centery
    size = s#offsetx#random.randrange(8,200)
    color = (random.choice([0, 255]), random.choice([0,255]), random.choice([0,255]))
    pygame.draw.circle(screen,color,[x,y],size)
    time.sleep(.05)


    
        
