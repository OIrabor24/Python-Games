"""Guess the number computer version. Ask the user to guess a number between 1 & 30. 
Prompt the user if the guess is too high or too low. Game ends when use guesses correct number."""
import random 

max_num = 20 

random_number = random.randint(1, max_num)

guess = 0 

while guess != random_number:
    guess = int(input(f"Enter a number between 1 and {max_num}: "))

    if guess < random_number:
        print("Too low... guess again!")

    elif guess > random_number:
        print("Too high... guess again")

print(f"You got it! The correct number is {random_number}") 