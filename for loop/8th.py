
# 8. Write a program to find the first and last digit of a number.



# using arrithematic:-

n = int(input("Enter n:"))

s = str(abs(n))
length = len(s)
power = 1

print("Last digit =",n%10)

for i in range (0,length-1):
    power *= 10

print("First digit =",n//power)



# using string:-


n = int(input("Enter n:"))

s = str(abs(n))
l = len(s)

print("First digit =",s[0])
print("last digit =",s[l-1] )
