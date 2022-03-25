import random 

def rock_paper_scissors():
    player = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ") 
    choices = ['r', 'p', 's']
    opponent = random.choice(choices) 

    if player == opponent:
        return print(f"It's a tie! You both selected {player}") 

    if winner(player, opponent):
        return print(f"You won! {player} beats {opponent}!")

    if winner(player, opponent) != True:
        return print(f"You lose! {opponent} beats {player}")

def winner(player1, computer):
    if (player1 == 'r' and computer == 's') or (player1 == 'p' and computer == 'r') or (player1 == 's' and computer == 'p'):
        return True 
rock_paper_scissors() 