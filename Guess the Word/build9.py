import random 
# library that we use in order to choose
# on random words from a list of words
name = input("Welcome, please enter your name: ")
# Here the user is asked to enter the name first
print("Good luck, " + name)
 
words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the letters: ")

guesses = ''

turns = 10

while turns > 0:
    failed = 0
# any number of turns can be used here
    for char in word:
	# counts the number of times a user fails
       if char in guesses:
           print(char)
       else:
           print("_")
# all characters from the input
	# word taking one at a time.
           failed += 1
    # comparing that character with
		# the character in guesses
			# for every failure 1 will be
			# incremented in failure
    if failed == 0:
        print("You win")
       
        print("The word is, " + word)
    # user will win the game if failure is 0
		# and 'You Win' will be given as output
        break 
		# this print the correct word
    guess = input("Guess the letters: ")
   
    guesses += guess
    # every input character will be stored in guesses
    if guess not in word:
        turns -= 1
       
        print("wrong") 
       
        print("You have " + turns, "more guesses") 
    # check input with the character in word
        if turns == 0:
            print("You lose, game over") 
# if the character doesn’t match the word
		# then “Wrong” will be given as output
        # this will print the number of
		# turns left for the user
       