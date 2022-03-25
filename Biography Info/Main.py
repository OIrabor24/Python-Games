"""Biography info: Ask a user for their personal info one question at a time. 
then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them."""
 # address = input('What is your address?: ')
# personal_goal = input('What is your # 1 personal goal?: ') 

name = input('What is your name?: ')
x = name.isalpha()

if not x:
    print('Invalid entry, what is your name (text characters only)!: ')
    name = input('What is your name?: ') 

dob = input('What is your date of birth?: ')
y = dob.isdigit() 
 
if not y:
    print('Invalid entry, What is your date of birth?: ') 
    dob = input('What is your date of birth?: ')

address = input('What is your address?: ')
z = address 

if not z:
    print('Invalid entry, please enter alphanumberic characters only!')

personal_goal = input('What is your # 1 personal goal?: ')
a = personal_goal

if not a:
    print('Invalid entry, please enter alphanumberic characters only!') 

print({'Name': name,
    'Date of Birth': dob, 
    'Address': address,
    'Personal Goals': personal_goal})