# 5. Write a program to find the sum of all odd numbers between 1 to n.

n = int(input("Enter n:"))
sum = 0

for i in range (1,n+1):
    if(i%2 != 0):sum += i

print(sum)






