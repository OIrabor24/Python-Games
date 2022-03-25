import random 

max_num = 10 

random_number = random.randint(1, max_num) 

guess = 0 

while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {max_num}: "))

    if guess < random_number:
        print("Too low... guess again!")

    elif guess > random_number:
        print("Too high... guess again!")

print(f"You got it! {random_number} is the correct number!")