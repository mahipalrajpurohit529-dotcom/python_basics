# 46.Given two lists of possibly different lengths, a = [1,3,5,7] and b = [2,4,6], merge them
# into a single list by alternating elements (start with a[0]) using only for loops and
# indexing. If one list runs out, append the remaining elements of the longer list.

a = [1,3,5,7] 
b = [2,4,6]
newlist=[]

for i in range (0,5):
    if(i<4):
        newlist.append(a[i])
    if(i<3):
        newlist.append(b[i])
print(newlist)