from GameObject import GameObject

class Walls(GameObject):
    def __init__(self, char, color):
        self.maxHealth = 30
        self.wallsArray = []
        self.healthArray = []
        for y in range(8, 20):
            for x in range(30, 50):
                if(x == 30 or x == 49 or y == 8 or y == 19):
                    self.wallsArray.append(GameObject(x, y, char, 1, 1, color))
                    self.healthArray.append(self.maxHealth)

    def draw(self, screen):
        for wall in self.wallsArray:
            wall.draw(screen)