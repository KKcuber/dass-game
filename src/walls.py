from src.GameObject import GameObject
import colorama as clr
class Walls(GameObject):
    def __init__(self, char, color, health):
        self.wallsArray = []
        for y in range(8, 20):
            for x in range(30, 50):
                if(x == 30 or x == 49 or y == 8 or y == 19):
                    self.wallsArray.append(GameObject(x, y, char, 1, 1, color, health))

    def draw(self, screen):
        for wall in self.wallsArray:
            if(wall.alive):
                wall.draw(screen)
    
    def revive(self):
        for wall in self.wallsArray:
            wall.alive = True
            wall.color = clr.Fore.GREEN
            wall.health = 30