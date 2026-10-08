from helper import *
from item import *
from equipment import *
from spell import *
from inventory import *
import random
import time

# list of party members (Character objects)
# not supported yet; for now we only use the player Character object
party = []



class Character:

  # character constructor
  def __init__(self, health, abilities, strength, defense, speed, enemyType, name, level, attackDamage):
    self.baseHealth = health
    self.health = self.baseHealth
    self.maxHealth = health
    self.abilities = abilities
    self.baseStrength = strength
    self.baseDefense = defense
    self.baseSpeed = speed
    self.resetToBaseStats()
    self.enemyType = enemyType
    self.name = name
    self.level = level
    self.inventory = Inventory([bomb, potion], [basicSword], [basicShield], [basicArmor], [])
    self.attackDamage = attackDamage
    self.currentTurn = False
    self.tempStats = [] # temporary (per battle/# of turns)
    self.money = 0

    # newly created Character objects of type "player" are added to party
    if enemyType == "player":
      party.append(self)
      
      
  def resetToBaseStats(self):
    
    self.strength = self.baseStrength
    self.defense = self.baseDefense
    self.speed = self.baseSpeed
    
  # allows this Character to learn a new Ability
  def addAbility(self, ability):
    self.abilities.append(ability)
    
  # check if this character knows the ability abilityName
  # i.e. dragon.checkAbilities("Fireball")
  def checkAbilities(self, abilityName):
    return abilityName in self.abilities

  # prints a representation of this Character's current battle status
  # examples:
  # "Fighter: 162 / 280"
  # "Red Slime: 54 / 100"
  def battleReport(self):
    print(self.name + ": " + str(self.health) + " / " + str(self.maxHealth))
    

  # used to determine an enemy (not player) character's battle choice during their turn
  def enemyChoice(self, abilityList):
    # chooses between attack, abilities, and defend
    return random.choice(abilityList)
    

  def damageChar(self, attacker, defender):
    if attacker.strength >= defender.defense:
      self.damage = self.attackDamage * int(attacker.strength / defender.defense)
    else:
      self.damage = int(self.attackDamage * attacker.strength / defender.defense)

  def castSpell(self, battle, abilityIndex):
    
    spell = self.abilities[abilityIndex]
    #print(spell)
    
    if spell.spellType == "damage":
      #print(battle.enemies)
      for index in range(len(battle.enemies)):
        enemy = battle.enemies[index]
        print("You dealt " + str(spell.damage) + " damage to " + enemy.name + ".")
        enemy.health -= spell.damage
        
    elif spell.spellType == "healing":
      self.healing(spell.healing)

  
  def useItem(self, battle, itemIndex):
    
    item = self.inventory.items[itemIndex]
    #print(item)
    
    if item.itemType == "damage":
      #print(battle.enemies)
      for index in range(len(battle.enemies)):
        enemy = battle.enemies[index]
        print("You dealt " + str(item.damage) + " damage to " + enemy.name + ".")
        enemy.health -= item.damage
      
        
    elif item.itemType == "healing":
      self.healing(item.healing)
      
    
    
  def healing(self, amount):
    
    if self.health + amount >= self.maxHealth:
      self.health = self.maxHealth
      print("You healed " + self.name + " to full health.")
    else:
      self.health += amount
      print("You healed " + str(amount) + " health to " + self.name + ".")


  def checkInventory(self):
    print(self.inventory)
    playerChoice = ""
    while playerChoice != "yes": #and playerChoice != "y":
      playerChoice = input("Ready to get back to the game?")

  
# create player characters (party)
player = Character(500, [Fire, Heal], 3, 30, 50, "player", "Mr. Dave", 1, 3)
player2 = Character(500, [UnknownSpell], 10, 15, 10, "player", "other person", 1, 10)
player3 = Character(450, [], 10, 15, 40, "player", "", 1, 10)
player4 = Character(500, [], 10, 15, 50, "player", "", 1, 10)

# create enemies
slime = Character(1, ["Fire"], 5, 5, 20, "slime", "Slime", 1, 50)
guard = Character(500, [], 10, 10, 5, "guard", "Guard", 1, 10)
ratBoss = Character(500, [], 100, 90, 40, "rat boss", "Rat Boss", 5, 10)
slimeBoss = Character(1500, ["Fire"], 5, 5, 500, "slime boss", "That Tutorial Slime from Earlier", 1, 50)
guardBoss = Character(1500, [], 10, 10, 500, "guard boss", "That Idiot Guard From Earlier That is Dumber Than a Doorknob", 1, 10)
evilKing = Character(65000, ["Annihilation"], 1200, 1300, 2500, "final boss", "Evil King Bad Guy", 75, 900)

# character parameters (health, abilities, strength, defense, speed, enemyType, name, level, attackDamage)