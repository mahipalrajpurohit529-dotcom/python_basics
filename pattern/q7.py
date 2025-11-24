"""
for n=5 print:-

    1
   12
  123
 1234
12345

"""

n = int(input("ENTER n:"))

for i in range (1,n+1):
    m = 1
    for j in range (n,0,-1):
        if(j<=i):
            print(m,end="")
            m+=1
        else:print(" ",end="")
    print(" ")


