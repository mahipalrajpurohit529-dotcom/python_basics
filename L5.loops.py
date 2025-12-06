

"""
LOOPS:-

- it helps to perform a repetative task 
- makes the code readable 
- there are 4 types of loops 
- for , while , do while , loop
- we will only study about for and while 

- the major difference is that if we know the number of iterations then we use for loop and if we dont then, we use while loop

"""




# SYNTEX:-

# for i in range(start,stop,step size)
# step size is by defaut 1 
# python does not include the end point

"""

for i in range(1,5,1):
    print(i)

for i in range(5,1,-1):
    print(i)

"""


# notice how the stoping point is not included in it
# you can also choose starting or ending point with a variable like in 6


"""

#Q. sum of loop

sum = 0
for i in range(1,6,1):
    sum += i
    print(i,sum)

"""




"""
#Q.sum of 98 to 66 sum in reverse

total = 0

for i in range(98,65,-1):
    total += i
print(total)

"""




"""
# odd and even after regex

for i in range (1,11):
    if(i%2 == 0):print("Regex even",i)
    else : print("Regex odd",i)

"""




"""
# Q. run a loop from 3 to 47 and get the sum of all even

sum = 0

for i in range(3,48):
    if(i%2 == 0): sum += i
print(sum)

"""


"""

# Q. run a loop from 114 to 56 and get the sum and count of number divisible by 6

count = 0
sum = 0

for i in range(114,55,-1):
    if(i%6 == 0):
        count += 1
        sum += i
print(sum , count)

"""

"""
# Q.check which numbers divide

num = int(input("Enter your number:"))
count = 0


for i in range(1,num+1):
    if(num % i == 0): 
        print(i)
        count += 1

print("total divisers = ",count)

"""



# prime number test







#string in range

data = "REGEX"

for a in data:
    print(a)



for i in range(0,5):
    print(i,data[i])





