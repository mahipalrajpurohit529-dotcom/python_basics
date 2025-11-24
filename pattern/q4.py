"""
for n = 5 print :-

A
BB
CCC
DDDD
EEEE

"""


n = int(input("Enter n:"))
c = 65

for i in range (1,n+1):
    for j in range (1,n+1):
        if(j<=i):
            print(chr(c),end="")
        else:print(" ",end="")
    print(" ")
    c += 1


