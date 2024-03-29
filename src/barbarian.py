from src.GameObject import GameObject
import colorama as clr
import sys

from src.TownHall import TownHall

def getWallIndex(x,y, walls):
    for wall in walls.wallsArray:
        if(wall.posX == x and wall.posY == y):
            return wall

class Barbarian(GameObject):
    def __init__(self, posX, posY, char, sizeX, sizeY, color, health):
        GameObject.__init__(self, posX, posY, char, sizeX, sizeY, color, health)
        self.vel = 1
        self.attackdamage = 4
        self.currentTarget = None
        self.attackWall = None
        self.attackTarget = False
        self.townHallPosition = None
        self.move = 1

    def moveAndAttack(self, walls, townHall, cannons, huts, screen, rageSpellActive, wizardTowers):
        self.move +=1
        if(self.move%2 == 0):
            if(self.attackWall != None):
                self.attackWall.health -= self.attackdamage
                if(self.attackWall.health <= self.attackWall.maxHealth*2/3):
                    self.attackWall.color = clr.Fore.YELLOW
                if(self.attackWall.health <= self.attackWall.maxHealth/3):
                    self.attackWall.color = clr.Fore.RED
                if(self.attackWall.health <= 0):
                    self.attackWall.alive = False
                    self.attackWall.color = clr.Fore.RESET
                    # self.attackWall.char = ' '
                    self.attackWall = None
            elif(self.attackTarget):
                self.currentTarget.health -= self.attackdamage
                if(self.currentTarget.health <= self.currentTarget.maxHealth*2/3):
                    self.currentTarget.color = clr.Fore.YELLOW
                if(self.currentTarget.health <= self.currentTarget.maxHealth/3):
                    self.currentTarget.color = clr.Fore.RED
                if(self.currentTarget.health <= 0):
                    self.currentTarget.alive = False
                    self.currentTarget.color = clr.Fore.RESET
                    self.currentTarget = None
                    self.attackTarget = False
            else:
                if(self.currentTarget == None or self.currentTarget.alive == False):
                    # find nearest wall/hut/town hall according to manhattan distance
                    minDistance = 99999
                    for hut in huts.hutsArray:
                        if(hut.alive):
                            if(abs(self.posX - hut.posX) + abs(self.posY - hut.posY) < minDistance):
                                self.currentTarget = hut
                                minDistance = abs(self.posX - hut.posX) + abs(self.posY - hut.posY)

                    for x in range(townHall.posX, townHall.posX + townHall.sizeX):
                        for y in range(townHall.posY, townHall.posY + townHall.sizeY):
                            if(townHall.alive):
                                if(abs(self.posX- x) + abs(self.posY - y) < minDistance):
                                    self.currentTarget = townHall
                                    self.townHallPosition = (x,y)
                                    minDistance = abs(self.posX - x) + abs(self.posY - y)

                    for cannon in cannons:
                        if(cannon.alive):
                            if(abs(self.posX - cannon.posX) + abs(self.posY - cannon.posY) < minDistance):
                                self.currentTarget = cannon
                                minDistance = abs(self.posX - cannon.posX) + abs(self.posY - cannon.posY)
                    
                    for tower in wizardTowers:
                        if(tower.alive):
                            if(abs(self.posX - tower.posX) + abs(self.posY - tower.posY) < minDistance):
                                self.currentTarget = tower
                                minDistance = abs(self.posX - tower.posX) + abs(self.posY - tower.posY)

                else:
                    if(self.posY != self.currentTarget.posY):
                        if(self.posY > self.currentTarget.posY):
                            if(screen.screenarr[self.posY - self.vel][self.posX] == ' ' or screen.screenarr[self.posY - self.vel][self.posX] == 'B'):
                                self.posY -= self.vel
                            elif(screen.screenarr[self.posY - self.vel][self.posX][5] == '#'):
                                self.attackWall = getWallIndex(self.posX, self.posY - self.vel, walls)
                            elif(screen.screenarr[self.posY - self.vel][self.posX][5] == self.currentTarget.char):
                                self.attackTarget = True
                        else:
                            if(screen.screenarr[self.posY + self.vel][self.posX] == ' ' or screen.screenarr[self.posY - self.vel][self.posX] == 'B'):
                                self.posY += self.vel
                            elif(screen.screenarr[self.posY + self.vel][self.posX][5] == '#'):
                                self.attackWall = getWallIndex(self.posX, self.posY + self.vel, walls)
                            elif(screen.screenarr[self.posY + self.vel][self.posX][5] == self.currentTarget.char):
                                self.attackTarget = True
                    elif(self.posX != self.currentTarget.posX):
                        if(self.posX > self.currentTarget.posX):
                            if(screen.screenarr[self.posY][self.posX - self.vel] == ' ' or screen.screenarr[self.posY - self.vel][self.posX] == 'B'):
                                self.posX -= self.vel
                            elif(screen.screenarr[self.posY][self.posX - self.vel][5] == '#'):
                                self.attackWall = getWallIndex(self.posX - self.vel, self.posY, walls)
                            elif(screen.screenarr[self.posY][self.posX - self.vel][5] == self.currentTarget.char):
                                self.attackTarget = True
                        else:
                            if(screen.screenarr[self.posY][self.posX + self.vel] == ' ' or screen.screenarr[self.posY - self.vel][self.posX] == 'B'):
                                self.posX += self.vel
                            elif(screen.screenarr[self.posY][self.posX + self.vel][5] == '#'):
                                self.attackWall = getWallIndex(self.posX + self.vel, self.posY, walls)
                            elif(screen.screenarr[self.posY][self.posX + self.vel][5] == self.currentTarget.char):
                                self.attackTarget = True
                    
            # else:
            #     self.currentTarget.health -= self.attackdamage
            #     if(self.currentTarget.health <= self.currentTarget.maxHealth*2/3):
            #         self.currentTarget.color = clr.Fore.YELLOW
            #     if(self.currentTarget.health <= self.currentTarget.maxHealth/3):
            #         self.currentTarget.color = clr.Fore.RED
            #     if(self.currentTarget.health <= 0):
            #         self.currentTarget.alive = False
            #         self.currentTarget.color = clr.Fore.RESET
            #         self.currentTarget = None