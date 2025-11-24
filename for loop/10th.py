
# 10.Write a program to enter a number and print its reverse.


n = int(input("Enter n:"))

s = str(abs(n))
l = len(s)

for i in range (l-1,-1,-1):
    print(s[i],end ="")

