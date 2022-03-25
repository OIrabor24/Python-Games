import random 

max_num = 20

random_number = random.randint(1, max_num) 

guess = 0 

while guess != random_number:
    guess = int(input(f"Guess a number between 1 & {max_num}: "))

    if guess < random_number:
        print(f"{guess} is too low, guess again!")

    elif guess > random_number:
        print(f"{guess} too high, guess again!")

print(f"You guessed the number, it's {random_number}") 