from helper import *
from dialogue import *

class Choice:
  
  def __init__(self):
    self.prompt = ""
    self.answers = {}
    # self.dialogue = dialogue
    
  # sets up a prompt for the player
  def setPrompt(self, promptText):
    self.prompt = promptText

  # registers the player's answer
  def registerAnswer(self, answer, result):
    self.answers[answer] = result

  # ask the user what choice they want to make from possible answers
  def askChoice(self):
    response = askPrompt(self.prompt, list(self.answers.keys()))
    self.answers[response].start()

  def start(self):
    self.setPrompt()

# EXAMPLE ANSWERS DICTIONARY
# self.answers = {}
# self.answers["yes"] = acceptQuestNode
# self.answers["no"] = rejectQuestNode
