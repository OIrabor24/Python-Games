import random 

def rock_paper_scissors():
    player = input("Choose 'r' for rock, 'p' for paper, or 's' for scissors: ")
    choices = ['r', 'p', 's']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"It's a tie! You both selected {player}") 

    if winner(player, opponent):
        return print(f"You win! {player} beats {opponent}!")

    if winner(player, opponent) != True:
        return print(f"You lose! {opponent} beats {player} everytime!")

def winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True 
rock_paper_scissors() 