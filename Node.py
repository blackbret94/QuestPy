""" Represents a node in the quest """
import random
import time

class Node:
	 # blank constructor
	def __init__(self):
		self.motive = "null"
		self.NPC = "NO ONE"
		self.item = "NOTHING"

	# constructor with param
	def __init__(self,motive,npc,item,suc,questPy):
		self.motive = motive
		self.NPC = npc
		self.item = item
		self.suc = suc
		self.questPy = questPy

		self.run()

	# performs major tasks
	def run(self):
		# create text chunk
		print(self.buildTextBlock())

		# pause
		time.sleep(self.questPy.restTime)

		# suc or fail?
		nextSuc = random.choice([True,False])

		# choose next motive
		nextMotive = self.chooseMotivation(self.motive,nextSuc)

		# choose next NPC

		# choose next item

		# create next node, should pass to questPy list
		nextNode = Node(nextMotive,self.NPC,self.item,nextSuc,self.questPy)

	# creates a text block
	def buildTextBlock(self):
		# next motive
		motiveText = self.chooseText(self.motive,self.chooseSubject(self.motive))

		if(self.suc):
			fullText = "Good work! Now "
		else:
			fullText = "After failing to " + motiveText + ", "

		# finish text block
		fullText += motiveText

		return fullText



	# chooses a subject for a motive, takes motive
	def chooseSubject(self,motive):
		if(motive == "knowledge"):
			questPy = self.questPy
			return random.choice(questPy.enemies+questPy.items+questPy.names+questPy.places)

		elif(motive == "comfort"):
			return self.NPC

		elif(motive == "reputation"):
			return self.NPC

		elif(motive == "serenity"):
			return self.NPC

		elif(motive == "protection"):
			return self.NPC
			
		elif(motive == "conquest"):
			return random.choice(self.questPy.enemies)

		elif(motive == "wealth"):
			return random.choice(self.questPy.items)

		elif(motive == "ability"):
			return random.choice(self.questPy.enemies)

		elif(motive == "equiptment"):
			return random.choice(self.questPy.items)


	# quest text for the object, takes motivation and quest subject
	def chooseText(self,motive, subject):
		txt = ""
		if(motive == "knowledge"):
			txt += "learn about "

		elif(motive == "comfort"):
			txt += "comfort "

		elif(motive == "reputation"):
			txt += "establish your reputation for "

		elif(motive == "serenity"):
			txt += "bring peace to "

		elif(motive == "protection"):
			txt += "protect "
			
		elif(motive == "conquest"):
			txt += "defeat "

		elif(motive == "wealth"):
			txt += "gather "

		elif(motive == "ability"):
			txt += "learn the ability to "

		elif(motive == "equiptment"):
			txt += "use "

		# mention subject
		txt += subject

		# return
		return txt

	# chooses a new motivation, takes previous motivation and success of that quest
	# future iteration will set a first sentence for the quest text based on the outcome
	def chooseMotivation(self,prevMot,success):
		if(prevMot == "knowledge"):
			if (success):
				return random.choice(["knowledge","wealth","equiptment","conquest"])
			else:
				return random.choice(["knowledge","reputation"])

		elif(prevMot == "comfort"):
			if (success):
				return random.choice(["serenity","knowledge"])
			else:
				return random.choice(["reputation"])

		elif(prevMot == "reputation"):
			if (success):
				return random.choice(["conquest","wealth","equiptment","ability"])
			else:
				return random.choice(["protection","equiptment"])

		elif(prevMot == "serenity"):
			if (success):
				return random.choice(["protection","wealth","comfort"])
			else:
				return random.choice(["reputation"])

		elif(prevMot == "protection"):
			if (success):
				return random.choice(["comfort","conquest","ability","knowledge"])
			else:
				return random.choice(["reputation","reputation"])

		elif(prevMot == "conquest"):
			if (success):
				return random.choice(["wealth","equiptment","ability","serenity"])
			else:
				return random.choice(["protection","reputation","knowledge"])

		elif(prevMot == "wealth"):
			if (success):
				return random.choice(["comfort","serenity","equiptment"])
			else:
				return random.choice(["protection","reputation","knowledge"])

		elif(prevMot == "ability"):
			if (success):
				return random.choice(["reputation","conquest","equiptment","wealth"])
			else:
				return random.choice(["knowledge","reputation"])

		elif(prevMot == "equiptment"):
			if (success):
				return random.choice(["conquest","protection","ability"])
			else:
				return random.choice(["knowledge","reputation"])