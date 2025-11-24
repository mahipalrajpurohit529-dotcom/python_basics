# 12.Write a program to find all factors of a number.


# all factors:-

n = int(input("Enter n:"))
temp = 2

for i in range(2,n+1):
    if(n%i == 0):print(i,end=",")
