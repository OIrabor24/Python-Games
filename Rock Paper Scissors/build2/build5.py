# import random module
import random 

# Print multiline instruction
# performstring concatenation of string
print("Rules of the Game: \n"
    +"Rock vs Paper -> Paper wins \n"
        +"Rock vs Scissors -> Rock wins \n"
    +"Scissors vs Paper -> Scissors wins \n")

#while loop
while True:
    print("Enter your choice: \n 1.Rock \n 2.Paper \n 3.Scissors \n")

# take the input from user
    choice = int(input("Your turn: "))

# OR is the short-circuit operator
# if any one of the condition is true
# then it return True value
# looping until user enters invalid input
    while choice > 3 or choice < 1:
        choice = int(input("Please make a valid selection: ")) 

# initialize value of choice_name variable
# corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors' 

# print user choice
    print("You selected " + choice_name) 
    print("Now it's your opponents turn....") 
# Computer chooses randomly any number
# among 1 , 2 and 3. Using randint method
# of random module
    comp_choice = random.randint(1, 3)  

# looping until comp_choice value
# is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1,3) 

# initialize value of comp_choice_name
# variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors' 

    print("Computer selects " + comp_choice_name)
    print(choice_name + " vs " + comp_choice_name) 
# condition for winning
    if ((choice == 1 and comp_choice == 2) or 
    (choice == 2 and comp_choice == 1)):
        print(" <==Paper wins==> ")
        result = 'Paper'

    elif ((choice == 1 and comp_choice == 3) or 
    (choice == 3 and comp_choice == 1)):
        print(" <==Rock wins==> ")
        result = 'Rock'

    else:
        print("<==Scissors wins==> ")
        result = 'Scissors' 
# Printing either user or computer wins
    if result == choice_name:
        print(" <==You win==> ") 
    else:
        print(" <==You lose==> ") 

    print("Do you want to play again? (Y/N): ") 

    answer = input()
# if user input n or N then condition is True
    if answer == 'n' or answer == 'N':
        break 
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for Playing Rock, Paper, Scissors!") 