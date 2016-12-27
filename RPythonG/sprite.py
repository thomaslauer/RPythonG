import pygame

class sprite:
	def __init__(self, imageID, id, sizex, sizey):
		self.image = pygame.image.load(imageID)
		self.id = id
		self.x = 0
		self.y = 0
		self.sizex = sizex
		self.sizey = sizey

	def setPosition(self, x, y):
		self.x = x
		self.y = y

	def getPosition(self):
		return tuple(self.x, self.y)


