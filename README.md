# Clash of Clans 

- A Terminal Based game based on the popular game of Clash of Clans 

### To run the game
1. Go into the main directory where game.py is present
2. Run game.py with the command `python game.py`

### To run the replay
1. Go into the main directory where the replay.py is present
2. Run replay.py with the command `python replay.py`

## Features

1. King 
   1. Controls : 
      1. <KBD>W</KBD> - up movement
      2. <KBD>A</KBD> - left movement
      3. <KBD>S</KBD> - right movement
      4. <KBD>D</KBD> - down movement
      5. <KBD>SPACE</KBD> - attack
    2. Health - 100
    3. Damage per attack - 10
2. Barbarians 
   1. These troops can be spawned from 3 spawning points as follows:
        - Top-right = <KBD>1</KBD>
        - Bottom-right = <KBD>2</KBD>
        - Bottom-left = <KBD>3</KBD>
   2. At max 6 barbarians can be spawned
   3. Health - 30
   4. Damage per attack - 1
   5. Barbarians change colour from Green to Yellow to Red on each hit they recieve from the cannon
3. Cannons
   1. It shoots at the nearest target which are at a distance of atmost 6 from the cannon
   2. Health - 200
   3. Damage per attack - 10
4. Spells 
   1. 2 spells of each type, heal and rage have been given for a game 
   2. for heal spell use <KBD>H</KBD> and for rage spell use <KBD>R</KBD>
5. Replay 
    - User is prompted for filename is which he wants to save replay in and the replay is saved in that file. 
    - The user can play the replay by executing the replay.py file.
6. Buildings
    1. Town Hall - A 4x3 structure in the center of the village
    2. Huts - 5 huts scattered around the whole village
