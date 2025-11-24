# Q. write an program that returns the largest even number from the list

# list = [2,5,-8,3,6,27,9]
# even='none'
 
# for x in list :
#     if(x%2==0 and even=='none'):
#         even=x
#     elif(x%2==0 and even<x):
#         even=x

# if(even=='none'):
#     print("none")
# else:
#     print(even)




# without using set() print every number that appears exactly once from the list

# nums = [1, 2, 2, 3, 4, 4, 4, 5]     # result should be 1,3,5
# newlist=[]

# for i in range (0,len(nums)):
#     count=0
#     for j in range (0,len(nums)):
#         if(i==j):
#             continue
#         if(nums[i]==nums[j]):
#             count+=1
#             break
        
#     if(count==0):
#         newlist.append(nums[i])


# for x in newlist:
#     print(x)
    
        


# memory shit(call by shit):-

# x = [1,2,3,4,5,6]
# y = x
# y.append(9)
# print(x)



# Write a program that prints all numbers from 1 to 50, but for multiples of 3 print "Fizz", 
# for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz"

# for i in range(1,51):
#     if(i%3==0 and i%5==0):
#         print("fizzbuzz")
#     elif(i%3==0):
#         print("fizz")
#     elif(i%5==0):
#         print("buzz")
#     else:
#         print(i)




# take multiple inputs from the user and add those ints to a list and print it

# 1st way:-

# nums = input("Enter numbers separated by space: ").split()
# nums = [int(x) for x in nums]  # convert to integers
# print(nums)


# 2nd way :-

# nums=[]
# while True:
#     x=input("Enter number (or enter when finished):")
    
#     if(x==""):
#         break
#     else:
#         nums.append(int(x))

# print(nums)
    

# Write a program that:
# Takes any number of integers as input from the user (dynamic input).
# Finds the numbers that appear more than once.
# Prints a list of duplicates, without using set()

# nums= input("Enter number separated by space ").split()
# nums= [int(x) for x in nums]

# duplist=[]

# for i in range(0,len(nums)):
#     for j in range (i+1,len(nums)):
#        if(nums[i]==nums[j]):
#            duplist.append(nums[i])

# print(duplist) 



# Given a list of integers, write a Python program (no built-in functions like max(), sort(), etc.) 
# to find the second largest unique number in the list

# list = [4, 1, 7, 7, 3, 4, 9]
# newlist=[]

# for i in range(0,len(list)):
#     if(list[i] not in newlist):
#         newlist.append(list[i])

# for i in range(0,len(newlist)):
#     for j in range(i+1,len(newlist)):
#         if(newlist[i]>newlist[j]):
#             newlist[i],newlist[j]=newlist[j],newlist[i] 

# print(newlist[-2])



#Q. Without using min(), max(), sort(), or creating another list,
# find and print the smallest and largest number from this list
# use only one loop and 2 variables

# nums = [12, 4, 19, -3, 7, 0, 22, -1]

# smallest=nums[0]
# largest=nums[0]

# for i in range(0,len(nums)):
#     if(nums[i]<smallest):
#         smallest=nums[i]
#     if(nums[i]>largest):
#         largest=nums[i]

# print(smallest,largest)

