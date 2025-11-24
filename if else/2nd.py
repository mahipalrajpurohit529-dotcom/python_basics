# Q2 Write a program that takes three numbers as input and prints the largest of the three.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if(a >= b and a >= c): print(f"The largest number is {a}")
elif(b >= a and b >= c ):  print(f"The largest number is {b}")
else: print(f"The largest number is {c}")

