from helper import *
from character import *
from item import *
from equipment import *
from npc import *


class Shop:

  def __init__(self, items: list = [], character = player):
    self.items = items
    self.character = character

  def addItems(self, item):
    self.items.append(item)
  
  def stock(self):
    item_numbers = list(range(1, len(self.items)+1))
    item_names = []
    for index in range(len(self.items)):
      item_numbers[index] = str(item_numbers[index])
      item_names.append(self.items[index].name)
    print(self.items)
    # display the item they could buy
    # "1 - Potion (15 gold)"
    for index in range(len(self.items)):
      item = self.items[index]
      print(str(index+1) + " - " + item.name + " (" + str(item.price) + ")")

    response = askPrompt("Which items? ", item_names)

    if response == "exit":
      self.leaveShop()
      
    for i in range(len(self.items)):
      if response == i+1 or response == self.items[i].name:
        self.buyItem(self.items[i])


  def buyItem(self, item):
    if isinstance(item, Item):
      self.character.inventory.items.append(item)
    elif isinstance(item, Equipment):
      self.character.inventory.weapons.append(item)


  # def sellItem(self, item):
    
  
  def leaveShop(self):
    gameStatus = "overworld"