import pygame
from ItemInfo import *
import os

class sprite:
	def __init__(self, id, resource, sizex, sizey):
		ItemDict.iDict[id] = pygame.transform.scale(pygame.image.load(os.path.join('__pycache__', resource)), (int(sizex), int(sizey)))
		
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


	'''
	How do we want to resize sprites?
	Should this be done one time only, i.e. on init, 
	or do we want a helper method so that it can be 
	done more than once. Should it be by a scale factor,
	or by a raw number of pixels?
	'''
	def resize():
		return  # Placeholder until we figure our what to do here

	# Takes window to draw into, and the (x,y) coords to draw at.
	def drawSelf(self, window, x, y):
		window.blit(ItemDict.iDict[self.id], (x,y))