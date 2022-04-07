from src.GameObject import GameObject
import time
import colorama as clr

class Cannon(GameObject):
    def __init__(self, posX, posY,char, color, health):
        GameObject.__init__(self, posX, posY, char, 1, 1, color, health)
        self.lastAttack = time.time()
        self.cannonDamage = 10
        self.currentTarget = None

    def attack(self, king, barbarians, archers):
        if(time.time() - self.lastAttack > 1):
            self.lastAttack = time.time()
            minDistance = 99999
            for barbarian in barbarians:
                if(barbarian.alive):
                    if(abs(self.posX - barbarian.posX) + abs(self.posY - barbarian.posY) < minDistance):
                        self.currentTarget = barbarian
                        minDistance = abs(self.posX - barbarian.posX) + abs(self.posY - barbarian.posY)
            for archer in archers:
                if(archer.alive):
                    if(abs(self.posX - archer.posX) + abs(self.posY - archer.posY) < minDistance):
                        self.currentTarget = archer
                        minDistance = abs(self.posX - archer.posX) + abs(self.posY - archer.posY)
            if(king.alive and abs(self.posX - king.posX) + abs(self.posY - king.posY) <= minDistance):
                self.currentTarget = king
                minDistance = abs(self.posX - king.posX) + abs(self.posY - king.posY)
            if(minDistance <= 6):
                self.currentTarget.health -= self.cannonDamage
                if(self.currentTarget.health <= self.currentTarget.maxHealth*2/3):
                    self.currentTarget.color = clr.Fore.YELLOW
                if(self.currentTarget.health <= self.currentTarget.maxHealth/3):
                    self.currentTarget.color = clr.Fore.RED
                if(self.currentTarget.health <= 0):
                    self.currentTarget.alive = False
                    self.currentTarget.color = clr.Fore.RESET
                    self.currentTarget = None
                