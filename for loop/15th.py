# 15.Write a program to check whether a number is Prime number or not.


n = int(input("Enter n:"))

if(n<0): 
    print("NOT PRIME")
else:
    count = 0

    for temp in range(2,(n//2)+1):
        if(n%temp == 0):
            count += 1
            break
    
    if(count == 0): print("PRIME")
    else:print("NOT PRIME")




