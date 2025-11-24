# 7. Write a program to calculate the sum of digits of a number.


n = int(input("Enter n:"))

p = str(abs(n))

digits = len(p)
sum = 0

for i in range(digits):
    sum = sum + int(p[i])

print(sum)
