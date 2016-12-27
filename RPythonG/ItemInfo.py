class ItemHandler:   
    # ID table contains list of all in-play sprites, along with relevant information
    # Stored as tuples (id, x, y, visible, etc.)

    def __init__(self):
        self.ItemIDTable = list()
        self.avatar = 0

    def id_Avatar(self): return self.avatar




    '''
    def remove_from_table(self, id):
        for itemTuple in self.ItemIDTable:
            if itemTuple
    '''