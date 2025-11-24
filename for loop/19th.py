#  19.Write a program to check whether a number is Strong number or not
#  a. Strong number is a special number whose sum of factorial digits is
#  equal to the original number.
#  For example: 145 is a strong number. Since, 1! + 4! + 5! = 145


n = int(input("Enter n:"))

count = len(str(n))
sum = 0
ogn = n

for temp in range (0,count):
    ld = n%10
    fact = 1
    for i in range(1,ld+1):
        fact = fact*i
    sum += fact
    n //= 10

if(ogn == sum):print("STRONG NUMBER")
else:print("NOT A STRONG NUMBER")