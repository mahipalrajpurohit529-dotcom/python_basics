# . Write a program to find the sum of first and last digit of a number.



n = int(input("Enter n:"))

s = str(abs(n))
l = len(s)

sum = int(s[0]) + int(s[l-1])

print("sum =",sum)

