# 9. Write a program to find the sum of first and last digit of a number.


n = int(input("Enter n:"))

ld = n%10
temp = n
power = 1

while(temp>0):
    power *= 10
    temp //= 10

power //= 10
fd = n // power

print("sum=",ld+fd)

