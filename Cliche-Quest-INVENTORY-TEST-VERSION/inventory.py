from helper import *


class Inventory:

  def __init__(self, items: list = [], weapons : list = [], subweapons : list = [], armor : list = [], keyItems : list = []):
    self.items = items
    self.weapons = weapons
    self.subweapons = subweapons
    self.armor = armor
    self.keyItems = keyItems