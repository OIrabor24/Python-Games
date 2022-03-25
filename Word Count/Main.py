"""Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output"""
# You can take this a step further and open a file that is handed to you, count the number of words in it, & print it out!


def Word_Count():
    print('Welcome to word count, a simple game where you input your thoughts and we give you a special output!')
    prompt = input("What's on your mind today?: ")
    prompt_length = len(prompt.split()) 
    print(f"Thank you, you just told me what's on your mind in {prompt_length} words! ") 

Word_Count() 

