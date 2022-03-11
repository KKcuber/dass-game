from email.base64mime import header_length
import colorama as clr

class GameObject:
    def __init__(self, posX, posY, char, sizeX, sizeY, color, health):
        self.posX = posX
        self.posY = posY
        self.char = char
        self.color = color
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.alive = True
        self.health = health
        self.maxHealth = health

    def draw(self, screen):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if(self.alive):
                    screen.screenarr[self.posY + y][self.posX + x] = self.color + self.char + clr.Fore.RESET