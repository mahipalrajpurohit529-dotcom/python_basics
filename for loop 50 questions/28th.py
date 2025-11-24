# 28. Given list nums = [2, -3, 5, -1, 0, -7], count and print how many negative numbers are
# in the list using a for loop.

nums = [2, -3, 5, -1, 0, -7]
count=0

for i in nums :
    if(i<0):
        count+=1
print(count)