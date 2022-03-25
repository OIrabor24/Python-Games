"""Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user."""
# Example: input -> As Soon As Possible. Output -> ASAP
# Example: input -> World Health Organization. Output -> WHO
# Example: input -> Absent Without Leave. Output -> AWOL 

def Acronym():
    user_input = input('Enter the full meaning of an acronym: ')
    phrase = user_input.split() 
    acronym = ""

    for word in phrase:
        acronym += word[0].upper() 

    print(acronym)

Acronym() 



