# 10 Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in
# kilograms) and height (in meters). Then categorize the BMI into:
# Underweight (BMI < 18.5)
# Normal weight (18.5 <= BMI < 24.9)
# Overweight (25 <= BMI < 29.9)
# Obesity (BMI >= 30)
# Use the formula: BMI = weight / (height ** 2)

height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kg:"))

bmi = weight / height**2

if(bmi < 18.5):print("Underweight")
elif(bmi < 24.9):print("Normal weight")
elif(bmi < 29.9):print("overweight")
else:print("Obesity")



