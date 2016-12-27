import pygame


'''
The constants field will be hard-coded in. It will not change during the run.
iDict will be added to each time a new image is loaded in for the first time. After that, 
images will be accessed through the dictionary.s
'''
class TextureMap:

	# Constants corresponding to each image
	AVATAR = 0

	'''
	Dictionary linking resources to image names
	Contains the image corresponding to each element.
	'''
	textures = { }

	def loadTexture(self, textureName):
		for key in self.textures:
			if(key == textureName):
				return textures[textureName]
		thisTexture = pygame.image.load(os.path.join('__pycache__', textureName))
		textures.update({textureName, thisTexture})
		return thisTexture