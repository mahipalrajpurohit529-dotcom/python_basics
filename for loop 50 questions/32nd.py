# 32.Given nums = [10, 20, 30, 40, 50], compute and print the average using a for loop.


nums = [10, 20, 30, 40, 50]
sum=0

for i in nums :
    sum+=i
    
print(sum/(len(nums)))
