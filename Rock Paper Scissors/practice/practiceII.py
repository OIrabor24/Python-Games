import random 

def rock_paper_scissors():
    player = input("Select 'r' for rock, 's' for scissors, or 'p' for paper: ")
    choices = ['r', 'p', 's']
    computer = random.choice(choices)

    if player == computer:
        return print(f"You both selected {player} it's a tie!")

    if is_winner(player, computer):
        return print(f"You win, {player} beats {computer} every time!")

    if is_winner(player, computer) != True:
        return print(f"You lose, {computer} beats {player}!")

def is_winner(user, opponent):
    # r > s s > p p > r
    if (user == 'r' and opponent == 's') or (user == 'p' and opponent == 'r') or (user == 's' and opponent == 'p'):
        return True 

rock_paper_scissors() 