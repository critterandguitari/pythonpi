import os
import pygame
import time
import random
import glob


images = []
image_index = 0

def setup():
    global images
    for filepath in sorted(glob.glob('../patches/treefill/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, vsynth):
    if vsynth.note_on :
        x=random.randrange(0,700)
        y=random.randrange(0,400)
        size = vsynth.knob2
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = vsynth.knob1 // 50
        if width == 0 : width = 1
        if width > size : width = size
        pygame.draw.circle(screen,color,[x,y],size, 0)
        global images
        image = images[0]
        rect = image.get_rect()
        screen.blit(image, rect)   
