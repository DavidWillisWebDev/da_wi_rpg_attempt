# python imports
import time

# our imports
from character import *
from dialogue import *
from choices import *
from battle import *
from helper import *
from item import *
from overworld import *
from room import *

# introductory dialogue
# (some of the messages are commented out to skip them for now)
story = Dialogue()
intro = ["The Princess, Damsel-In-Distress, has been kidnapped by the Evil King Bad Guy!\n", "It's definitely not because the guards were written to be as useless as possible!\n", "Now, it's up to you, Conveniently-Chosen Hero, to save Princess Damsel-In-Distress!\n", "Oh, right. Take this sword. Every hero uses a sword, right?\n", "By the way, here's a slime for you to fight. We're legally required to have a battle tutorial.\n"]

#intro = story
encounter = Battle(story)
encounter.addEnemy(slime)
#encounter.addEnemy(slime)
encounter.addPartyMember(player)
#encounter.addPartyMember(player2)
story.addEvent(intro)
gameStatus = "cutscene"


#playerName = input("By the way, what is your name?\n")
#story.addMessage("Nice to meet you, " + playerName + ".")


story.addEvent(encounter)
cutscene2 = ["Congratulations on your tutorial.\n", "Well, then, continue on with your quest to save Princess Damsel-In-Distress.\n", "I almost forgot to mention. You're in the town of Intarough.\n"]
story.addCutscene(cutscene2)

#story.makeRoom(intarough)
gameStatus = "overworld"

# Joke for later:
# unknownCutscene = ["Then again, video game guards are always stupid. Even doorknobs are smarter than them.\n"]