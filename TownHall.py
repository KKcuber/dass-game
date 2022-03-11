from GameObject import GameObject

class TownHall(GameObject):
    def __init__(self, posX, posY, color, health):
        GameObject.__init__(self, posX, posY, 'T', 4, 3, color, health)