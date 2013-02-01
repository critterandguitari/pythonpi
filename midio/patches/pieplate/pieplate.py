import os
import pygame
import time
import random
import pygame.gfxdraw

def setup():
    print "setting up random pies ..."

def draw(screen, vsynth):
	if vsynth.half_note: 
		screen.fill((0,0,0))
			
	if vsynth.note_on:
		x=random.randrange(0,700)
		y=random.randrange(0,400)
		pierad=random.randrange(10,100) #radius
		arcstart=random.randrange(0,360)
		arcend=random.randrange(0, 360-arcstart)
		size = vsynth.knob2
		color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
		width = vsynth.knob1 // 50
		if width == 0 : width = 1
		if width > size : width = size 
		fillrange=vsynth.knob1/10
		for i in range(fillrange):
			pygame.gfxdraw.pie(screen, x, y, pierad, arcstart + i*2, arcend - i*2, color)
        
#		pygame.gfxdraw.pie(screen, x, y, pierad, 5, 50, color)
#        pygame.draw.circle(screen,color,[x,y],size, 0)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
#        pygame.gfxdraw.filled_circle(screen, x, y, size, color)

#pgyame.gfxdraw.pie(surface, x, y, radius, arcstart, arcend, color): return None
