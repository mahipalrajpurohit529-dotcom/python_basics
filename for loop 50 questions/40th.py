# 40.Given a positive integer n = 28, use a for loop to find and print all its proper divisors
# (excluding n) and state whether n is perfect (sum of proper divisors equals n).

n = int(input("Enter n:"))
sum=0

for i in range (1,n):
    if(n%i==0):
        print(i,end=" ")
        sum+=i
print(" ")
if(sum==n):print("perfect number")
else:print("Not a perfect number")