import random
# library that we use in order to choose
# on random words from a list of words

name = input("Enter your name: ")
# Here the user is asked to enter the name first

print("Good Luck ", name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words) 

print("Guess the characters: ") 

guesses = '' 

turns = 12
# any number of turns can be used here
while turns > 0:
    
    failed = 0
	# counts the number of times a user fails
    for char in word:
        # all characters from the input
	# word taking one at a time.
        
        if char in guesses:
            print(char)

        else:
            print("_") 	
		# comparing that character with
		# the character in guesses 
           
            failed += 1
			
			# for every failure 1 will be
			# incremented in failure
			
    if failed == 0:
        print("You win") 
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
        print("The word is ", word) 
        break

    guess = input("Guess another character: ")

    guesses += guess
		# this print the correct word
    if guesses not in word:
        turns -= 1

        print("Wrong") 

        print("You have " + turns, "more guesses")

        if turns == 0:
         print("Game over!") 
		