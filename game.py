import imp
from src.screen import *
from src.king import *
import colorama as clr
import time
from src.walls import Walls
from src.TownHall import TownHall
from src.hut import Huts
from src.cannon import Cannon
from src.barbarian import Barbarian
import pickle as pkl
from src.archer import *
from src.balloon import *
from src.queen import *
from src.wizardTower import *
from threading import Timer
import time

#    |
#  --+-----> X
#    |
#    |
#    V
#    Y

# clear terminal every time you start the game
os.system('clear')

# array for all printStrings
printStrings = []

# creating objects
screen = Screen(80, 25)
walls = Walls('#', clr.Fore.GREEN, 30)
huts = Huts('H', clr.Fore.GREEN, 60)
townHall = TownHall(38, 12, clr.Fore.GREEN, 200)
cannons = [Cannon(33, 12, 'C', clr.Fore.GREEN, 200), Cannon(47, 17, 'C', clr.Fore.GREEN, 200)]
wizardTowers = [WizardTower(36, 10, 'W', clr.Fore.GREEN, 200), WizardTower(44, 18, 'W', clr.Fore.GREEN, 200)]

# Useful variables
prevFrameTime = time.time()
archers = []
barbarians = []
balloons = []
numBalloons = 0
numBarbarians = 0
numArchers = 0
rageSpellTime = None
level = 1

# save replay function
def saveReplay():
    # ask user for filename
    filename = input("Enter filename for replay to be saved in: ")
    if(filename == 'q'):
        return
    # open file
    file = open('replays/' + filename, 'wb')
    # save all printStrings
    pkl.dump(printStrings, file)
    # close file
    file.close()
    print("Replay saved! UwU")

print("Welcome to the game!")
print("Which character do you want to play?")
print("1. King")
print("2. Archer Queen")
print("Enter 1 or 2: ")
choice = input()
if(choice == '1'):
    king = King(0, 0, 'K',1, 1, clr.Fore.BLUE, 100)
else:
    king = Queen(0, 0, 'Q',1, 1, clr.Fore.BLUE, 100)


#render loop
while(1):
    inputchar = input_to(Get())
    if(inputchar == 'q'):
        break
    if(inputchar == '1' and numBarbarians < 6):
        barbarians.append(Barbarian(79, 0, 'B', 1, 1, clr.Fore.BLUE, 60))
        numBarbarians += 1
    if(inputchar == '2' and numBarbarians < 6):
        barbarians.append(Barbarian(79, 24, 'B', 1, 1, clr.Fore.BLUE, 60))
        numBarbarians += 1
    if(inputchar == '3' and numBarbarians < 6):
        barbarians.append(Barbarian(0, 24, 'B', 1, 1, clr.Fore.BLUE, 30))
        numBarbarians += 1

    # spawn archers
    if(inputchar == '4' and numArchers < 4):
        archers.append(Archer(79, 0, 'A', 1, 1, clr.Fore.BLUE, 30))
        numArchers += 1
    if(inputchar == '5' and numArchers < 4):
        archers.append(Archer(79, 24, 'A', 1, 1, clr.Fore.BLUE, 30))
        numArchers += 1
    if(inputchar == '6' and numArchers < 4):
        archers.append(Archer(0, 24, 'A', 1, 1, clr.Fore.BLUE, 30))
        numArchers += 1

    # spawn balloons
    if(inputchar == '7' and numBalloons < 6):
        balloons.append(Balloon(79, 0, 'O', 1, 1, clr.Fore.BLUE, 30))
        numBalloons += 1
    if(inputchar == '8' and numBalloons < 6):
        balloons.append(Balloon(79, 24, 'O', 1, 1, clr.Fore.BLUE, 30))
        numBalloons += 1
    if(inputchar == '9' and numBalloons < 6):
        balloons.append(Balloon(0, 24, 'O', 1, 1, clr.Fore.BLUE, 30))
        numBalloons += 1

    # check for game endings
    # game ending can be of 2 types - victory or defeat
    # if all king and barbarians die, then game ends in defeat
    # if all buildings other than walls are destroyed, then game ends in victory
    allBarbariansDead = True
    for barbarian in barbarians:
        if(barbarian.alive):
            allBarbariansDead = False
            break
    allArchersDead = True
    for archer in archers:
        if(archer.alive):
            allArchersDead = False
            break
    allBalloonsDead = True
    for balloon in balloons:
        if(balloon.alive):
            allBalloonsDead = False
            break
    if(not king.alive and allBarbariansDead and allArchersDead and allBalloonsDead):
        screen.clear()
        os.system('clear')
        print('Game Over! You lost!')
        print('\n\nPress q to quit or any other key to save replay\n\n')
        saveReplay()
        exit()

    # defeat
    allHutsDead = True
    for hut in huts.hutsArray:
        if(hut.alive):
            allHutsDead = False
            break
    allCannonsDead = True
    for cannon in cannons:
        if(cannon.alive):
            allCannonsDead = False
            break
    allWizardTowersDead = True
    for wizardTower in wizardTowers:
        if(wizardTower.alive):
            allWizardTowersDead = False
            break
    if(allWizardTowersDead and allHutsDead and allCannonsDead and not townHall.alive):
        level = level+1
        if(level <=3):
            os.system('clear')
            print("You won! On to Level " + str(level) + "!")
            time.sleep(2)
        numArchers = 0
        numBarbarians = 0
        numBalloons = 0
        balloons.clear()
        archers.clear()
        barbarians.clear()
        for hut in huts.hutsArray:
            hut.alive = True
            hut.health = hut.maxHealth
        for cannon in cannons:
            cannon.alive = True
            cannon.health = cannon.maxHealth
        for wizardTower in wizardTowers:
            wizardTower.alive = True
            wizardTower.health = wizardTower.maxHealth
        townHall.alive = True
        king.alive = True
        king.health = king.maxHealth
        townHall.health = townHall.maxHealth
        king.posX = 0
        king.posY = 0
        walls.revive()
        rageSpellTime = None

        if(level == 2):
            cannons.append(Cannon(39,9, 'C', clr.Fore.GREEN, 200))
            wizardTowers.append(WizardTower(32, 17, 'W', clr.Fore.GREEN, 200))
        if(level == 3):
            cannons.append(Cannon(35, 15, 'C', clr.Fore.GREEN, 200))
            wizardTowers.append(WizardTower(43, 13, 'W', clr.Fore.GREEN, 200))
        if(level == 4):
            screen.clear()
            os.system('clear')
            print('Game Over! You Win!')
            print('\n\nPress q to quit or any other key to save replay\n\n')
            saveReplay()
            exit()

    # heal spell heals all troops - barbarians and king and increases health by 150% capped at max Health
    if(inputchar == 'h'):
        king.health = min(king.health + king.maxHealth/2, king.maxHealth)
        if(king.health >= king.maxHealth*2/3):
            king.color = clr.Fore.BLUE
        elif(king.health >= king.maxHealth/3):
            king.color = clr.Fore.YELLOW
        else:
            king.color = clr.Fore.RED
        for barbarian in barbarians:
            barbarian.health = min(barbarian.health + barbarian.maxHealth/2, barbarian.maxHealth)
            if(barbarian.health >= barbarian.maxHealth*2/3):
                barbarian.color = clr.Fore.BLUE
            elif(barbarian.health >= barbarian.maxHealth/3):
                barbarian.color = clr.Fore.YELLOW
            else:
                barbarian.color = clr.Fore.RED
        for archer in archers:
            archer.health = min(archer.health + archer.maxHealth/2, archer.maxHealth)
            if(archer.health >= archer.maxHealth*2/3):
                archer.color = clr.Fore.BLUE
            elif(archer.health >= archer.maxHealth/3):
                archer.color = clr.Fore.YELLOW
            else:
                archer.color = clr.Fore.RED
        for balloon in balloons:
            balloon.health = min(balloon.health + balloon.maxHealth/2, balloon.maxHealth)
            if(balloon.health >= balloon.maxHealth*2/3):
                balloon.color = clr.Fore.BLUE
            elif(balloon.health >= balloon.maxHealth/3):
                balloon.color = clr.Fore.YELLOW
            else:
                balloon.color = clr.Fore.RED

    # rage spell - doubles damage and movement speed for 3 senconds
    if(inputchar == 'r'):
        if(rageSpellTime == None):
            rageSpellTime = time.time()
            king.attackdamage = king.attackdamage * 2
            king.vel = 2
            for barbarian in barbarians:
                barbarian.attackdamage = barbarian.attackdamage * 2
                barbarian.vel = 2
            for archer in archers:
                archer.attackdamage = archer.attackdamage * 2
                archer.vel = 2
            for balloon in balloons:
                balloon.attackdamage = balloon.attackdamage * 2
                balloon.vel = 2

    # Check if rage spell has finished
    if(rageSpellTime != None and time.time() - rageSpellTime > 3 and rageSpellTime != 0):
        rageSpellTime = 0
        king.vel = 1
        king.attackdamage = king.attackdamage / 2
        for barbarian in barbarians:
            barbarian.attackdamage = barbarian.attackdamage / 2
            barbarian.vel = 1
        for archer in archers:
            archer.attackdamage = archer.attackdamage / 2
            archer.vel = 1
        for balloon in balloons:
            balloon.attackdamage = balloon.attackdamage / 2
            balloon.vel = 1
    
    # draw all elements
    king.draw(screen)
    walls.draw(screen)
    townHall.draw(screen)
    huts.draw(screen)
    for wizardTower in wizardTowers:
        wizardTower.draw(screen)
    for cannon in cannons:
        cannon.draw(screen)
    for barbarian in barbarians:
        barbarian.draw(screen)
    for archer in archers:
        archer.draw(screen)
    for balloon in balloons:
        balloon.draw(screen)

    # update all elements
    if(inputchar == ' '):
        if(king.alive):
            king.attack(walls, townHall, cannons, huts, wizardTowers)
    
    # queen special attack
    if(inputchar == 'l'):
        if(king.alive):
            attackCenter = king.findAttackPositionForQueenSpecialAttack()
            r = Timer(1.0,king.specialAttack, (walls, townHall, cannons, huts, wizardTowers, attackCenter))
            r.start()
    for cannon in cannons:
        if(cannon.alive):
            cannon.attack(king, barbarians, archers)
    for wizardTower in wizardTowers:
        if(wizardTower.alive):
            wizardTower.attack(king, barbarians, archers, balloons)

    flag = True
    if(rageSpellTime == None or rageSpellTime == 0):
        flag = False
    for barbarian in barbarians:
        if(barbarian.alive):
            barbarian.moveAndAttack( walls, townHall, cannons, huts, screen, flag, wizardTowers)
    for archer in archers:
        if(archer.alive):
            archer.moveAndAttack( walls, townHall, cannons, huts, screen, flag, wizardTowers)
    for balloon in balloons:
        if(balloon.alive):
            balloon.moveAndAttack( walls, townHall, cannons, huts, screen, flag, wizardTowers)
    if(king.alive):
        king.move(inputchar, screen, flag)
    if(time.time() - prevFrameTime > screen.frameTime):
        os.system('clear')
        printString = screen.printScreen(king.health)
        printStrings.append(printString)
        screen.clear()
        prevFrameTime = time.time()