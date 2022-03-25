# Odd or Even practice 1/5/22

def odd_or_even():
    user = int(input("Choose a number between 1 & 100: "))

    if (user % 2 == 0):
        return print("Your number is even")

    else:
        return print("Your number is odd!")
odd_or_even() 