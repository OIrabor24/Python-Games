import random 

def rock_paper_scissors(): 
    user = input("Select 'r' for rock, 'p' for paper, or 's' for scissors: ") 

    choices = ['r', 'p', 's'] 

    opponent = random.choice(choices) 

    if user == opponent:
        return print(f"It's a tie! You both selected {user}!")

    if is_winner(user, opponent):
        return print(f"You win! {user} beats {opponent}!")

    if is_winner(user, opponent) != True:
        return print(f"You lose, {opponent} beats {user}") 

def is_winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True 

rock_paper_scissors()