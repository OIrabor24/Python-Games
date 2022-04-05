"""BMI Calculator to output healthy height and weight mass.""" #BMI = w/ (h/100)**2; height cent, weight kilo
   
height = input("Please enter your height in centimeters: ")
weight = input("Please enter your weight in kilometers: ") 

BMI = weight * (height/100) ** 2 

print(f"Your BMI is {BMI}")
if BMI <= 18.4:
    print("You are underweight!")

elif BMI <= 24.9:
    print("You are healthy!")

elif BMI <= 29.9:
    print("You are overweight")

elif BMI <= 34.9:
    print("You are obese.")

elif BMI <= 39.9:
    print("You are very obese!")

else:
    print("Yikes, you should be on 'My 600 Pound Life!'") 


