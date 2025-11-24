# 7. Write a program to calculate the sum of digits of a number.


n = int(input("Enter number:"))

sum = 0

while(n>0):
    sum += n%10
    n //= 10
print(sum)
