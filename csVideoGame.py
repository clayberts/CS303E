import random
#Class that pretty much just saves the name of the player that we get from the input in titleScreen(). I don't really have too much of a plan to actually use the class for anything in the actual game.
class Player:
	#Constructor method for the class
	#Declares default name as John Doe
	def __init__(self, name: str = 'John Doe'):
		self.__name = name
	#Mutator method for class
	def setName (self, name:str):
		self.__name = name
	#Accessor method for class
	def getName(self):
		return self.__name
	#Method to print information
	def __str__(self):
		return "Player's name is {}.format(self.__name)"
def titleScreen():
# print() statement 2 points
	print("Welcome to Our Game!")
	player = str(input("Please Enter a Username to Begin: "))
	return player

def tutorialNote():
# This function reads a text file that has the instructions for the game on it.
# 2 Style of Comments (single and multiline) 
# File Reading 15 points
	with open("tutorial.txt") as inFile:
		return inFile.read()

def gameplayLevelOne():
	# Formatting for strings 5 points ??
	# If statement 5 points

	player = titleScreen()
	playerClass = Player(player) #The Player Class is used within the gameplayLevelOne function here and in the following print statement 2 lines down as playerClass.getName()
	skip = '\n'
	print(f"{playerClass.getName()}, you wake up in an empty room {skip}aside from an ajar door on the far wall {skip}and a desk with a note ontop of it.")
	choice1 = input("Enter 'note' to read the note; Enter 'door' to cross through the doorway: ")
	if choice1.lower() == "door":
		print("You cross the room and pass through the frame of the door. Your journey begins...")
	elif choice1.lower() == "note":
		print("You pick the note up and examine it. The note looks to be covered in instructions")
		print('\n'  + tutorialNote())
		choice2 = input("Enter 'door' to cross through the doorway: ")
		if choice2.lower == "door":
			print("You cross the room and pass through the frame of the door. Your journey begins...")

def rollingDice():
#This function uses the random number generator in order to have the computer roll two dice.
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)
    return diceOne,diceTwo

def comparingRolls(diceOne,diceTwo,dictionaryForRolls,health=100):
#This function uses the recursive function definition and Recursive Function Call. It also uses -= 
#This recursive function in the game helps determine what happens to the player’s health when some obstacle or object causes her/him to get stuck/injured. 
    if diceTwo > diceOne:
        return dictionaryForRolls['Win']
    elif diceTwo < diceOne:
        return dictionaryForRolls['Lose']
    else:
        health -= 5   # -= used to subtract the player’s health percentage by five each time he/she is stuck/injured.
        print(dictionaryForRolls['Tie'])
        print(f"Health level: {health}%")
        diceOne,diceTwo = rollingDice()
        return comparingRolls(diceOne,diceTwo,dictionaryForRolls,health)

def main():
#This function is where we will execute our entire game code.
	gameplayLevelOne()
	print('\n' + "You enter a room that has a dice laying on a table. You approach the dice, compelled to roll it.")
	continuePlay = input("Roll the Dice? One you begin you will be unable to stop until a final outcome has been reached: ")
	dictionaryForRolls = {'Tie':'You are stuck! Losing health fast!','Win':'You are safe!','Lose':'Stuck for too long\nHealth level: 0%...Mission incomplete'}
	diceOne,diceTwo = rollingDice()
	print(comparingRolls(diceOne,diceTwo,dictionaryForRolls,health=100))

    #line 59 below uses a dictionary. It is used as a parameter in the comparingRolls recursive function.
    #lines 59-61 will be right next to each other in the finished game code as shown below. However right now these three lines in main() are just testing to see if the recursive function,dictionary, and print statement work together.

	
main()
