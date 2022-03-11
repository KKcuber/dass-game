from screen import *
from king import *
import colorama as clr
import time
from walls import Walls
from TownHall import TownHall
from hut import Huts
from cannon import Cannon
#    |
#  --+-----> Y
#    |
#    |
#    V
#    X

#clear terminal every time you start the game
os.system('clear')
screen = Screen(80, 25)
king = King(0, 0, 'K',1, 1, clr.Fore.BLUE)
walls = Walls('#', clr.Fore.GREEN)
huts = Huts('H', clr.Fore.GREEN)
townHall = TownHall(38, 12, clr.Fore.GREEN)
prevFrameTime = time.time()
cannon1 = Cannon(33, 12, 'C', clr.Fore.GREEN)
cannon2 = Cannon(47, 17, 'C', clr.Fore.GREEN)
#render loop
while(1):
    inputchar = input_to(Get())
    if(inputchar == 'q'):
        break
    king.draw(screen)
    walls.draw(screen)
    townHall.draw(screen)
    huts.draw(screen)
    cannon1.draw(screen)
    cannon2.draw(screen)
    cannon1.attack(king)
    cannon2.attack(king)
    king.move(inputchar, screen)
    if(time.time() - prevFrameTime > screen.frameTime):
        os.system('clear')
        screen.printScreen(king.health)
        screen.clear()
        prevFrameTime = time.time()