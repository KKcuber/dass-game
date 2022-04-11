from src.GameObject import GameObject
from src.input import *
import colorama as clr

def euclideanDistance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
class Queen(GameObject):
    def __init__(self, posX, posY, char, sizeX, sizeY, color, health):
        GameObject.__init__(self, posX, posY, char, sizeX, sizeY, color, health)
        self.vel = 1
        self.attackdamage = 5
        self.lastMoved = 'down'
        self.range = 5

    def findAttackPosition(self):
        if(self.lastMoved == 'up'):
            return (self.posX, self.posY - 8)
        elif(self.lastMoved == 'down'):
            return (self.posX, self.posY + 8)
        elif(self.lastMoved == 'left'):
            return (self.posX - 8, self.posY)
        elif(self.lastMoved == 'right'):
            return (self.posX + 8, self.posY)

    def move(self, inputchar, screen, rageSpellActive):
        if(inputchar == 'w'):
            self.lastMoved = 'up'
            if(self.posY > 0 and screen.screenarr[self.posY - 1][self.posX] == ' '):
                if(rageSpellActive and screen.screenarr[self.posY - 2][self.posX] != ' '):
                    self.posY -= 1
                else:
                    self.posY -= self.vel
        elif(inputchar == 's'):
            self.lastMoved = 'down'
            if(self.posY < screen.height - 1 and screen.screenarr[self.posY + 1][self.posX] == ' '):
                if(rageSpellActive and screen.screenarr[self.posY + 2][self.posX] != ' '):
                    self.posY += 1
                else:
                    self.posY += self.vel
        elif(inputchar == 'a'):
            self.lastMoved = 'left'
            if(self.posX > 0 and screen.screenarr[self.posY][self.posX - 1] == ' '):
                if(rageSpellActive and screen.screenarr[self.posY][self.posX - 2] != ' '):
                    self.posX -= 1
                else:
                    self.posX -= self.vel
        elif(inputchar == 'd'):
            self.lastMoved = 'right'
            if(self.posX < screen.width - 1 and screen.screenarr[self.posY][self.posX + 1] == ' '):
                if(rageSpellActive and screen.screenarr[self.posY][self.posX + 2] != ' '):
                    self.posX += 1
                else:
                    self.posX += self.vel

    def attack(self, walls, townHall, cannons, huts, wizardTowers):
        attackCenter = self.findAttackPosition()
        for hut in huts.hutsArray:
            if(euclideanDistance(hut.posX, hut.posY, attackCenter[0], attackCenter[1]) <= 2.9):
                hut.health -= self.attackdamage
                if(hut.health <= hut.maxHealth*2/3):
                    hut.color = clr.Fore.YELLOW
                if(hut.health <= hut.maxHealth/3):
                    hut.color = clr.Fore.RED
                if(hut.health <= 0):
                    hut.alive = False
                    hut.color = clr.Fore.RESET

        for wall in walls.wallsArray:
            if(wall.alive and euclideanDistance(wall.posX, wall.posY, attackCenter[0], attackCenter[1]) <= 2.9):
                wall.health -= self.attackdamage
                if(wall.health <= wall.maxHealth*2/3):
                    wall.color = clr.Fore.YELLOW
                if(wall.health <= wall.maxHealth/3):
                    wall.color = clr.Fore.RED
                if(wall.health <= 0):
                    wall.alive = False
                    wall.color = clr.Fore.RESET

        for cannon in cannons:
            if(cannon.alive and euclideanDistance(cannon.posX, cannon.posY, attackCenter[0], attackCenter[1]) <= 2.9):
                cannon.health -= self.attackdamage
                if(cannon.health <= cannon.maxHealth*2/3):
                    cannon.color = clr.Fore.YELLOW
                if(cannon.health <= cannon.maxHealth/3):
                    cannon.color = clr.Fore.RED
                if(cannon.health <= 0):
                    cannon.alive = False
                    cannon.color = clr.Fore.RESET

        for wizardTower in wizardTowers:
            if(wizardTower.alive and euclideanDistance(wizardTower.posX, wizardTower.posY, attackCenter[0], attackCenter[1]) <= 2.9):
                wizardTower.health -= self.attackdamage
                if(wizardTower.health <= wizardTower.maxHealth*2/3):
                    wizardTower.color = clr.Fore.YELLOW
                if(wizardTower.health <= wizardTower.maxHealth/3):
                    wizardTower.color = clr.Fore.RED
                if(wizardTower.health <= 0):
                    wizardTower.alive = False
                    wizardTower.color = clr.Fore.RESET

        for x in range(townHall.posX, townHall.posX + townHall.sizeX):
            for y in range(townHall.posY, townHall.posY + townHall.sizeY):
                if(townHall.alive and abs(attackCenter[0]- x) + abs(attackCenter[1] - y) <= 5):
                    townHall.health -= self.attackdamage
                    if(townHall.health <= townHall.maxHealth*2/3):
                        townHall.color = clr.Fore.YELLOW
                    if(townHall.health <= townHall.maxHealth/3):
                        townHall.color = clr.Fore.RED
                    if(townHall.health <= 0):
                        townHall.alive = False
                        townHall.color = clr.Fore.RESET