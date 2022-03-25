"""Ask the user for a number between 1 and 1000. Then check if the number is odd or even. After which, produce a message like your number is odd"""

def odd_or_even():
    user_input = int(input("Pick a number between 1 & 1,000: ")) 

    if (user_input % 2 == 0):
        return print("That is an even number!")

    else:
        return print("The number you picked is odd!") 

odd_or_even() 