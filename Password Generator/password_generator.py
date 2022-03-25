# import the random module
import random 
# Ask the user to enter the length of a password! saved as an int.
pass_len = int(input("Enter the length of your password: ")) 
# generate a list of possible password characters to be selected at random.
pass_data = "qwertyiuopbncmvasdfghkl8345020981234-_@#%^&**)" 
# Use random.sample() to collect random data from pass_data (as a list) & use .join() to join the list elements to form a string
password = "".join(random.sample(pass_data, pass_len)) 

print(password)