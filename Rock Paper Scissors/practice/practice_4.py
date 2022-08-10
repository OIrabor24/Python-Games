import random 

def rock_paper_scissors():
    player = input("choose 'r' for Rock, 'p' for Paper, or 's' for Scissors: ")
    choices = ['r', 'p', 's']
    opponent = random.choice(choices) 

    if winner(player, opponent):
        return print(f"You win! {player} beats {opponent}!")
    
    if player == opponent:
        return print(f"It's a tie! you both selected {opponent}")

    if winner(player, opponent) != True:
        return print(f"You lose, {opponent} beats {player}!") 

def winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True 
rock_paper_scissors() 