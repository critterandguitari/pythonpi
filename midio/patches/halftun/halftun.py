import os
import pygame
import time
import random
import pygame.gfxdraw

bg = pygame.Surface((656,416))

def setup():
    print "setting up random pies ..."

def draw(screen, vsynth):
			
	if vsynth.note_on:
		x=random.randrange(0,700)
		y=random.randrange(0,400)
		pierad=random.randrange(10,) #radius
		arcstart=random.randrange(0,360)
		arcend=random.randrange(0, 360-arcstart)
		coloralpha=vsynth.knob3/4
#		size = vsynth.knob2
		color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), coloralpha)
#		width = vsynth.knob1 // 50
#		if width == 0 : width = 1
#		if width > size : width = size 
		nestrange=vsynth.knob1/8
		fanrange=vsynth.knob2/10
		count=0
		for i in range(nestrange):
			count = i
			arcstart=random.randrange(0,360)
			arcend=random.randrange(0, 360-arcstart)
			for i in range(fanrange):
				pygame.gfxdraw.pie(screen, screen.get_width()/2, screen.get_height(), screen.get_height() - (count*screen.get_height()/nestrange), arcstart + i*fanrange, arcend - i*fanrange, color)
				#pygame.gfxdraw.pie(screen, screen.get_width()/2, screen.get_height()/2, (nestrange-count)*, arcstart + i*fanrange, arcend - i*fanrange, color)
			pygame.display.flip() #updates the display surface


		

	
#pgyame.gfxdraw.pie(surface, x, y, radius, arcstart, arcend, color): return None
