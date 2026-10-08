from helper import *
#from overworld import *


iPrices = {
  "Potion" : 15,
  "Bomb" : 20,
}

class Item:

  def __init__(self, itemType, name, damage = 0, healing = 0):
    self.itemType = itemType
    self.name = name
    self.quantity = 1
    self.damage = damage
    self.healing = healing
    self.price = iPrices[self.name]


potion = Item("healing", "Potion", healing = 10)
bomb = Item("damage", "Bomb", damage = 10)
