"""Ask the user for a number between 1 and 1000. Then check if the number is odd or even. After which, produce a message like your number is odd"""


def odd_or_even():
    print("Welcome to the odd or even game! Please pick a number between 1 & 1000: ")

    user_input = int(input('What number are you thinking? '))
     

    if (user_input % 2 == 0):
        print("That's an even number! Have another?")

    else:
        print("That's an odd number! Have another?") 


odd_or_even() 