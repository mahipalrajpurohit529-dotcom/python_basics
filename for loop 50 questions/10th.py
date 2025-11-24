# Given the list nums = [1, 3, 5, 7, 9], print the cumulative sum at each step using a for loop

nums = [1, 3, 5, 7, 9]
sum=0

for i in range (0,len(nums)):
    sum+=nums[i]
    print(f"at index = {i} :: the sum = {sum}")