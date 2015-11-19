import json
import random
import time
from pprint import pprint
# Main class, quick script to bounce ideas around, will be drastically re-written later
# settings
restTime = 3;

# read in config file
with open('QuestConfig.json') as data_file:
	data = json.load(data_file)

#pprint(data) #print whole set
# save important rows
names = data["names"]
places = data["places"]
items = data["items"]
enemies = data["enemies"]
motivations = ["knowledge","comfort","reputation","serenity","protection","conquest","wealth","ability","equiptment"]
pprint(places)

# choose initial settings
startNPC = random.choice(names)
currentNPC = startNPC
startLocation = random.choice(places)
currentLocation = startLocation
motivation = random.choice(motivations)
motiveText = "NOTHING YET"
fullText = "NOTHING YET"

#print(startNPC)
#print(startLocation)



# chooses a new motivation, takes previous motivation and success of that quest
# future iteration will set a first sentence for the quest text based on the outcome
def chooseMotivation(prevMot,success):
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

# chooses a subject for a motive, takes motive
def chooseSubject(motive):
	if(motive == "knowledge"):
		return random.choice(enemies+items+names+places)

	elif(motive == "comfort"):
		return currentNPC

	elif(motive == "reputation"):
		return currentNPC

	elif(motive == "serenity"):
		return currentNPC

	elif(motive == "protection"):
		return currentNPC
		
	elif(motive == "conquest"):
		return random.choice(enemies)

	elif(motive == "wealth"):
		return random.choice(items)

	elif(motive == "ability"):
		return random.choice(enemies)

	elif(motive == "equiptment"):
		return random.choice(items)


# quest text for the object, takes motivation and quest subject
def chooseText(motive, subject):
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

# choose next motivation
while(True):
	time.sleep(restTime)
	# suc/fail
	suc = random.choice([True,False])

	# create text block
	if(suc):
		fullText = "Good work! Now "
	else:
		fullText = "After failing to " + motiveText + ", "


	# next motive
	motivation = chooseMotivation(motivation,suc)
	motiveText = chooseText(motivation,chooseSubject(motivation))

	# finish text block
	fullText += motiveText

	print(fullText)