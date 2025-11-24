# 38.Given numbers = [4, 9, 16, 25], print a new list of square roots (as integers) using a
# for loop.



numbers = [4, 9, 16, 25]
newlist=[]

for x in numbers:
    temp='none'
    for i in range(1,(x//2)+1):
        if(i*i==x):
            temp=i
    newlist.append(temp)

print(numbers,newlist)