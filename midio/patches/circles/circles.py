import os
import pygame
import time
import random

def setup():
    print "setting up random circles ..."


def draw(screen, vsynth):
    x=random.randrange(0,700)
    y=random.randrange(0,400)
    size = vsynth.size
    color = (255, random.randrange(0,255), random.randrange(0,255))
    pygame.draw.circle(screen,color,[x,y],size)
