from room import *
from dialogue import *
from battle import *
from story import *




def makeRoom(i, j, roomID, whatEnemies = "", extraDialogue = "", whatShopItems = None):
  # Room(roomID: int = 100, event = None,  description = "")
  # print(roomID)
  blankRoom = Room(roomID)
  if blankRoom.type == "2":
    blankRoom.event = "shop"
    # NOTE: Shops are not implemented yet.
  elif blankRoom.type == "3":
    blankRoom.event = "treasure"
    # NOTE: Treasure is not implemented yet.
  elif blankRoom.type == "1" or blankRoom.type == "5":
    encounter = Battle()
    encounter.addEnemy(whatEnemies)
    encounter.addPartyMember(player)
    blankRoom.event = encounter
    
  elif blankRoom.type == "4":
    cutsceneRoom = Dialogue()
    blankRoom.event = cutsceneRoom
  elif blankRoom.type == "6":
    blankRoom.event = "trap"
    # NOTE: Traps are not implemented yet.
  elif blankRoom.type == "7":
    blankRoom.event = "npc"
    # NOTE: NPCs are not implemented yet.
  else:
    mainRoom = "none"
  blankRoom.processDesc()
  intarouRooms[i][j] = blankRoom