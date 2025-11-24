n = int(input("Enter n:"))

for i in range (1,n+1):
    m=1
    for j in range (n,0,-1):
        if(j<=i):
            print(m,end="")
            m+=1
        else:print(" ",end="")
    
         
    for k in range (2,n+1):
        if(k<=i):
            print(m,end="")
            m+=1
        else:print(" ",end="")
   
    print(" ")

for i in range (n-1,0,-1):
    m=1
    for j in range (n,0,-1):
        if(j<=i):
            print(m,end="")
            m+=1
        else:print(" ",end="")

    for k in range (2,n+1):
        if(k<=i):
            print(m,end="")
            m+=1
        else:print(" ",end="")
   

    print(" ")