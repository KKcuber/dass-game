from src.GameObject import GameObject
import colorama as clr
import sys

from src.TownHall import TownHall

def getWallIndex(x,y, walls):
    for wall in walls.wallsArray:
        if(wall.posX == x and wall.posY == y and wall.alive):
            return wall
    return None

def manhattanDistance(object1, object2):
    return abs(object1.posX - object2.posX) + abs(object1.posY - object2.posY)

class Archer(GameObject):
    def __init__(self, posX, posY, char, sizeX, sizeY, color, health):
        GameObject.__init__(self, posX, posY, char, sizeX, sizeY, color, health)
        self.vel = 1
        self.attackdamage = 0.5
        self.currentTarget = None
        self.attackWall = None
        self.attackTarget = False
        self.townHallPosition = None
        self.range = 8

    def moveAndAttack(self, walls, townHall, cannons, huts, screen, rageSpellActive, wizardTowers):
        # if attacking a wall then decrease wall's health
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

        # if attacking target then decrease target's health
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

        # if not attacking then find nearest wall/hut/town hall according to manhattan distance or move towards target
        else:
            # if no target, then set current target to nearest wall/hut/town hall
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

                for wizardTower in wizardTowers:
                    if(wizardTower.alive):
                        if(abs(self.posX - wizardTower.posX) + abs(self.posY - wizardTower.posY) < minDistance):
                            self.currentTarget = wizardTower
                            minDistance = abs(self.posX - wizardTower.posX) + abs(self.posY - wizardTower.posY)
            # move towards target
            else:
                if(manhattanDistance(self, self.currentTarget) > self.range):
                    if(self.posX < self.currentTarget.posX):
                        for i in range(self.posX, self.currentTarget.posX):
                            if(getWallIndex(i, self.posY, walls) != None):
                                self.posX = i - 1
                                self.attackWall = getWallIndex(i, self.posY, walls)
                                break
                        if(self.attackWall == None):
                            self.posX += self.vel
                    elif(self.posX > self.currentTarget.posX):
                        for i in range(self.posX, self.currentTarget.posX, -1):
                            if(getWallIndex(i, self.posY, walls) != None):
                                self.posX = i + 1
                                self.attackWall = getWallIndex(i, self.posY, walls)
                                break
                        if(self.attackWall == None):
                            self.posX -= self.vel
                    elif(self.posY < self.currentTarget.posY):
                        for i in range(self.posY, self.currentTarget.posY):
                            if(getWallIndex(self.posX, i, walls) != None):
                                self.posY = i - 1
                                self.attackWall = getWallIndex(self.posX, i, walls)
                                break
                        if(self.attackWall == None):
                            self.posY += self.vel
                    elif(self.posY > self.currentTarget.posY):
                        for i in range(self.posY, self.currentTarget.posY, -1):
                            if(getWallIndex(self.posX, i, walls) != None):
                                self.posY = i + 1
                                self.attackWall = getWallIndex(self.posX, i, walls)
                                break
                        if(self.attackWall == None):
                            self.posY -= self.vel
                else:
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