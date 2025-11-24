# 23. Given list nums = [3, 1, 4, 1, 5, 9, 2], print the list of numbers that are greater than
#     their immediate predecessor using a for loop.


nums = [3, 1, 4, 1, 5, 9, 2]
newelist=[]

for i in range (1,len(nums)):
    if(nums[i]>nums[i-1]):
        newelist.append(nums[i])
print(newelist)