import random 

def guess(num):
    low = 1
    high = num 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f"Is it {guess}? Or is it low (L) or is it high (H) or is it correct (C): ").lower() 

        if feedback == 'l':
            low = guess + 1

        elif feedback == 'h':
            high = guess -1
    print(f"I got it! It's {guess}!")

guess(25)
    