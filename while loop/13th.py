# 13.Write a program to calculate the factorial of a number.

n = int(input("Enter n:"))

fact = 1

while(n>1):
    fact *= n
    n-=1

print(fact)
