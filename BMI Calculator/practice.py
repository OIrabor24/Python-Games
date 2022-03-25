height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = weight / (height/100)**2 

if BMI <= 18.4:
    print("You are underweight")

elif BMI <= 24.9:
    print("Your are relatively healthy!")

elif BMI <= 29.9:
    print("You are overweight!")

elif BMI <= 34.9:
    print("You are severly overweight, whoa Fatty!")

else:
    print("You are very obese and need to go on a diet for your own good, smh, fatass...") 

