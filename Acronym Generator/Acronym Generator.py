"""Acronym generator: As Soon As Possible = ASAP"""

# Taking user input
user_input = input("Please enter the words in your favorite acronym: ") 

# Spliting the user input into individual words using split() method
phrase = user_input.split() 

# initializing an empty string to append the acronym
acronym = ''
# for loop to append acronym 
for word in phrase:
    acronym = acronym + word[0].upper()
print(f"{acronym}")
