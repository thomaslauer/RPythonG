from module1 import *

from engine import *

class test:
	def __init__(self):
		self.x = 4

a = test()
b = OtherTest()

print(a.x)
print(b.name)

game = GameEngine()
game.mainLoop()