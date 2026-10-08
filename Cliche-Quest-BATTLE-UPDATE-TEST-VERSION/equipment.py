from helper import *
#from overworld import *

ePrices = {
  "a brand new sword" : 25,
  "definitely not overpriced garbage" : 999999999
}

class Equipment:

  def __init__(self, equipmentType, name):
    self.equipmentType = equipmentType
    self.name = name
    self.quantity = 1
    self.price = ePrices.get()

