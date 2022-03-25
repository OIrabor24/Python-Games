"""Biography info: Ask a user for their personal info one question at a time. 
then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them."""
#isalpha(); isdigit(); name, dob, address, personal goal 

name = input("Enter your name: ")
x = name.isalpha()

if not x:
    print("Invalid entry! Enter alphabet characters only.")
    name = input("Enter your name: ") 

dob = input("Enter your date of birth: ")
y = dob.isdigit() 

if not y:
    print("Invalid entry! Enter numbers only.")
    dob = input("Enter your date of birth: ") 

address = input("Enter your address (numbers & letters only): ")
a = address 

if not a.isalpha() or a.isdigit():
    print("Invalid entry! Enter numbers & letters only. ")
    address = input("Enter your address (numbers & letters only): ") 

personal_goals = input("Enter your #1 personal goals for 2022: ") 
b = personal_goals

if not b.isalpha() or b.isdigit():
    print("Invalid entry! Enter numbers & letters only: ") 
    personal_goals = input("Enter your #1 personal goals for 2022: ") 

print({ 
    'name': name,
    'dob': dob,
    'address': address,
    'personal_goal': personal_goals,
})