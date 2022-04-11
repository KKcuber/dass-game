from src.GameObject import GameObject
import colorama as clr
import sys

from src.TownHall import TownHall

def manhattanDistance(object1, object2):
    return abs(object1.posX - object2.posX) + abs(object1.posY - object2.posY)

class Balloon(GameObject):
    def __init__(self, posX, posY, char, sizeX, sizeY, color, health):
        GameObject.__init__(self, posX, posY, char, sizeX, sizeY, color, health)
        self.vel = 1
        self.attackdamage = 0.5
        self.currentTarget = None
        self.attackTarget = False
        self.townHallPosition = None
        self.range = 1

    def moveAndAttack(self, walls, townHall, cannons, huts, screen, rageSpellActive, wizardTowers):
        # if attacking target then decrease target's health
        if(self.attackTarget):
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
                            
                goto = True
                # Balloon prioritizes to attack defensive buildings first, so it will go through defensive buildings first
                if(self.currentTarget != None):
                    goto = False

                if(goto):
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


            # move towards target
            else:
                if(manhattanDistance(self, self.currentTarget) > self.range):
                    if(self.posX < self.currentTarget.posX):
                        self.posX += self.vel
                    elif(self.posX > self.currentTarget.posX):
                        self.posX -= self.vel
                    elif(self.posY < self.currentTarget.posY):
                            self.posY += self.vel
                    elif(self.posY > self.currentTarget.posY):
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