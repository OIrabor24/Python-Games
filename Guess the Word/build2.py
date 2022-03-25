import random 
# library that we use in order to choose
# on random words from a list of words

name = input("Enter your name: ") 
# Here the user is asked to enter the name first

print("Good luck ", name) 

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
	
	# all characters from the input
	# word taking one at a time.
    for char in word:
        
        # comparing that character with
		# the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_") 
			
			# for every failure 1 will be
			# incremented in failure
            failed += 1
			

	
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
    if failed == 0:
        print("You win")
		
		# this print the correct word
        print("The word is: ", word)
        break 
    
    guess = input("Guess another character: ")

    guesses += guess 
	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
    if guess not in word:

        turns -= 1
	# every input character will be stored in guesses
        print("Wrong")

        print("You have ", + turns, "More guesses")

        if turns == 0:
            print("You lose!") 