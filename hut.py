from GameObject import GameObject
import random

class Huts(GameObject):
    def __init__(self, char, color, health):
        self.hutsArray = []
        self.hutsArray.append(GameObject(32, 10, char, 1, 1, color, health))
        self.hutsArray.append(GameObject(33, 15, char, 1, 1, color, health))
        self.hutsArray.append(GameObject(36, 18, char, 1, 1, color, health))
        self.hutsArray.append(GameObject(47, 11, char, 1, 1, color, health))
        self.hutsArray.append(GameObject(45, 15, char, 1, 1, color, health))

    def draw(self, screen):
        for hut in self.hutsArray:
            if(hut.alive):
                hut.draw(screen)