from GameObject import GameObject

class TownHall(GameObject):
    def __init__(self, posX, posY, color):
        GameObject.__init__(self, posX, posY, 'T', 4, 3, color)
        self.health = 100
        self.maxhealth = 100
        self.wallsarray = []