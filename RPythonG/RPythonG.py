#from module1 import *

from engine import *

class test:
	def __init__(self):
		self.x = 4

a = test()

print(a.x)

game = GameEngine()
game.mainLoop()