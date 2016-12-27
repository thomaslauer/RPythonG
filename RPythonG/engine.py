import pygame
from module3 import *
import sprite

'''
Surface.blit(source, dest, area=None, special_flags = 0): return Rect
draw one image onto another
'''


# distance moved for a single press of the corresponding arrow key
MOVE_RIGHT = 5
MOVE_LEFT = -5
MOVE_DOWN = 5
MOVE_UP = -5



class GameEngine:

	def __init__(self):
		self.initWindow(300, 300)
		self.running = False
		self.setBackgroundColor((0, 0, 0))
		self.fps = 30
		self.avatar = Avatar("Sci-fi Avatar.png", 15, 15)

	# Get the currently pressed direction key(s), and return the direction to move accordingly
	# return as a tuple
	def getUserMove(self):
		coords = [0,0]
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			coords[1] += MOVE_UP
		if keys[pygame.K_DOWN]:
			coords[1] += MOVE_DOWN
		if keys[pygame.K_LEFT]:
			coords[0] += MOVE_LEFT
		if keys[pygame.K_RIGHT]:
			coords[0] += MOVE_RIGHT
		return tuple(coords)


	def initWindow(self, width, height):
		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption('RPythonG')
		self.clock = pygame.time.Clock()
	
	def mainLoop(self):
		self.running = True

		x = 10
		y = 10
		while self.running:
			self.window.fill(self.background_color)
			self.avatar.drawSelf(self.window, x, y)
			
			delta = self.getUserMove()
			x += delta[0]
			y += delta[1]

			# check for exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			if self.running:
				self.flipWindowBuffers()
			
			self.clock.tick(self.fps) # fps cap
	
	
	

	def flipWindowBuffers(self):
		pygame.display.flip()


	def setBackgroundColor(self, color):
		self.background_color = color
