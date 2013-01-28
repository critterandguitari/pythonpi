import os
import pygame
import time
import random

def setup():
    print "setting up random circles ..."


def draw(screen, vsynth):
    if vsynth.note_on :
        x=random.randrange(0,700)
        y=random.randrange(0,400)
        size = vsynth.knob2
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        pygame.draw.circle(screen,color,[x,y],size)
