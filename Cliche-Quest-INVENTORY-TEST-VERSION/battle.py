from helper import *
from character import *
from item import *
from spell import *
import random
import os
# from room import *


# the options each player can choose during their turn
battleOptions = ["Fight", "Abilities", "Defend", "Items", "Escape"]


"""
Battling should loosely follow this pattern:

1 - Ask the user for their choices (from every party member)
2 - Resolve the user's choices (i.e. deal damage, use abilities, use items, handle victory/loss, etc.)
3 - Select the enemy's choices
4 - Resolve the enemy's choices 
5 - Repeat

Once the battle has finished, call a function that starts the next event (either from winning or losing).
"""


class Battle:

  # for now Battle objects are created with an empty constructor
  # and enemies are added to the battle manually using addEnemy
  def __init__(self):
    self.enemies = []
    self.party = []
    self.turnOrder = []
    self.completed = False
    

  # adds an enemy to this Battle
  def addEnemy(self, enemy):
    enemyObject = Character(enemy.health, enemy.abilities, enemy.strength, enemy.defense, enemy.speed, enemy.enemyType, enemy.name, enemy.level, enemy.attackDamage)
    self.enemies.append(enemyObject)

  def addPartyMember(self, player):
    self.party.append(player)

  # starts the battle by asking the user for their first move
  def start(self):
    print("battle started")
    gameStatus = "battle"
    self.determineTurnOrder()
    self.prompt()
    #self.switchTurn()

  # asks the user for their next move, and performs that action
  def prompt(self):
    os.system("clear")
    #print(self.turnOrder)
    #for i in range(len(self.turnOrder)):
      #print(self.turnOrder[i].name)
    # display player and enemy stats
    for i in range(len(self.party)):
      
      self.party[i].battleReport()
      self.party[i].currentTurn = True
      #print("player defense: " + str(self.party[i].defense))
    for i in range(len(self.enemies)):
      self.enemies[i].battleReport()
      # check who won


    enemiesWon = False
    partyWon = True
    # Check to see if the character is dead
    # If the character is of enemyType = player, then the player is unable to move.
    # Otherwise, remove the character from self.enemies.
    enemyListLength = len(self.enemies)
    i = 0
    while i < enemyListLength:
      if self.enemies[i].health > 0:
        partyWon = False
      if self.party[i].health < 1:
        pass
        # print("You lose.")
        # enemiesWon = False
      if self.enemies[i].health < 1:
        self.turnOrder.remove(self.enemies[i])
        self.enemies.remove(self.enemies[i])
        enemyListLength -= 1
      i += 1
      
    if len(self.enemies) == 0:
      print("You win.")
      partyWon = True
      self.complete = True
      return

    if len(self.party) == 0:
      print("You lose.")
      enemiesWon = True
      
    k = 0
    self.turnLength = len(self.turnOrder)
    while k < self.turnLength:
      os.system("clear")
      currentPerson = self.turnOrder[k]
      print(str(currentPerson.name) + "'s turn.")
      if currentPerson.enemyType == "player":
        currentPlayer = currentPerson
        if partyWon == False and currentPerson.health != 0:
          for i in range(len(self.party)):
        
            self.party[i].battleReport()
            self.party[i].currentTurn = True
          for i in range(len(self.enemies)):
            self.enemies[i].battleReport()
        # ask the user what they want to do, and resolve their choice
          response = askPrompt("What do you want to do?", battleOptions)
          if response == "Fight" or response == battleShortcuts[0]:
            self.promptFight(currentPlayer)
            input("Press Enter to Continue...")
          elif response == "Abilities" or response == battleShortcuts[1]:
            self.promptAbilities(currentPlayer)
            input("Press Enter to Continue...")
          elif response == "Defend" or response == battleShortcuts[2]:
            self.defend(currentPlayer)
            input("Press Enter to Continue...")
          elif response == "Items" or response == battleShortcuts[3]:
            self.promptItems()
            input("Press Enter to Continue...")
          elif response == "Escape" or response == battleShortcuts[4]:
            self.escape()
            input("Press Enter to Continue...")
          else:
            print("ERROR - unexpected response in Battle.prompt(): " + str(response))
        else:
          self.completed = True
      else:
        self.enemyTurn(currentPerson)

      k += 1
    for i in range(len(self.party)):
      currentPlayer.resetToBaseStats()
    
      print(currentPerson.tempStats)
      if len(currentPerson.tempStats) > 0:
        for j in range(len(currentPlayer.tempStats)):
          if currentPerson.tempStats[j] == "defense boost":
            currentPerson.defense += 500
      print("player defense: " + str(currentPlayer.defense))
      currentPerson.currentTurn = False
    for i in range(len(self.enemies)):
      currentEnemy = self.enemies[i]
      if currentEnemy.health > 0:
        #self.switchTurn()
        input("Press Enter to Continue...")
    #self.switchTurn()
    self.prompt()
      
    


  # when the "Fight" command is chosen, promptFight asks the user
  # who they want to attack
  def promptFight(self, currentPlayer):

    # convert the enemies list (list of strings) into enemy_numbers list (list of ints)
    # i.e. enemies might be ["Slime", "Slime", "Rat"]
    # and enemy_numbers would be [1, 2, 3]
    # since an enemy name (i.e. "Slime") might appear in the enemies more than once,
    # we use the number associated with each enemy to make it clear which one they are targeting
    
    enemy_numbers = list(range(1, len(self.enemies)+1))
    for index in range(len(enemy_numbers)):
      enemy_numbers[index] = str(enemy_numbers[index])
    
    # display the enemies they could attack, in the format
    # "1 - Slime"
    for index in range(len(self.enemies)):
      enemy = self.enemies[index]
      print(str(index+1) + " - " + enemy.name)

    # ask them which enemy they want to attack (they target an enemy using the enemies' numbers)
    response = askPrompt("Which one? ", enemy_numbers)
    
    # attack that enemy
    enemy = self.enemies[int(response)-1]
    currentPlayer.damageChar(currentPlayer, enemy)
    print("You dealt " + str(enemy.attackDamage) + " damage to " + enemy.name + ".")
    enemy.health = enemy.health - enemy.attackDamage
    print(enemy.health)
    if enemy.health < 1:
      self.turnOrder.remove(enemy)
      self.turnLength -= 1
      self.enemies.remove(enemy)

  # when the "Abilities" command is chosen, promptAbilities asks the user
  # what ability they want to use (and if necessary) who they want to target
  # with that ability
  # unlike promptFight, we assume that no ability name will show up in an abilities list twice, meaning that we can pick an ability by its name rather than its number
  def promptAbilities(self, currentPlayer):

      
    # display their abilities
    abilityNames = []
    for index in range(len(currentPlayer.abilities)):
      ability = currentPlayer.abilities[index].name
      #print(ability)
      abilityNames.append(ability)
      
    # convert the ability list (list of strings) into ability_numbers list (list of ints)
    # i.e. abilities might be ["fire", "heal", "freeze"]
    # and ability_numbers would be [1, 2, 3]
    # we use the number associated with each enemy to make the battle system go by quicker
    
    ability_numbers = list(range(1, len(currentPlayer.abilities)+1))
    for index in range(len(ability_numbers)):
      ability_numbers[index] = str(ability_numbers[index])
    
    # display the abilities they could use, in the format
    # "1 - Fire"
    for index in range(len(currentPlayer.abilities)):
      ability = currentPlayer.abilities[index]
      print(str(index+1) + " - " + ability.name)

    # ask them which ability they want to use
    response = askPrompt("Which one? ", ability_numbers)
    
    # use that ability
    #print(response)
    print("You cast " + currentPlayer.abilities[int(response) - 1].name + ".")
    currentPlayer.castSpell(self, int(response)-1)
    

  # performs the defend action when the "Defend" command is chosen
    # selecting this will reduce damage taken
  def defend(self, currentPlayer):

      
    if currentPlayer.currentTurn == True:
      #player.defense = currentPlayer.defense + 500
      currentPlayer.tempStats.append("defense boost")
      print("You block the enemy's attack.")

      
  # when the "Items" command is chosen, promptItems asks the user
  # what item they want to use (and if necessary) who they want to target
  # with that item
  # NOTE: Multiple copies of the same item (i.e. two potions) will be stacked (i.e. Potion x2) at a later time.
  def promptItems(self):


    for i in range(len(self.party)):
      player = self.party[i]
      
    # build a list of item names from the list of item objects
    # also print the item names for the user to choose from
    item_names = []
    for index in range(len(player.inventory.items)):
      item = player.inventory.items[index].name
      print(item)
      item_names.append(item)
      
    # convert the item list (list of strings) into item_numbers list (list of ints)
    # i.e. abilities might be ["fire", "heal", "freeze"]
    # and ability_numbers would be [1, 2, 3]
    # we use the number associated with each enemy to make the battle system go by quicker
    
    item_numbers = list(range(1, len(player.inventory.items)+1))
    for index in range(len(item_numbers)):
      item_numbers[index] = str(item_numbers[index])
    
    # display the abilities they could use, in the format
    # "1 - Fire"
    for index in range(len(player.abilities)):
      item = player.inventory.items[index]
      print(str(index+1) + " - " + item.name)

    # ask them which ability they want to use
    response = askPrompt("Which one? ", item_numbers)
    
    # use that ability
    #print(response)
    print("You used " + player.inventory.items[int(response)-1].name + ".")
    player.useItem(self, int(response)-1)
    
    #item.quantity = item.quantity - 1

  # performs the escape action when the "Escape" command is chosen
  def escape(self):
    print("You attempted to escape this pointless battle.")
    #return

  def enemyTurn(self, currentEnemy):
    os.system("clear")
    currentEnemy.currentTurn = True
    print(str(currentEnemy.name) + "'s turn.")
    
    for i in range(len(self.party)):
      currentPlayer = self.party[i]
      currentPlayer.battleReport()
      currentPlayer.currentTurn = True
      
    currentEnemy.battleReport()
      

    if random.randint(1,2) == 1:
      currentEnemy.decision = "attack"
    else:
      currentEnemy.decision = "defend"
      
    
    if currentEnemy.decision == "attack":
      target = random.choice(self.party)
      print(currentEnemy.name + " attacked " + target.name + ".")
      currentEnemy.damageChar(currentEnemy, target)
      print(currentEnemy.name + " dealt " + str(currentEnemy.damage) + " damage to " + target.name + ".")
      target.health = target.health - currentEnemy.damage
      
      
    if currentEnemy.decision == "defend":
      if currentEnemy.currentTurn == True:
        currentEnemy.tempStats.append("defense boost")
        print(currentEnemy.name + " blocked " + currentPlayer.name + "'s attack.")
        if "defense boost" in currentEnemy.tempStats:
          currentEnemy.tempStats.remove("defense boost")
          currentEnemy.resetToBaseStats()
    
    for i in range(len(self.party)):
      currentPlayer = self.party[i]
      if "defense boost" in currentPlayer.tempStats:
        currentPlayer.tempStats.remove("defense boost")
        currentPlayer.resetToBaseStats()
    input("Press Enter to Continue...")
    #self.switchTurn()



  def determineTurnOrder(self):
    for i in range(len(self.party)):
      player = self.party[i]
      self.turnOrder.append(player)
    for j in range(len(self.enemies)):
      enemy = self.enemies[j]
      self.turnOrder.append(enemy)
    self.turnOrder.sort(key = lambda x: x.speed, reverse = True)
    

  """
  def switchTurn(self):
    for i in range(len(self.turnOrder)):
      char = self.turnOrder[i]
      
      if char.enemyType == "player":
        self.prompt(char)
      else:
        self.enemyTurn(char)
        """

# self.damage = self.attackDamage * int(attacker.strength / defender.defense)
