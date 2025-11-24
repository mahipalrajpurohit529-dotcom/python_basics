# 11.Write a program to find the power of a number using for loop

x = int(input("Enter the number:"))
y = int(input("Enter the power you want to find:"))

power = 1

for i in range(0,y):
    power *= x

print(f"{x} raised to the power of {y} is {power}")