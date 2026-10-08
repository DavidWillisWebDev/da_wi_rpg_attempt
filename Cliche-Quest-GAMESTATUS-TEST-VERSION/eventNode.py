# NOTE TO COACH: this eventNode class is never used!
# currently, this class is more or less serving as a template for the Dialogue, Battle, and Choice classes
# eventually, this could be a good opportunity to teach inheritance (and treat eventNode as the parent class)!

"""
from helper import *

# every eventNode will contain a list which is a sequence of events
# each event can be dialogue, battle, or a branching choice

class eventNode:
  def __init__(self, sequence):
    self.sequence = sequence
    self.currentEvent = None
    self.currentIndex = 0;
  
  def start(self):
    self.currentEvent = self.sequence[0]
    self.currentIndex = 1
    self.currentEvent.start()

  def next(self):
    self.currentIndex = self.currentIndex + 1
    self.currentEvent = self.sequence[self.currentIndex]
    self.currentEvent.start()
"""