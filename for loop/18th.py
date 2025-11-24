#  18.Write a program to check whether a number is an Armstrong number or
#   not.
#   a. An Armstrong number is a n-digit number that is equal to the sum
#   of the nth power of its digits. For example –
#   6 = 6^1 = 6
#   371 = 3^3 + 7^3 + 1^3 = 371


n = int(input("Enter n:"))

count = len(str(abs(n)))
sum = 0
ogn = n

for i in range (0,count):
    ld = n%10 
    sum = sum + ld**count
    n //= 10

if (sum == ogn):print("ARMSTRONG NUMBER")
else : print("NOT ARMSTRONG NUMBER")
