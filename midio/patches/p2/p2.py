import os
import pygame
import time
import random


def draw(screen):
    x=random.randrange(0,656)
    y=random.randrange(0,400)
    y1=random.randrange(0,400)
    x1=random.randrange(0,656)
    size = random.randrange(0,200)
    width = random.randrange(100,255)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.line(screen, color, [x, y], [x1, y1], width)

    time.sleep(.05)
