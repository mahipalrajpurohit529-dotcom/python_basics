# 18. Given the list mixed = [1,'2', 3, '4', 5], print only the integer elements using a for loop

mixed = [1,'2', 3, '4', 5]

for x in mixed :
    if(type(x)==int):
        print(x)