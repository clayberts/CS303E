import random
#Class that pretty much just saves the name of the player that we get from the input in titleScreen(). I don't really have too much of a plan to actually use the class for anything in the actual game.
"""explaination of class"""

def titleScreen():
# print() statement 2 points
	print("Welcome to Our Game!")
	player = str(input("Please Enter a Username to Begin: "))
	return player

def tutorialNote():
# This function reads a text file that has the instructions for the game on it.
# 2 Style of Comments (single and multiline) 
# File Reading 15 points
	with open("tutorial.txt", "r") as inFile:

def gameplayLevelOne():
# Formatting for strings 5 points ??
# If statement 5 points

	player = titleScreen()
	skip = '\n'
	print(f"{player}, you wake up in an empty room {skip}aside from an ajar door on the far wall {skip}and a desk with a note ontop of it.")
	choice1 = input("Enter 'note' to read the note; Enter 'door' to cross through the doorway: ")
	if choice1.lower() == "door":
		print("You cross the room and pass through the frame of the door. Your journey begins...")
	elif choice1.lower() == "note"
		print("You pick the note up and examine it. The note looks to be covered in instructions")
#		tutorialNote()
		choice2 = input("Enter 'door' to cross through the doorway: ")
		if choice2.lower == "door":
			print("You cross the room and pass through the frame of the door. Your journey begins...")

