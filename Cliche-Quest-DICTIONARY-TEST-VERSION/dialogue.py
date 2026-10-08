import time
import os
from helper import *
from overworld import *
from room import *


class Dialogue:
  def __init__(self):
    self.messages = []
    self.currentMessage = None
    self.currentIndex = 0
    self.endingEvent = None
    self.completed = False
    self.cutscenes = []
    self.map = []
    
  # adds a message to this Dialogue object's messages list
  def addMessage(self, message):
    self.messages.append(message)

  def addMap(self, area):
    self.map = []
    self.map = area.rooms

  # starts the dialogue sequence
  def start(self):
    print("starting next event")
    self.currentMessage = self.messages[0]
    self.currentIndex = 0
    if isinstance(self.currentMessage, list):
      for i in range(len(self.currentMessage)):
        self.listMessage = self.currentMessage[i]
        #print(i)
        print(self.listMessage)
      input("Press Enter to Continue...")
      os.system("clear")
      self.next()
        
    elif isinstance(self.currentMessage, str):
      print("printing all at once")
      print(self.currentMessage)
    else:
      self.endingEvent = self.currentMessage
      print("Battle event")
      print(self.endingEvent)
      self.endingEvent.start()

  # proceeds to next dialogue message after enter is clicked
  def next(self):
    self.currentIndex = self.currentIndex + 1
    if len(self.messages) > self.currentIndex:
      self.currentMessage = self.messages[self.currentIndex]
      print(self.currentMessage)
    else:
      self.chooseNextRoom(currentRoom)
    if self.currentIndex < len(self.messages)-1 and self.completed:
      self.completed = False
    else:
      if isinstance(self.currentMessage, list):
        self.start()
      elif not isinstance(self.currentMessage, str):
        self.currentMessage.start()
    print("Press Enter to continue...")
    input()
    self.next()

  # adds an event to this Dialogue that is triggered once this dialogue has completed
  def addEvent(self, event):
    self.messages.append(event)


  def addCutscene(self, cutscene):
    self.cutscenes.append(cutscene)
    for i in range(len(cutscene)):
      self.messages.append(cutscene[i])

  def chooseNextRoom(self, currentRoom):
    os.system("clear")
    directions = []
    roomChoice = "none"
    #print(len(self.map))
    #print(len(currentRoom))
    isTopRow = currentRoom[0] == 0
    isBottomRow = currentRoom[0] == len(self.map)-1
    leftEdge = currentRoom[1] == 0
    rightEdge = currentRoom[1] == len(self.map[currentRoom[0]])-1
    
    
    if isinstance(self.map[currentRoom[0] - 1][currentRoom[1]], Room) and not isTopRow:
      directions.append("north")
    if isinstance(self.map[currentRoom[0]][currentRoom[1] + 1], Room) and not rightEdge:
      directions.append("east")
    if isinstance(self.map[currentRoom[0] + 1][currentRoom[1]], Room) and not isBottomRow:
      directions.append("south")
    if isinstance(self.map[currentRoom[0]][currentRoom[1] - 1], Room) and not leftEdge:
      directions.append("west")
      
    roomChoice = askPrompt("Which room?", directions)
    if roomChoice == "North":
      currentRoom[0] = currentRoom[0] - 1
    elif roomChoice == "East":
      currentRoom[1] = currentRoom[1] + 1
    elif roomChoice == "South":
      currentRoom[0] = currentRoom[0] + 1
    elif roomChoice == "West":
      currentRoom[1] = currentRoom[1] - 1

    self.messages = []
    self.processRoom(currentRoom)
    
  
  def processRoom(self, currentRoom):
    self.currentRoomObject = self.map[currentRoom[0]][currentRoom[1]]
    #print(self.currentRoomObject.description)
    if self.currentRoomObject.description != "":
      self.addMessage(self.currentRoomObject.description)
    #print(self.currentRoomObject.description)
    
    input("second press enter to continue")
    self.next()
    

# self.map[][]
# roomRow is horizontal, while roomCol is vertical.
# currentRoom = [1, 2]
# currentRoom[0] = 1 (This is going to give us the current row)
# currentRoom[0] + 1

# list = [a, b, c, d]
# list[2] = c
# list[-1] = d