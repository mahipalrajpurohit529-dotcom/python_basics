# 49. Given list nums = [2,3,5,7,11,13,17,19], using only for loops, find and print all pairs
# (i, j) where i<j and nums[i] + nums[j] is a prime number.


nums = [2,3,5,7,11,13,17,19]

for i in range (0,len(nums)):
    for j in range (i+1,len(nums)):
        temp=nums[i]+nums[j]
        count=0
        for x in range (2,temp):
            if(temp%x==0):
                count=1
                break
        if(count==0):
            print(i,j)