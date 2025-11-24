# 21. Given the list nums = [12, 5, 8, 130, 44], find and print the largest number using a for loop

nums = [12, 5, 8, 130, 44]

a=0

for x in nums :
    if (x > a):
        a=x
print(a)