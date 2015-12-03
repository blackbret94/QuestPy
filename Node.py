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
	def __init__(self,motive,npc,item,suc,questData):
		self.motive = motive
		self.NPC = npc
		self.item = item
		self.suc = suc
		self.questData = questData

		self.run()

	# performs major tasks
	def run(self):
		# create text chunk
		print(self.buildTextBlock())

		# pause
		time.sleep(self.questData.restTime)

		# suc or fail?
		nextSuc = random.choice([True,False])

		# choose next motive
		nextMotive = self.chooseMotivation(self.motive,nextSuc)

		# choose and set new data
		self.chooseNewData(nextMotive,nextSuc)

		# create next node, should pass to questData list
		nextNode = Node(nextMotive,self.NPC,self.item,nextSuc,self.questData)

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
			questData = self.questData
			return random.choice(questData.enemies+questData.items+questData.names+questData.places)

		elif(motive == "comfort"):
			return self.NPC

		elif(motive == "reputation"):
			return self.NPC

		elif(motive == "serenity"):
			return self.NPC

		elif(motive == "protection"):
			return self.NPC
			
		elif(motive == "conquest"):
			return random.choice(self.questData.enemies)

		elif(motive == "wealth"):
			return random.choice(self.questData.items)

		elif(motive == "ability"):
			return random.choice(self.questData.enemies)

		elif(motive == "equiptment"):
			return random.choice(self.questData.items)


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
	# has a chance to change items, characters, and places as well
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

	# chances data based on the new motive and whether it was a pass or fail
	def chooseNewData(self,motive,success):
		# if fail pop
		if(not success):
			self.popFromStack()
			return

		# else choose new data
		if(motive == "knowledge"):
			self.changeData(0,.5,.5)

		elif(motive == "comfort"):
			self.changeData(0,0,0)

		elif(motive == "reputation"):
			self.changeData(0,0,0)

		elif(motive == "serenity"):
			self.changeData(0,1,0)

		elif(motive == "protection"):
			self.changeData(0,0,.25)

		elif(motive == "conquest"):
			self.changeData(.5,.25,.5)

		elif(motive == "wealth"):
			self.changeData(0,1,.75)

		elif(motive == "ability"):
			self.changeData(0,.5,.75)

		elif(motive == "equiptment"):
			self.changeData(0,.75,.25)

	# changes some values and pushes the old state to the stack.  All param are values between 0 and 1, with 1 meaning always 0 being never
	def changeData(self,npc,item,place):
		# if anything is to change, push old state
		if(npc > 0 or item > 0 or place > 0):
			self.pushToStack()

		if(random.random() < npc):
			# change NPC
			self.npc = random.choice(questData.names)
		if(random.random() < item):
			# change item
			self.npc = random.choice(questData.items)

		if (random.random() < place):
			# change place
			self.npc = random.choice(questData.places)

	# pushes current set of info to the parent stack
	def pushToStack(self):
		newDict = dict(NPC=self.NPC,item=self.item)
		self.questData.append(newDict)

	# pops the current set of info from the parent stack
	def popFromStack(self):
		if(len(self.questData.stack) > 0):
			poppedDict = self.questData.stack.pop()
			self.NPC = poppedDict.NPC
			self.item = poppedDict.item