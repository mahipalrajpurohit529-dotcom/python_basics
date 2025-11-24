# 16.Write a program to print all Prime numbers between 1 to n.

n = abs(int(input("Enter n:")))

for p in range (2,n+1):
    count = 0
    for temp in range(2,int(p**0.5)+1):
        if(p%temp == 0):
            count += 1
            break
    if(count == 0): print(p,end=",")



