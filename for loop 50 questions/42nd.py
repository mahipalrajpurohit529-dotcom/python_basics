# 42.Given list nums = [1,2,3,4,5,6,7,8,9], use a for loop to print a 3x3 matrix (rows)
# representation of the list (three numbers per row).

nums = [1,2,3,4,5,6,7,8,9]

count=0

for x in nums:
    if(count%3==0):
        print(" ")

    print(x,end=" ")
    count+=1
