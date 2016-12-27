import pygame


'''
The constants field will be hard-coded in. It will not change during the run.
iDict will be added to each time a new image is loaded in for the first time. After that, 
images will be accessed through the dictionary.s
'''
class ItemDict:

	# Constants corresponding to each image
	AVATAR = 0

	'''
	Dictionary linking resources to image names
	Contains the image corresponding to each element.
	'''
	iDict = { }

