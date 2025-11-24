"""
for n=5 print :-

    *
   **
  ***
 ****
*****

"""


n = int(input("ENTER n:"))

for i in range (1,n+1):
    for j in range (n,0,-1):
        if(j<=i):print("*",end="")
        else:print(" ",end="")
    print(" ")

