# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_square = height * height
bmi = round(weight / height_square)
if bmi < 35:
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight")
    if bmi > 18.5 and bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    if bmi > 25 and bmi < 30:
        print(f"Your BMi is {bmi}, you are slightly overweight.")
    if bmi > 30 and bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
