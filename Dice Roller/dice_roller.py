import random 

#initiating a while loop to keep the program executing (continue rolling..)
while True:
    print("Continue rolling...")

#Using random.randint() to generate a random value between 1 & 20 (the number is)
    print(f"The number is", random.randint(1,20))

# Asking user to roll the dice again or quit
    roll_again = input("Play again? Type 'y' for yes, or 'n' for no: ")
#If the user answers 'n' for no the loop will break and the program execution stops otherwise the program will continue executing.
    if roll_again == 'n':
        break 
    