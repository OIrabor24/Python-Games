import random 

max_num = 30 

random_number = random.randint(1, max_num) 

guess = 0

while guess != random_number:
    guess = int(input(f"Guess a number between 1 & {max_num}: ")) 

    if guess < random_number:
        print(f"{guess}, Too low... guess again!")

    elif guess > random_number:
        print(f"{guess}, Too high... guess again!")  
print(f"You got it! The correct number was {guess}!")   