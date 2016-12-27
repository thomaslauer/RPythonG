from sprite import *
from ItemInfo import *

class Avatar(sprite):
    def __init__(self, x, y):
        super.__init__(self, "me.png", ItemHandler.id_Avatar(), 0, 0)
        self.setPosition(x, y)
