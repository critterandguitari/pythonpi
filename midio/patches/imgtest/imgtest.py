import os
import pygame
import glob

images = []
image_index = 0

def setup() :
    global images
    for filepath in sorted(glob.glob('../patches/imgtest/*.jpg')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, vsynth) :
    global images, image_index
    
    image_index += 1
    if image_index == len(images) : image_index = 0
    image = images[image_index]

    screen.fill((0, 0, 0))
    rect = image.get_rect()
    screen.blit(image, rect)
