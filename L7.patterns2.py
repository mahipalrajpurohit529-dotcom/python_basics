for i in range (1,6):
    for j in range (1,i):
        print(" ",end="")
    
    for k in range(1,7-i):
        print("*",end=" ")
    
    
    print(" ")

print(end="\n\n\n")



m=1
for i in range (1,6):
    for j in range (1,i):
        print(" ",end="")
    
    for k in range(1,7-i):
        if(m/10==0):print("  ",m,sep="",end=" ")
        else:print(m,end=" ")
        m+=1
    
    
    print(" ")
    

print(end="\n\n\n")


for i in range (1,6):
    m=1
    for j in range (1,i):
            print(" ",end="")

    for k in range(1,7-i):
        print(m,end=" ")
        m+=1
    
    
    print(" ")
