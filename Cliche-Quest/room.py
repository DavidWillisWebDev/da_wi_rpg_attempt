from helper import *
from character import *
from dialogue import *
from npc import *

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

  def shop(self, inventory):
    self.inventory = []

  #def roomDesc(self, dialogue):
    
    

room1 = Room(141, "This is where you started your quest.")

#room2 = Room()