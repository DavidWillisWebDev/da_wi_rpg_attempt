from helper import *
#from overworld import *

ePrices = {
  "Obligatory Sword" : 0,
  "Obligatory Shield" : 0,
  "Armor That Definitely Will Not Be Replaced With Something Better" : 0,
  "A Brand New Sword" : 25,
  "Definitely Not Overpriced Garbage" : 999999999
}

class Equipment:

  def __init__(self, equipmentType, name):
    self.equipmentType = equipmentType
    self.name = name
    self.quantity = 1
    self.price = ePrices[self.name]

basicSword = Equipment("weapon", "Obligatory Sword")
basicShield = Equipment("shield", "Obligatory Shield")
basicArmor = Equipment("armor", "Armor That Definitely Will Not Be Replaced With Something Better")
newSword = Equipment("weapon", "A Brand New Sword")
trashSword = Equipment("weapon", "Definitely Not Overpriced Garbage")