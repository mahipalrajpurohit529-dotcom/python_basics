#  20.Write a program to check whether a number is perfect number or not
#  a Perfect number is a positive integer which is equal to the sum of
#  its proper positive divisors.
#  For example: 6 is the first perfect number
#  Proper divisors of 6 are 1, 2, 3
#  Sum of its proper divisors = 1 + 2 + 3 = 6.
#  Hence 6 is a perfect number.


n = int(input("Enter n:"))

sum = 0

for i in range (1,(n//2)+1):
    if(n%i == 0):
        sum += i
if(n == sum):print("PERFECT NUMBER")
else: print("NOT A PERFECT NUMBER")
