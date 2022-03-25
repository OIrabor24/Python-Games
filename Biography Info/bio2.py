"""Biography info: Ask a user for their personal info one question at a time. 
then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them."""
#isalpha(); isdigit(); name, dob, address, personal goal 

name = input("Enter your name: ")
x = name.isalpha()

if not x:
    print("Invalid entry! (text characters only): ")
    name = input("Enter your name: ") 

dob = input("Enter your date of birth: ")
y = dob.isdigit() 

if not y:
    print("Invalid entry! (enter digit values only!): ")
    dob = input("Enter your dob: ") 

address = input("Enter your address: ")
z = address

if not z.isalpha or z.isdigit():
    print("Invalid entry! Enter alphabet characters or digits: ")
    address = input("Enter your address: ")

personal_goal = input("Enter your #1 goal for 2022: ") 
a = personal_goal

if not a.isalpha() or a.isdigit():
    print("Invalid entry! Enter alphabet characters only: ")
    personal_goal = input("Enter your #1 goal for 2022: ") 

print({ 
    'name': name,
    'dob': dob,
    'address': address,
    'personal_goal': personal_goal,
})

