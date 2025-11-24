# 17.Write a program to find all prime factors of a number.


n = int(input("Enter n:")) 
temp = 2 
ogn = n
 
if(n<1):print("Make sure n is positive intiger")
else:
    for i in range(1,n+1): 
        if(n%temp == 0): 
            print(temp) 
            n//= temp 
        else : temp += 1
        
        if(n==1):break