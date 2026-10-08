from helper import *
#from overworld import *

# NOTE: the Spell class / Spell objects will mostly be handled through functions outside of the class ... check out the examples below!

# NOTE: I am not quite sure how the Spell class / object will have access to the player/party/battle/item information ... I leave that mystery up to yall! :)

class Spell:

  def __init__(self, name, spellType, damage = 0, healing = 0):
    self.name = name
    self.spellType = spellType
    self.damage = damage
    self.healing = healing
    #self.castSpell = castSpell

  

#Fire = Spell("Fire", "damage", castFire)
Fire = Spell("Fire", "damage", damage = 10)
#Fireball.castSpell()
Heal = Spell("Heal", "healing", healing = 10)
#Heal.castSpell()
UnknownSpell = Spell("Unknown", "damage", damage = 50)