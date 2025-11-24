"""
print the pattern for n=5

A
AB
ABC
ABCD
ABCDE

"""


n = int(input("Enter n:"))

for i in range (1,n+1):
    c = 65
    for j in range (1,n+1):
        if(j<=i):
            print(chr(c),end="")
            c += 1
        else:print(" ",end="")
    print(" ")





