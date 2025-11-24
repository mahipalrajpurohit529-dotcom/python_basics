"""
for n = 5 print :-

12345
 1234
  123
   12
    1

"""
n = int(input("Enter n:"))

for i in range (n,0,-1):
    m=1
    for j in range (n,0,-1):
        if(j<=i):
            print(m,end="")
            m+=1
        else:print(" ",end="")
    print("")
