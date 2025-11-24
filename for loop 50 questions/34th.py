# 34.Given list nums = [5, 2, 9, 1, 5, 6], use a for loop to create and print a sorted version
# of the list using simple selection sort logic (implement selection sort using for loops, no
# built-in sort())


nums = [5, 2, 9, 1, 5, 6]

for i in range (0,len(nums)):
    for j in range (i+1,len(nums)):
        if(nums[j]<nums[i]):
            nums[i],nums[j]=nums[j],nums[i]

print(nums)
