from matplotlib.pyplot import bar
from screen import *
from king import *
import colorama as clr
import time
from walls import Walls
from TownHall import TownHall
from hut import Huts
from cannon import Cannon
from barbarian import Barbarian
import pickle as pkl

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
king = King(0, 0, 'K',1, 1, clr.Fore.BLUE, 100)
walls = Walls('#', clr.Fore.GREEN, 30)
huts = Huts('H', clr.Fore.GREEN, 60)
townHall = TownHall(38, 12, clr.Fore.GREEN, 100)
cannon1 = Cannon(33, 12, 'C', clr.Fore.GREEN, 60)
cannon2 = Cannon(47, 17, 'C', clr.Fore.GREEN, 60)

# Useful variables
prevFrameTime = time.time()
barbarians = []
numBarbarians = 0
rageSpellTime = None

# save replay function
def saveReplay():
    # ask user for filename
    filename = input("Enter filename for replay to be saved in: ")
    # open file
    file = open(filename, 'wb')
    # save all printStrings
    pkl.dump(printStrings, file)
    # close file
    file.close()
    print("Replay saved! UwU")

#render loop
while(1):
    inputchar = input_to(Get())
    if(inputchar == 'q'):
        break
    if(inputchar == '1' and numBarbarians < 10):
        barbarians.append(Barbarian(79, 0, 'B', 1, 1, clr.Fore.BLUE, 30))
        numBarbarians += 1
    if(inputchar == '2' and numBarbarians < 10):
        barbarians.append(Barbarian(79, 24, 'B', 1, 1, clr.Fore.BLUE, 30))
        numBarbarians += 1
    if(inputchar == '3' and numBarbarians < 10):
        barbarians.append(Barbarian(0, 24, 'B', 1, 1, clr.Fore.BLUE, 30))
        numBarbarians += 1

    # check for game endings
    # game ending can be of 2 types - victory or defeat
    # if all king and barbarians die, then game ends in defeat
    # if all buildings other than walls are destroyed, then game ends in victory
    allBarbariansDead = True
    for barbarian in barbarians:
        if(barbarian.alive):
            allBarbariansDead = False
            break
    if(not king.alive and allBarbariansDead):
        screen.clear()
        os.system('clear')
        print('Game Over! You lost!')
        exit()

    # defeat
    allHutsDead = True
    for hut in huts.hutsArray:
        if(hut.alive):
            allHutsDead = False
            break
    if(allHutsDead and not cannon1.alive and not cannon2.alive and not townHall.alive):
        screen.clear()
        os.system('clear')
        print('Game Over! You Win!')
        print('\n\nPress q to quit or any other key to save replay\n\n')
        if(input_to(Get()) == 'q'):
            exit()
        else:
            saveReplay()
            exit()

    # heal spell heals all troops - barbarians and king and increases health by 150% capped at max Health
    if(inputchar == 'h'):
        king.health = min(king.health + king.maxHealth/2, king.maxHealth)
        for barbarian in barbarians:
            barbarian.health = min(barbarian.health + barbarian.maxHealth/2, barbarian.maxHealth)

    # rage spell - doubles damage and movement speed for 3 senconds
    if(inputchar == 'r'):
        if(rageSpellTime == None):
            rageSpellTime = time.time()
            king.attackdamage = king.attackdamage * 2
            king.vel = 2
            for barbarian in barbarians:
                barbarian.attackdamage = barbarian.attackdamage * 2
                barbarian.vel = 2

    # Check if rage spell has finished
    if(rageSpellTime != None and time.time() - rageSpellTime > 3 and rageSpellTime != 0):
        rageSpellTime = 0
        king.vel = 1
        king.attackdamage = king.attackdamage / 2
        for barbarian in barbarians:
            barbarian.attackdamage = barbarian.attackdamage / 2
            barbarian.vel = 1
    
    # draw all elements
    king.draw(screen)
    walls.draw(screen)
    townHall.draw(screen)
    huts.draw(screen)
    cannon1.draw(screen)
    cannon2.draw(screen)
    for barbarian in barbarians:
        barbarian.draw(screen)

    # update all elements
    if(inputchar == ' '):
        king.attack(walls, townHall, cannon1, cannon2, huts)
    if(cannon1.alive):
        cannon1.attack(king, barbarians)
    if(cannon2.alive):
        cannon2.attack(king, barbarians)
    flag = True
    if(rageSpellTime == None or rageSpellTime == 0):
        flag = False
    for barbarian in barbarians:
        if(barbarian.alive):
            barbarian.moveAndAttack( walls, townHall, cannon1, cannon2, huts, screen, flag)
    if(king.alive):
        king.move(inputchar, screen, flag)
    if(time.time() - prevFrameTime > screen.frameTime):
        # print("hi", file=sys.stderr)
        os.system('clear')
        printString = screen.printScreen(king.health)
        printStrings.append(printString)
        screen.clear()
        prevFrameTime = time.time()