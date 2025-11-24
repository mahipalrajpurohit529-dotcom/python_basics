# 8. Write a program to find the first and last digit of a number.

n = int(input("Enter n:"))

temp = n

print("last digits =",n%10)
power = 1

while(temp>0):
    power = power*10
    temp //= 10
power //= 10

print("First digit =",n//power)
