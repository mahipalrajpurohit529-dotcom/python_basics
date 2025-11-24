# 43.Given list nums = [0,1,2,3,4,5], shift all elements to the right by one position using a
# for loop (the last element becomes first).

nums = [0,1,2,3,4,5]
new=[]

for i in range(0,len(nums)):
    new.append(nums[i-1])
print(new)