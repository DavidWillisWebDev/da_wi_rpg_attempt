from room import *
from dialogue import *
from battle import *

def makeRoom(roomID, whatEnemies = "", extraDialogue = ""):
  # Room(roomID: int = 100, event = None,  description = "")
  blankRoom = Room(roomID)
  if blankRoom.type == "2":
    blankRoom.event = "shop"
    # NOTE: Shops are not implemented yet.
  elif blankRoom.type == "3":
    encounter = Battle(blankRoom)
    encounter.addEnemy(whatEnemy)
  elif blankRoom.type == "4":
    cutsceneRoom = Dialogue()
  else:
    mainRoom = Dialogue()