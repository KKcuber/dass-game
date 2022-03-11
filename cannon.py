from GameObject import GameObject
import time

class Cannon(GameObject):
    def __init__(self, posX, posY,char, color):
        GameObject.__init__(self, posX, posY, char, 1, 1, color)
        self.health = 30
        self.maxhealth = 30
        self.lastAttack = time.time()
        self.cannonDamage = 10

    def attack(self, king):
        if(time.time() - self.lastAttack > 1):
            self.lastAttack = time.time()
            # Manhattan Distance
            if(king.alive and abs(self.posX - king.posX) + abs(self.posY - king.posY) <= 6):
                king.health -= self.cannonDamage
                if(king.health <= 0):
                    king.health = 0
                    king.alive = False
                