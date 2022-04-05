import random 

def rock_paper_scissors():
    player = input("Select 'r' for Rock, 'p' for Paper, or 's' for Scissors: ")
    choices = ['r', 'p', 's']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"It's a tie! You both selected {opponent}!")

    if winner(player, opponent):
        return print(f"You win! {player} beats {opponent}!")

    if winner(player, opponent) != True:
        return print(f"You lose! {opponent} beats {player}!")

def winner(user, cpu):
    if (user == 'r' and cpu == 's') or (user == 'p' and cpu == 'r') or (user == 's' and cpu == 'p'):
        return True 
rock_paper_scissors() 