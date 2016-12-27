import pygame

class GameEngine:
	def __init__(self):
		self.initWindow(300, 300)
		self.running = False
		self.setBackgroundColor((0, 0, 0))
		self.fps = 30


	def initWindow(self, width, height):
		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption('RPythonG')
		self.clock = pygame.time.Clock()
	
	def mainLoop(self):
		self.running = True

		x = 10;
		while self.running:
			self.window.fill(self.background_color)


			# do update here

			pygame.draw.circle(self.window, (0, 0, 255), (x, 100), 15, 5)
			x += 1

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

