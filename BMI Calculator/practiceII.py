height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print(f"Your BMI is {BMI}") 

if BMI <= 18.4:
    print(f"{BMI}, You are underweight.") 

elif BMI <= 24.9:
    print(f"{BMI}, You are at a healthy weight.")

elif BMI <= 29.9:
    print(f"{BMI}, You are overweight.")

elif BMI <= 34.9:
    print(f"{BMI}, You are obese, lose weight!")

elif BMI <= 39.9:
    print(f"Too heavy, you need to lose weight!")

else:
    print(f"{BMI}, You are severely obese, you must lose a lot of weight!")  
