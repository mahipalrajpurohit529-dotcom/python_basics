# 14.Write a program to find LCM of two numbers.


m = abs(int(input("Enter first number:")))
n = abs(int(input("Enter second number:")))

temp = 2
lcm = 1

for i in range (max(m,n)*2):
    if(m%temp == 0 or n%temp == 0):
        if(m%temp == 0 and n%temp == 0):
            lcm *= temp
            m /= temp
            n /= temp
        elif(m%temp == 0): 
            lcm *= temp
            m /= temp
        elif(n%temp == 0):
            lcm *= temp
            n /= temp
    else:
        temp += 1

print(f"lcm = {lcm}")




# max (m,n) results in larger of m and n
# multiplying it by 2 gives you large enough range to cover all prime factors
# so the range from 0 to max(m,n)*2 is long enough