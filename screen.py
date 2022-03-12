import numpy as np
import sys
import os
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
import time

class Screen:
    frameTime = 1/60.0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screenarr = np.array([[' ' for x in range(width)] for y in range(height)], dtype=object)
        self.state = 'running'

    def clear(self):
        self.screenarr = np.array([[' ' for x in range(self.width)] for y in range(self.height)], dtype=object) 
        # print("\033[%d;%dH" % (0, 0))
        # os.system('clear') 

    def printScreen(self, kingHealth):
        printString = ''
        for row in self.screenarr:
            for column in row:
                printString += column
            printString += '\n'
        printString += "King's Health: "
        for i in range(int(kingHealth/10)):
            printString += '|'
        sys.stdout.write(printString)
        return printString