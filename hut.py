from GameObject import GameObject
import random

class Huts(GameObject):
    def __init__(self, char, color):
        self.hutsarray = []
        self.healtharray = []
        self.hutsarray.append(GameObject(32, 10, char, 1, 1, color))
        self.hutsarray.append(GameObject(33, 15, char, 1, 1, color))
        self.hutsarray.append(GameObject(36, 18, char, 1, 1, color))
        self.hutsarray.append(GameObject(47, 11, char, 1, 1, color))
        self.hutsarray.append(GameObject(45, 15, char, 1, 1, color))
        for i in range(5):
            self.healtharray.append(60)

    def draw(self, screen):
        for hut in self.hutsarray:
            hut.draw(screen)