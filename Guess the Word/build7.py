import random 
# library that we use in order to choose
# on random words from a list of words
name = input("Please enter your name")
# Here the user is asked to enter the name first
print("Good luck, "+name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
# Function will choose one random
# word from this list of words
word = random.choice(words)

guesses = ''

turns = 10

while turns > 0:
# any number of turns can be used here
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
			# for every failure 1 will be
			# incremented in failure
            failed += 1
        # user will win the game if failure is 0
		# and 'You Win' will be given as output
    if failed == 0:
		# this print the correct word
        print("You win")
        print("The word is: "+word)
    # every input character will be stored in guesses
    guess = input("Guess the character: ")
    guesses += guess
    # if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
    if guess not in word:
        turns -= 1
        print("Wrong")
    # check input with the character in word
        print("You have"+ turns, "more guesses left")
    # if the character doesn’t match the word
	# then “Wrong” will be given as output
        if turns == 0:
            print("You have no more guesses left, game over!")
    # this will print the number of
		# turns left for the user
    
        