
# Given a list of integers nums, use for loops to find the longest contiguous
# subsequence whose elements form an increasing sequence and print its length and
# elements. (Implement scanning logic with for loops and indexing.


list = [1, 2, 3, 2, 4, 5, 6, 1, 2]
newlist=[]
long=1

for i in range (0,len(list)):
    temp=[list[i]]
    curr=list[i]
    for j in range (i+1,len(list)):
        if(curr<list[j]):
            temp.append(list[j])
            curr=list[j]
        else:
            break

    if(len(newlist)<len(temp)):
        newlist=temp

print(f"length = {len(newlist)} and the list is {newlist}")


        
        

# other way :- 


# list = [1, 2, 3, 2, 4, 5, 6, 1, 2]
# newlist=[]

# for i in range (0,len(list)):
#     temp=[list[i]]
#     curr=i
    
#     for j in range(i+1,len(list)):
#         if(list[curr]<list[j]):
#             temp.append(list[j])
#             curr=j
#         else:
#             break
    
#     if(len(newlist)<len(temp)):
#         newlist=temp

# print(f"length : {len(newlist)}  :: list : {newlist}")