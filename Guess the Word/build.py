import random 
# library that we use in order to choose
# on random words from a list of words
name = input("Enter your name: ")

print("Good luck", name)

# Here the user is asked to enter the name first


words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words) 

print("Guess the characters: ")

guesses = ''

turns = 10
# any number of turns can be used here
while turns > 0:
    failed = 0
	# counts the number of times a user fails
    
    for char in word:
# all characters from the input
	# word taking one at a time.
        if char in guesses:
# comparing that character with
# the character in guesses
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
        print("the word is ", word) 
        break 


    guess = input("Guess the character: ")
	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet

    guesses += guess 
	# every input character will be stored in guesses
    if guess not in word:
        turns -= 1 
	# check input with the character in word
        print("Wrong")
        # if the character doesn’t match the word
		# then “Wrong” will be given as output
        print(f"You have {turns} guesses left!")        

		# this will print the number of
		# turns left for the user
    if turns == 0:
        print("game over!") 
        
