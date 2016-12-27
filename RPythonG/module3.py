from sprite import *
import pygame

class Avatar(sprite):
	def __init__(self, resource, x, y):
		super().__init__(0, resource, 15, 15)
	
	

		'''
		Do we want to handle all updates to the display screen in their
		separate classes, and have a single call to display.flip() to 
		update them all at once?
		'''