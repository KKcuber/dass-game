from src.GameObject import GameObject
import time
import colorama as clr
import sys

def euclideanDistance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

class WizardTower(GameObject):
    def __init__(self, posX, posY,char, color, health):
        GameObject.__init__(self, posX, posY, char, 1, 1, color, health)
        self.damage = 3
        self.currentTarget = None

    def attack(self, king, barbarians, archers, balloons):
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
            for balloon in balloons:
                if(balloon.alive):
                    if(abs(self.posX - balloon.posX) + abs(self.posY - balloon.posY) < minDistance):
                        self.currentTarget = balloon
                        minDistance = abs(self.posX - balloon.posX) + abs(self.posY - balloon.posY)
            if(king.alive and abs(self.posX - king.posX) + abs(self.posY - king.posY) <= minDistance):
                self.currentTarget = king
                minDistance = abs(self.posX - king.posX) + abs(self.posY - king.posY)
            if(minDistance <= 6):
                for barbarian in barbarians:
                    if(euclideanDistance(barbarian.posX, barbarian.posY, self.currentTarget.posX, self.currentTarget.posY) < 1.8):
                        barbarian.health -= self.damage
                        if(barbarian.health <= barbarian.maxHealth*2/3):
                            barbarian.color = clr.Fore.YELLOW
                        if(barbarian.health <= barbarian.maxHealth/3):
                            barbarian.color = clr.Fore.RED
                        if(barbarian.health <= 0):
                            barbarian.alive = False
                            barbarian.color = clr.Fore.RESET
                for archer in archers:
                    if(euclideanDistance(archer.posX, archer.posY, self.currentTarget.posX, self.currentTarget.posY) < 1.8):
                        archer.health -= self.damage
                        if(archer.health <= archer.maxHealth*2/3):
                            archer.color = clr.Fore.YELLOW
                        if(archer.health <= archer.maxHealth/3):
                            archer.color = clr.Fore.RED
                        if(archer.health <= 0):
                            archer.alive = False
                            archer.color = clr.Fore.RESET
                if(euclideanDistance(king.posX, king.posY, self.currentTarget.posX, self.currentTarget.posY) < 1.8):
                    king.health -= self.damage
                    if(king.health <= king.maxHealth*2/3):
                        king.color = clr.Fore.YELLOW
                    if(king.health <= king.maxHealth/3):
                        king.color = clr.Fore.RED
                    if(king.health <= 0):
                        king.alive = False
                        king.color = clr.Fore.RESET
                for balloon in balloons:
                    if(euclideanDistance(balloon.posX, balloon.posY, self.currentTarget.posX, self.currentTarget.posY) < 1.8):
                        balloon.health -= self.damage
                        if(balloon.health <= balloon.maxHealth*2/3):
                            balloon.color = clr.Fore.YELLOW
                        if(balloon.health <= balloon.maxHealth/3):
                            balloon.color = clr.Fore.RED
                        if(balloon.health <= 0):
                            balloon.alive = False
                            balloon.color = clr.Fore.RESET
                