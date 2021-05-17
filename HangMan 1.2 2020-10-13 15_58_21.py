# Hangman Game Ver 1.2
# Ethan Frailey
# 10/13/20
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

#Version 1.2 bring new words + definitions to those words

#imports
import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |    +
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |    +
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   |
 |   |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   |  |
 |   |  |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   | |
 |   | |
 |~-
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    +
 |   | |
 |   | |
 |  ~  ~
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PYTHON", "STRING", "LOOP", "ASCII", "IF", "VARIBLE", "CODE", "RANDOM", "COMPUTER", "GAME")
word=random.choice(WORDS)
wrong = 0
used = []
so_far = " _ "*len(word)


word=random.choice(WORDS)

print("Welcome to HangMan. Good Luck!")

#testing purposes
print(word)



while wrong < MAX_WRONG and so_far != word:
	print(HANGMAN[wrong])
	print()
	print("So far, the word is:",so_far)
	print()
	print("You've used the following letters:", used)
	
	guess = input("Enter your guess: ")
	guess = guess.upper()
	

	while guess in used:
		print("You've already guessed the letter", guess)
		guess = input("Enter your guess: ")
		guess = guess.upper()
		
	used.append(guess)


	if len(guess)>1:
		if guess == word:
			so_far = guess
							
	elif guess in word:
		
		print("Yes!", guess, "is the word!")
		#create a new so_far to include guess
		new = ""
		
		for I in range(len(word)):
			if guess == word[I]:
				new += guess
				
			else:
				new += so_far[I]
				
		so_far = new
		
	else:
		print("Sorry,", guess, "is not in the word.")
		wrong += 1
		
if wrong == MAX_WRONG:
	print(HANGMAN[wrong])
	print("You've been hanged")
	print("So far, the word is", so_far)
else:
	print(HANGMAN[wrong])
	print("You Guessed it right")
	print()
	print("The word was", so_far)
	
#definitions of words
print()
print("The Definition of", word)
print()

if word == "PYTHON":
	print("Is a coding language")
elif word == "STRING":
	print("A string is a line of text in Python")
elif word == "LOOP":
	print("A Loop is something that repeats a line of code in python untill certain conditions are met.")
elif word == "ASCII":
	print("Ascii is a type of art that is made up of symbols instead of colors.")
elif word == "IF":
	print("The if statement if a condition in python that if true will execute the indented code below itself.")
elif word == "VARIBLE":
	print("A varible is a way to store data in all coding languages.")
elif word == "CODE":
	print("Code is the langauge computers understand.")
elif word == "RANDOM":
	print("Random in python will choose a random data value in a list")
elif word == "COMPUTER":
	print("A compueter is a device to store, execute, and process data. It is uselly electronic")
elif word == "GAME":
	print("A game is a source of entertainment")
	
	
print()	
print("Press Enter to Exit")

input()
	
