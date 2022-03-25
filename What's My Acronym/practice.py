def Acronym():
    user_input = input('Enter the full meaning of an acronym! ')
    phrase = (user_input).split() 
    acronym = ""

    for word in phrase:
       acronym += word[0].upper() 

    print(acronym) 
Acronym() 
