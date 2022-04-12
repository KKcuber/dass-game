from src.GameObject import GameObject
from src.input import *
import colorama as clr
import time

def euclideanDistance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
class Queen(GameObject):
    def __init__(self, posX, posY, char, sizeX, sizeY, color, health):
        GameObject.__init__(self, posX, posY, char, sizeX, sizeY, color, health)
        self.vel = 1
        self.lastAttack = time.time()
        self.attackdamage = 10
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

    def findAttackPositionForQueenSpecialAttack(self):
        if(self.lastMoved == 'up'):
            return (self.posX, self.posY - 16)
        elif(self.lastMoved == 'down'):
            return (self.posX, self.posY + 16)
        elif(self.lastMoved == 'left'):
            return (self.posX - 16, self.posY)
        elif(self.lastMoved == 'right'):
            return (self.posX + 16, self.posY)

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
        if(time.time() - self.lastAttack > 1):
            self.lastAttack = time.time()
            attackCenter = self.findAttackPosition()
            for hut in huts.hutsArray:
                if(hut.alive and abs(hut.posX - attackCenter[0]) <= 2 and abs(hut.posY - attackCenter[1]) <= 2):
                    hut.health -= self.attackdamage
                    if(hut.health <= hut.maxHealth*2/3):
                        hut.color = clr.Fore.YELLOW
                    if(hut.health <= hut.maxHealth/3):
                        hut.color = clr.Fore.RED
                    if(hut.health <= 0):
                        hut.alive = False
                        hut.color = clr.Fore.RESET

            for wall in walls.wallsArray:
                if(wall.alive and abs(wall.posX - attackCenter[0]) <= 2 and abs(wall.posY - attackCenter[1]) <= 2):
                    wall.health -= self.attackdamage
                    if(wall.health <= wall.maxHealth*2/3):
                        wall.color = clr.Fore.YELLOW
                    if(wall.health <= wall.maxHealth/3):
                        wall.color = clr.Fore.RED
                    if(wall.health <= 0):
                        wall.alive = False
                        wall.color = clr.Fore.RESET

            for cannon in cannons:
                if(cannon.alive and abs(cannon.posX - attackCenter[0]) <= 2 and abs(cannon.posY - attackCenter[1]) <= 2):
                    cannon.health -= self.attackdamage
                    if(cannon.health <= cannon.maxHealth*2/3):
                        cannon.color = clr.Fore.YELLOW
                    if(cannon.health <= cannon.maxHealth/3):
                        cannon.color = clr.Fore.RED
                    if(cannon.health <= 0):
                        cannon.alive = False
                        cannon.color = clr.Fore.RESET

            for wizardTower in wizardTowers:
                if(wizardTower.alive and abs(wizardTower.posX - attackCenter[0]) <= 2 and abs(wizardTower.posY - attackCenter[1]) <= 2):
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
                    if(townHall.alive and abs(x - attackCenter[0]) <= 2 and abs(y - attackCenter[1]) <= 2):
                        townHall.health -= self.attackdamage
                        if(townHall.health <= townHall.maxHealth*2/3):
                            townHall.color = clr.Fore.YELLOW
                        if(townHall.health <= townHall.maxHealth/3):
                            townHall.color = clr.Fore.RED
                        if(townHall.health <= 0):
                            townHall.alive = False
                            townHall.color = clr.Fore.RESET
        
    def specialAttack(self, walls, townHall, cannons, huts, wizardTowers, attackCenter):
        if(time.time() - self.lastAttack > 1):
            self.lastAttack = time.time()
            for hut in huts.hutsArray:
                if(hut.alive and abs(hut.posX - attackCenter[0]) <= 4 and abs(hut.posY - attackCenter[1]) <= 4):
                    hut.health -= 2*self.attackdamage
                    if(hut.health <= hut.maxHealth*2/3):
                        hut.color = clr.Fore.YELLOW
                    if(hut.health <= hut.maxHealth/3):
                        hut.color = clr.Fore.RED
                    if(hut.health <= 0):
                        hut.alive = False
                        hut.color = clr.Fore.RESET

            for wall in walls.wallsArray:
                if(wall.alive and abs(wall.posX - attackCenter[0]) <= 4 and abs(wall.posY - attackCenter[1]) <= 4):
                    wall.health -= 2*self.attackdamage
                    if(wall.health <= wall.maxHealth*2/3):
                        wall.color = clr.Fore.YELLOW
                    if(wall.health <= wall.maxHealth/3):
                        wall.color = clr.Fore.RED
                    if(wall.health <= 0):
                        wall.alive = False
                        wall.color = clr.Fore.RESET

            for cannon in cannons:
                if(cannon.alive and abs(cannon.posX - attackCenter[0]) <= 4 and abs(cannon.posY - attackCenter[1]) <= 4):
                    cannon.health -= 2*self.attackdamage
                    if(cannon.health <= cannon.maxHealth*2/3):
                        cannon.color = clr.Fore.YELLOW
                    if(cannon.health <= cannon.maxHealth/3):
                        cannon.color = clr.Fore.RED
                    if(cannon.health <= 0):
                        cannon.alive = False
                        cannon.color = clr.Fore.RESET

            for wizardTower in wizardTowers:
                if(wizardTower.alive and abs(wizardTower.posX - attackCenter[0]) <= 4 and abs(wizardTower.posY - attackCenter[1]) <= 4):
                    wizardTower.health -= 2*self.attackdamage
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
                        townHall.health -= 2*self.attackdamage
                        if(townHall.health <= townHall.maxHealth*2/3):
                            townHall.color = clr.Fore.YELLOW
                        if(townHall.health <= townHall.maxHealth/3):
                            townHall.color = clr.Fore.RED
                        if(townHall.health <= 0):
                            townHall.alive = False
                            townHall.color = clr.Fore.RESET