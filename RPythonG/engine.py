import pygame

class GameEngine:
	def __init__(self):
		self.initWindow(300, 300)
		self.running = False


	def initWindow(self, width, height):
		self.window = pygame.display.set_mode((width, height))
	
	def mainLoop(self):
		self.running = True
		while self.running:
			# do update here
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			if self.running:
				self.flipWindowBuffers()


	def flipWindowBuffers(self):
		pygame.display.flip()

