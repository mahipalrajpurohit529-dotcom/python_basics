# Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
# on the following criteria:
# >= 90: Grade A
# >= 80: Grade B
# >= 70: Grade C
# >= 60: Grade D
# < 60: Grade F


marks = int(input("Enter your marks:"))

if(marks>100):print("please enter valid marks")
elif(marks >= 90): print("Your grade is A ")
elif(marks >= 80): print("Your grade is B ")
elif(marks >= 70): print("Your grade is C ")
elif(marks >= 60): print("Your grade is D ")
else: print("Your grade is F ")

