#  Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
#  for Monday, 2 for Tuesday, etc.).

day = int(input("Enter the day number:"))

if(day == 1):print("Monday")
elif(day == 2):print("Tuesday")
elif(day == 3):print("Wednesday")
elif(day == 4):print("Thursday")
elif(day == 5):print("Friday")
elif(day == 6):print("Saturday")
elif(day == 7):print("Sunday")
else:print("Please enter a valid day number")
