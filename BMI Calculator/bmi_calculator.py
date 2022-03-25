"""BMI Calculator to output healthy height and weight mass."""
   
height = float(input("Please enter your height in centimeters: "))
weight = float(input("Please enter your weight in kilograms: "))

BMI = weight / (height/100) ** 2 

print(f"Your BMI is {BMI}")

if BMI <= 18.4:
    print("You are underweight!")

elif BMI <= 24.9:
    print("You are healthy.") 

elif BMI <= 29.9:
    print("You are overweight!")

elif BMI <= 34.9:
    print("You are obese") 

elif BMI <= 39.9:
    print("You are very fat!")

else:
    print("You are severely overweight, Yikes!")