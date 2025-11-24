# 13.Write a program to calculate the factorial of a number.

n = abs(int(input("Enter n:")))


factorial = 1

for i in range(n,1,-1):
    factorial *= i

print(factorial)