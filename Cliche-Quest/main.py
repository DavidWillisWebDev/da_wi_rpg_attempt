# python imports
import time

# our imports
from character import *
from eventNode import *
from dialogue import *
from choices import *
from battle import *
from helper import *
from item import *
from story import *
from overworld import *
from npc import *


# set up the first area

intarough = Area()
intarough.addRoom()
story.addMap(intarough)
story.start()
# player information (variables will be given values later)
playerName = ""

# setup first encounter
#player.battleReport()



