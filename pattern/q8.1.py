
"""
for n = 5 print :-
ABCDE
 ABCD
  ABC
   AB
    A

"""



n = int(input("Enter n:"))

for i in range (n,0,-1):
    m=65
    for j in range (n,0,-1):
        if(j<=i):
            print(chr(m),end="")
            m+=1
        else:print(" ",end="")
    print("")