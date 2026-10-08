from helper import *


class NPC:
  
  def __init__(self, npcType, name):
    self.npcType = npcType
    self.name = name
    self.npcs = []

  
genericGuy = NPC("generic", "Some Generic Guy")
shopkeeper = NPC("shopkeeper", "Shopkeeper")
uselessGuard = NPC("generic", "This Useless Guard")