import json
import random
import time
from pprint import pprint
# Main class

# read in config file
with open('QuestConfig.json') as data_file:
	data = json.load(data_file)

#pprint(data) #print whole set
# save important rows
names = data["names"]
places = data["places"]
motivations = ["knowledge","comfort","reputation","serenity","protection","conquest","wealth","ability","equiptment"]
pprint(places)

# choose initial settings
startNPC = random.choice(names)
currentNPC = startNPC
startLocation = random.choice(places)
currentLocation = startLocation
motivation = random.choice(motivations)

print(startNPC)
print(startLocation)



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

# quest text for the object, takes motivation
#def chooseText(motive):
	#something

# choose next motivation
while(True):
	print(motivation)
	time.sleep(1)
	motivation = chooseMotivation(motivation,random.choice([True,False]))