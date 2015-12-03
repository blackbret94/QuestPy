import json
import random
import time
from Node import Node
from pprint import pprint
"""from enum import Enum

class Motivation(Enum):
	knowledge = 0
	comfort = 1
	reputation = 2
	serenity = 3
	protection = 4
	conquest = 5
	wealth = 6
	ability = 7
	equiptment = 8"""

# Main class, quick script to bounce ideas around, will be drastically re-written later
# settings
class QuestData:
	def __init__(self):
		self.restTime = 2.5;

		# read in config file
		with open('QuestConfig.json') as data_file:
			self.data = json.load(data_file)

		#pprint(data) #print whole set
		# save important rows
		self.names = self.data["names"]
		self.places = self.data["places"]
		self.items = self.data["items"]
		self.enemies = self.data["enemies"]
		self.motivations = ["knowledge","comfort","reputation","serenity","protection","conquest","wealth","ability","equiptment"]

		# stack of data
		self.stack = list()

		#pprint(places)

		# choose initial settings
		#startNPC = random.choice(names)
		#currentNPC = startNPC
		#startLocation = random.choice(places)
		#currentLocation = startLocation
		#motivation = random.choice(motivations)
		#motiveText = "NOTHING YET"
		#fullText = "NOTHING YET"

		

	def chooseMotive(self):
		return random.choice(self.motivations)

	def chooseLocation(self):
		return random.choice(self.places)

	def chooseNPC(self):
		return random.choice(self.names)

	def chooseEnemy(self):
		return random.choice(self.enemies)

	def chooseItem(self):
		return random.choice(self.items)

# instanciate quest data
qd = QuestData()
# create first node
Node(qd.chooseMotive(),qd.chooseNPC(),qd.chooseItem(),True,qd)