from helper import *
from character import *
from choices import *
from dialogue import *
from room import *
from npc import *
import os
# age = 512
# age1 = str(age)
# self.type = age1[0]
# print(age1[0])


# hi Dave (:
'''
(roomNumber)(numOfExits)(areaType)

The first digit is the room number.
The second digit is the number of exits.
The last digit is the area type (shops, enemies, bosses, etc.).

age = 512
age[0] = 5

Examples:

Normal/No Event Rooms (0):
010 - normal room with 1 exit
020 - normal room with 2 exits
030 - normal room with 3 exits
040 - normal room with 4 exits

Enemy Rooms (1):
012 - enemy room with 1 exit
022 - enemy room with 2 exits
032 - enemy room with 3 exits
042 - enemy room with 4 exits

Shop Rooms (2):
012 - shop room with 1 exit
022 - shop room with 2 exits
032 - shop room with 3 exits
042 - shop room with 4 exits


Treasure Rooms (3):
013 - treasure room with 1 exit
023 - treasure room with 2 exits
033 - treasure room with 3 exits
043 - treasure room with 4 exits

Cutscene Rooms (4):
014 - cutscene room with 1 exit
024 - cutscene room with 2 exits
034 - cutscene room with 3 exits
044 - cutscene room with 4 exits

Boss Rooms (5):
015 - boss room with 1 exit
025 - boss room with 2 exits
035 - boss room with 3 exits
045 - boss room with 4 exits

Trap Tooms (6):
016 - trap room with 1 exit
026 - trap room with 2 exits
036 - trap room with 3 exits
046 - trap room with 4 exits
'''

map = []

class Area():
  
  
  def __init__(self):
    self.rooms = []
    self.directions = []
    self.map = [[000, 000, 114, 000, 000],
                [000, 114, 140, 112, 000],
                [000, 115, 140, 144, 000],
                [000, 115, 140, 000, 000]]
    
  def addRoom(self):
    for i in range(len(self.map)):
      self.rooms.append([])
      currentRow = self.rooms[i]
      for j in range(len(self.map[i])):
        if self.map[i][j] > 100:
          currentRow.append(Room(self.map[i][j]))
        else:
          currentRow.append(None)
      
    for i in range(len(self.rooms)):
      for j in range(len(self.rooms[i])):
        if self.rooms[i][j] != None:
          self.rooms[i][j].processDesc()
          #print(self.rooms[i][j].description)
          #input("test")
      print(self.rooms[i])
    print(self.map)
    #input("This is to check the area")
    os.system("clear")


# Intarough = Area()
# currentRoom = [1, 3]
# currentRoom[1] += 1
