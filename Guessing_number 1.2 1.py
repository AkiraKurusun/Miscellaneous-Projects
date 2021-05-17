#Ethan Frailey
#9/29/20 - cont 10/1/20
#Guess my number ver 1.2

#Ver 1.2 Adds Diffuculty Selection

#Default Varible
lifes = 3
diff = 1

cheat = 124

win = False

print("~Welcome to Guess that Number~")

#diffuculty selection
useransr = input("~~What diffulculty do you want? (Easy, Medium, or Hard)~~ ")

if useransr ==  useransr.startswith("E") or useransr.startswith("e"):
	maxnumber = 11
	lives = 3
	diff = 1
	pass
	
elif useransr == useransr.startswith("M") or useransr.startswith("m"):
	maxnumber = 51
	lives = 6
	diff = 2
	pass
	
elif useransr == useransr.startswith("H") or useransr.startswith("h"):
	maxnumber = 101
	lives = 9
	diff = 3
	pass
	
else:
	print("No known diffuculty detected. Setting to Easy")
	maxnumber = 11
	lives = 3
	diff = 1
	pass
	
#Importing Random Number
import random
theNumber = random.randint (1, int(maxnumber))

#For testing purposes below
#print(theNumber)

 #Dialoge/Instrustions
print("-Ok, the goal is to guess my number")
print(str.format("--The numbers will only be 1 - {}", str(maxnumber - 1)))
print(str.format("---You will have {} lives to get it right", str(lives)))

#guess #1 Diff - 1
if diff == 1:
	if win == False:
		print(str.format("lives: {}", lives))
		guess1 = input(str.format("Pick a number between 1-{}: ", str(maxnumber - 1)))
		
		#cheat statement
		if int(guess1) == cheat:
			win = "Cheat"
			pass
		elif int(guess1) == theNumber:
			win = True
			pass
		elif int(guess1) > theNumber and int(guess1) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess1) < theNumber:
			print("Guess higher")
			pass
		elif int(guess1) > maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#guess #2 diff - 1

	if win == False:
	
		print(str.format("lives: {}", int(lives) - 1))
		guess2 = input("Pick another number ")
		
	#cheat statement
		if int(guess2) == cheat:
			win = "Cheat"
			pass
		elif int(guess2) == theNumber:
			win = True
			pass
		elif int(guess2) > theNumber and int(guess2) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess2) < theNumber:
			print("Guess higher")
			pass
		elif int(guess2) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#guess #3 diff - 1

	if win == False:
	
		print(str.format("lives: {}", int(lives) - 2))
		guess3 = input("One more chance, pick another ")
		
	#cheat statement
		if int(guess3) == cheat:
			win = "Cheat"
			pass
		elif int(guess3) == theNumber:
			win = True
			pass
		if int(guess3) == theNumber:
			win = True
		elif int(guess3) > theNumber and int(guess3) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess3) < theNumber:
			print("Guess higher")
			pass
		elif int(guess3) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
elif diff == 2:

#Guess #1 Diff - 2

	if win == False:
		
		print(str.format("lives: {}", lives))
		guess1 = input(str.format("Pick a number between 1-{}: ", str(maxnumber - 1)))
	
	#cheat statement
		if int(guess1) == cheat:
			win = "Cheat"
			pass
			
		elif int(guess1) == theNumber:
			win = True
			pass
		elif int(guess1) > theNumber and int(guess1) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess1) < theNumber:
			print("Guess higher")
			pass
		elif int(guess1) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
		
#Guess #2 Diff - 2
	if win == False:
		
		print(str.format("lives: {}", lives - 1))
		guess2 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess2) == cheat:
			win = "Cheat"
			pass
		elif int(guess2) == theNumber:
			win = True
			pass
		elif int(guess2) > theNumber and int(guess2) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess2) < theNumber:
			print("Guess higher")
			pass
		elif int(guess2) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#Guess #3 Diff - 2
	if win == False:
		print(str.format("lives: {}", lives -2))
		guess3 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess3) == cheat:
			win = "Cheat"
			pass
		elif int(guess3) == theNumber:
			win = True
			pass
		elif int(guess3) > theNumber and int(guess3) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess3) < theNumber:
			print("Guess higher")
			pass
		elif int(guess3) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#Guess #4 Diff - 2
	if win == False:
		print(str.format("lives: {}", lives - 3))
		guess4 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess4) == cheat:
			win = "Cheat"
			pass
		elif int(guess4) == theNumber:
			win = True
			pass
		elif int(guess4) > theNumber and int(guess4) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess4) < theNumber:
			print("Guess higher")
			pass
		elif int(guess4) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#Guess #5 Diff - 2
	if win == False:
		print(str.format("lives: {}", lives - 4))
		guess5 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess5) == cheat:
			win = "Cheat"
			pass
		elif int(guess5) == theNumber:
			win = True
			pass
		elif int(guess5) > theNumber and int(guess5) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess5) < theNumber:
			print("Guess higher")
			pass
		elif int(guess5) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
		
#Guess #6 Diff - 2
	if win == False:
		print(str.format("lives: {}", lives - 5))
		guess6 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess6) == cheat:
			win = "Cheat"
			pass
		elif int(guess6) == theNumber:
			win = True
			pass
		elif int(guess6) > theNumber and int(guess6) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess6) < theNumber:
			print("Guess higher")
			pass
		elif int(guess6) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("You broke it?")
			pass
#end of Diff - 2

#guess 1 Diff - 3
elif diff == 3:
	if win == False:
		
		print(str.format("lives: {}", lives))
		guess1 = input(str.format("Pick a number between 1-{}: ", str(maxnumber - 1)))
	
	#cheat statement
		if int(guess1) == cheat:
			win = "Cheat"
			pass
			
		elif int(guess1) == theNumber:
			win = True
			pass
		elif int(guess1) > theNumber and int(guess1) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess1) < theNumber:
			print("Guess higher")
			pass
		elif int(guess1) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
		
#Guess #2 Diff - 3
	if win == False:
		
		print(str.format("lives: {}", lives - 1))
		guess2 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess2) == cheat:
			win = "Cheat"
			pass
		elif int(guess2) == theNumber:
			win = True
			pass
		elif int(guess2) > theNumber and int(guess2) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess2) < theNumber:
			print("Guess higher")
			pass
		elif int(guess2) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#Guess #3 Diff - 3
	if win == False:
		print(str.format("lives: {}", lives - 2))
		guess3 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess3) == cheat:
			win = "Cheat"
			pass
		elif int(guess3) == theNumber:
			win = True
			pass
		elif int(guess3) > theNumber and int(guess3) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess3) < theNumber:
			print("Guess higher")
			pass
		elif int(guess3) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#Guess #4 Diff - 3
	if win == False:
		print(str.format("lives: {}", lives - 3))
		guess4 = input(str.format("Nope, pick Another "))
	 
	#cheat statement
		if int(guess4) == cheat:
			win = "Cheat"
			pass
		elif int(guess4) == theNumber:
			win = True
			pass
		elif int(guess4) > theNumber and int(guess4) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess4) < theNumber:
			print("Guess higher")
			pass
		elif int(guess4) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#Guess #5 Diff - 3
	if win == False:
		print(str.format("lives: {}", lives - 4))
		guess5 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess5) == cheat:
			win = "Cheat"
			pass
		elif int(guess5) == theNumber:
			win = True
			pass
		elif int(guess5) > theNumber and int(guess5) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess5) < theNumber:
			print("Guess higher")
			pass
		elif int(guess5) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
		
#Guess #6 Diff - 3
	if win == False:
		print(str.format("lives: {}", lives - 5))
		guess6 = input(str.format("Nope, pick Another "))
	 
	#cheat statement
		if int(guess6) == cheat:
			win = "Cheat"
			pass
		elif int(guess6) == theNumber:
			win = True
			pass
		elif int(guess6) > theNumber and int(guess6) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess6) < theNumber:
			print("Guess higher")
			pass
		elif int(guess6) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#guess #7 Diff - 3
	if win == False:
		print(str.format("lives: {}", lives - 6))
		guess7 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess7) == cheat:
			win = "Cheat"
			pass
		elif int(guess7) == theNumber:
			win = True
			pass
		elif int(guess7) > theNumber and int(guess7) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess7) < theNumber:
			print("Guess higher")
			pass
		elif int(guess7) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass	
			
#guess #8 Diff - 3	

	if win == False:
		print(str.format("lives: {}", lives - 7))
		guess8 = input(str.format("Nope, pick Another "))
	#cheat statement
		if int(guess8) == cheat:
			win = "Cheat"
			pass
		elif int(guess8) == theNumber:
			win = True
			pass
		elif int(guess8) > theNumber and int(guess8) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess8) < theNumber:
			print("Guess higher")
			pass
		elif int(guess8) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass
			
#guess #9 Diff - 3
	if win == False:
		print(str.format("lives: {}", lives - 8))
		guess9 = input(str.format("Nope, pick Another "))
	
	#cheat statement
		if int(guess9) == cheat:
			win = "Cheat"
			pass
		elif int(guess9) == theNumber:
			win = True
			pass
		elif int(guess9) > theNumber and int(guess9) < maxnumber:
			print("Guess lower")
			pass
		elif int(guess9) < theNumber:
			print("Guess higher")
			pass
		elif int(guess9) >= maxnumber:
			print(str.format("Cheater, Its in between 1-{}", int(maxnumber - 1)))
			pass
		else:
			print("What did you do?")
			pass					
#end of diff - 3

#PRIZE / CONGRATS
if win == True:
	print("You Won. The number was", theNumber)
	
if win == "Cheat":
	print("You werent supposed to find this. You won!!")
	
#Loser

if win == False:
	print("You lost. The number was", theNumber)
input()
