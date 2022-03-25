import random 
from words import words 
from hangman_visual import lives_visual_dict 
import string 

def get_valid_word(words):  
    word = random.choice(words) # randomly chooses something from the list; our word list has spaces and dashes which would not be valid for python to parse
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words) 
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()  # what the user has guessed
 
    # Get user input for each letter
    while len(word_letters) > 0:
        pass 



    user_letter = input("Choose a letter: ")  