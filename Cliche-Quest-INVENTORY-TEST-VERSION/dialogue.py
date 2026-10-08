import time
import os
from helper import *
# from overworld import *
from room import *


class Dialogue:
  def __init__(self):
    self.messages = []
    self.currentMessage = None
    self.currentIndex = 0
    self.endingEvent = None
    self.completed = False
    self.cutscenes = []
    
  # adds a message to this Dialogue object's messages list
  def addMessage(self, message):
    self.messages.append(message)

  
  # starts the dialogue sequence
  def start(self):
    gameStatus = "cutscene"
    #print("starting next event")
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
      if isinstance(self.currentMessage, str):
        os.system("clear")
        print(self.currentMessage)
        #print("Press Enter to continue")
        #input()
    if self.currentIndex < len(self.messages)-1 and self.completed:
      self.completed = False
    else:
      if isinstance(self.currentMessage, list):
        #self.start()
        for k in range(len(self.currentMessage)):
          os.system("clear")
          print(self.currentMessage[i])
          #print("Press Enter to continue")
          #input()
      elif not isinstance(self.currentMessage, str):
        self.currentMessage.start()
      if self.currentIndex == len(self.messages)-1:
        self.completed = True
    print("Press Enter to continue...")
    input()
    if self.completed == True:
      chooseNextRoom(currentRoom, currentArea)
    self.next()

  # adds an event to this Dialogue that is triggered once this dialogue has completed
  def addEvent(self, event):
    self.messages.append(event)


  def addCutscene(self, cutscene):
    self.cutscenes.append(cutscene)
    for i in range(len(cutscene)):
      self.messages.append(cutscene[i])
    
    
    

# self.map[][]
# roomRow is horizontal, while roomCol is vertical.
# currentRoom = [1, 2]
# currentRoom[0] = 1 (This is going to give us the current row)
# currentRoom[0] + 1

# list = [a, b, c, d]
# list[2] = c
# list[-1] = d