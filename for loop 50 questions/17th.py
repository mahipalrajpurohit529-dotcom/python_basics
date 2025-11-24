# Use a for loop to print the first 15 Fibonacci numbers starting with 0 and 1 (do it inline, without defining functions).

n=15

a = 0
b = 1

while(n>0):
    if(a==0 and b==1):
        print(a)
        print(b)
        next = a+b
        a=b
        b=next
        n-=2
    else:
        next = a+b
        a = b
        b = next
        print(next) 
        n-=1
        
