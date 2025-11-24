# 6. Write a program to count the number of digits in a number.

n = int(input("Enter n:"))

digits = 0

while(n!=0):
    digits += 1
    n //= 10

print(digits)