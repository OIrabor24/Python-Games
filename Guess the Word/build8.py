import random 
# library that we use in order to choose
# on random words from a list of words
name= input("Please enter your name: ")
# Here the user is asked to enter the name first
print("Good luck, " + name )

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters: ")

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

        print("The word is " + word)
		# this print the correct word
        break 
    # every input character will be stored in guesses
    guess = input("Guess the characters: ")
    # check input with the character in word
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")

        print("You have" +turns, "more guesses")
# if the character doesn’t match the word
		# then “Wrong” will be given as output
    if turns == 0:
        print("Game over, you lose!")
        # this will print the number of
		# turns left for the user
        