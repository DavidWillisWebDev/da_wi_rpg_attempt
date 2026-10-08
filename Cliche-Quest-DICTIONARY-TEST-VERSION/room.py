from helper import *
from character import *
from dialogue import *
from npc import *

roomTypesDict = {
  "0" : ["standardRoom", "This is a standard room, nothing special."],
  "1" : ["enemyRoom", "This is an enemy room."],
  "2" : ["shopRoom", "This is a shop room."],
  "3" : ["treasureRoom", "This is a treasure room."],
  "4" : ["cutsceneRoom", "This is a cutscene room."],
  "5" : ["bossRoom", "This is a boss room."],
  "6" : ["trapRoom", "This is definitely not a trap room. What's the worst that could happen?"]
}

roomExitDict = {
  "oneExit" : 1,
  "twoExits" : 2,
  "threeExits" : 3,
  "fourExits" : 4
}

class Room():

  def __init__(self, roomID: int = 100, description = ""): 
    self.npcs = []
    self.roomID = roomID
    self.num = str(self.roomID)[0]
    self.exits = str(self.roomID)[1]
    self.type = str(self.roomID)[2]
    self.description = description

  # adds an npc to this room
  def addNPC(self, npc):
    self.npcs.append(npc)

  """
  def addExit(self, exit):
    self.exits = exit
  """
  
  def addDesc(self, desc):
    self.description = desc
    #print(self.description)
    #input("descriptions should be here")

  """
  def processExits(self, room):
    if self.exits == 1:
      self.exits(roomExitDict.get("oneExit"))
    if self.exits == 2:
      self.addDesc(roomExitDict.get("twoExits"))
    if self.exits == 3:
      self.addDesc(roomExitDict.get("threeExits"))
    if self.exits == 4:
      self.addDesc(roomExitDict.get("fourExits"))
  """

  def processDesc(self):
    #input(roomTypesDict.get("0")[1])
    if self.type == "0":
      self.addDesc(roomTypesDict.get("0")[1])
    if self.type == "1":
      self.addDesc(roomTypesDict.get("1")[1])
    if self.type == "2":
      self.addDesc(roomTypesDict.get("2")[1])
    if self.type == "3":
      self.addDesc(roomTypesDict.get("3")[1])
    if self.type == "4":
      self.addDesc(roomTypesDict.get("4")[1])
    if self.type == "5":
      self.addDesc(roomTypesDict.get("5")[1])
    if self.type == "6":
      self.addDesc(roomTypesDict.get("6")[1])
      
      
  def shop(self, inventory):
    self.inventory = []

  #def roomDesc(self, dialogue):


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



room1 = Room(141, "This is where you started your quest.")

#room2 = Room()