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

        feedback = input(f"Is the number {guess}? Is it too low (L) or too high (H) or is it just right (C)?").lower()  
        if feedback == 'l':
            low = guess + 1 
        elif feedback == 'h':
            high = guess - 1 
    print(f"I got it! its {guess}") 
guess(1000) 
