# 12.Write a program to find all factors of a number.

n = int(input("Emter the number:"))
fact = 1

while(fact<=n):
    if(n%fact == 0): print(fact,end=", ")
    fact += 1