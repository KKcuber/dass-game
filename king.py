from GameObject import GameObject
from input import *

class King(GameObject):
    def __init__(self, posX, posY, char, sizeX, sizeY, color):
        GameObject.__init__(self, posX, posY, char, sizeX, sizeY, color)
        self.vel = 1
        self.health = 100
        self.maxHealth = 100

    def move(self, inputchar, screen):
        if(inputchar == 'w'):
            if(self.posY > 0 and screen.screenarr[self.posY - 1][self.posX] == ' '):
                self.posY -= self.vel
        elif(inputchar == 's'):
            if(self.posY < screen.height - 1 and screen.screenarr[self.posY + 1][self.posX] == ' '):
                self.posY += self.vel
        elif(inputchar == 'a'):
            if(self.posX > 0 and screen.screenarr[self.posY][self.posX - 1] == ' '):
                self.posX -= self.vel
        elif(inputchar == 'd'):
            if(self.posX < screen.width - 1 and screen.screenarr[self.posY][self.posX + 1] == ' '):
                self.posX += self.vel