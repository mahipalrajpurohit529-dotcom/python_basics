# 24.Given the list numbers = [2, 4, 6, 8, 10], create and print a new list containing only
#    the odd numbers using a for loop


mylist = [2, 3, 4, 6, 8, 10]
oddlist = []

for x in mylist :
    if(x%2 != 0):
        oddlist.append(x)
print(oddlist)

