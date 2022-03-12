import pickle as pkl
import time
import sys
import os

# ask user for filename
filename = input("Enter filename for replay to be loaded from: ")
# open file
file = open('replays/' + filename, 'rb')
# load all printStrings
printStrings = pkl.load(file)
# close file
file.close()

#print all screens one by one at 60 fps
for i in range(len(printStrings)):
    sys.stdout.write(printStrings[i])
    time.sleep(1/30)
    os.system('clear')