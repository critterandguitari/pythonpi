import os
import pygame
import time
import random

def test(t):
    print t

def draw(screen):
    x=random.randrange(0,700)
    y=random.randrange(0,400)
    size = random.randrange(80,120)
    color = (0, random.randrange(0,255), random.randrange(0,255))
    pygame.draw.circle(screen,color,[x,y],size)
    time.sleep(.05)
