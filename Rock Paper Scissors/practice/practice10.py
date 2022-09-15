import random 

def rock_paper_scissors():
    player = input("Choose 'r' for Rock, 'p' for Paper or 's' for Scissors: ")
    choices = ['r', 'p', 's']
    opponent = random.choice(choices) 

    if player == opponent:
        return print(f"{player} vs {opponent}, it's a tie!")

    if winner(player, opponent):
        return print(f"You win! {player} beats {opponent}!")

    if winner(player, opponent) != True:
        return print(f"You lose! {opponent} beats {player}...") 

def winner(human, computer):
    if (human == 'r' and computer == 's') or (human == 'p' and computer == 'r') or (human == 's' and computer == 'p'):
        return True 
rock_paper_scissors() 