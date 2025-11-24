#  2.Write a program to print all natural numbers in reverse (from n to 1). 
#    using while loop


n = int(input("Enter n:"))

while(n>0):
    print(n,end=",")
    n -= 1

