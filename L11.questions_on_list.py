# mylist = [10,11,12,15,19]

# #1st way :-

# for x in mylist:
#     print(x,end=" ")

# print(" ")

# # 2nd way:-

# for i in range (0,len(mylist)):
#     print(i,mylist[i])







# Q. print odd numbers

# mylist = [10,11,12,15,19]
# oddlist=[]
# for i in range (0,len(mylist)):
#     curr=mylist[i]
#     if(curr%2!=0):
#         print(curr)
#         oddlist.append(curr)

# print(oddlist)





# Q. find maximum

# mylist = [10,11,12,15,19]
# mylist.sort()
# print(mylist[len(mylist)-1])


# other way :-

# mylist = [10,11,12,15,19]

# a = mylist[0]

# for i in range (0,len(mylist)):
#     if(a<mylist[i]): a=mylist[i]
# print(a)






# Q.

# mylist=[10,11,2,3,19]
# a=[]
# sum=0
# for i in range (0,len(mylist)):
#     sum=sum+mylist[i]
#     a.append(sum)
# print(a)






# Q.extract the duplicate items and add them to a new list


# mylist=[10,19,56,98,10,56]
# newlist=[]
# neededlist=[]

# for i in range(0,len(mylist)):
#     curr = mylist[i]
#     if(curr in newlist):neededlist.append(curr)
#     else:newlist.append(curr)

# print(newlist)
# print(neededlist)





# Q. 

# x = "ishan hey"
# consonant=[]
# vowel=[]

# check=['a','e','i','o','u']

# for i in range (0,len(x)):
#     curr = x[i]
#     if(curr in check):vowel.append(curr)
#     else:consonant.append(curr)

# print(consonant)
# print(vowel)






# Q. palindrome list check

# mylist = [10,20,30,50,30,20,10]
# end=len(mylist)-1
# p=1
# for i in range (0,len(mylist)):
#     print(mylist[i],end=" ")
#     print(mylist[end])
#     if(mylist[i]!=mylist[end]):
#         p=0
#         break
#     end-=1
# if(p==1):print("Palindrome")   
# else:print("not palindrome")  



# you can also check if the value of i is same as [len(mylist)-1] which indicates that the loop ran for all elements
# if it ran for all elements then it is palindrome
# if(i==len(mylist)-1):print("Palindrome")
# else:print("Not a palindrome")



# in while loop:-
# mylist = [10,20,30,50,30,20,10]
# i=0
# end=len(mylist)-1
# p=1
# while(i<=end):

#     if(mylist[i]!=mylist[end]):
#         p=0
#         break
#     end-=1
#     i+=1
# if(p==1):print("Palindrome")   
# else:print("not palindrome")  







#Q two pointer approach in duplicate list check

# mylist=[10,20,10,46,87,90,87]

# start = 0
# end = len(mylist)-1

# while(start<end):
#     if(mylist[start]==mylist[end]):
#         print(mylist[start])

#     end-=1

#     if(end==start):
#         end=len(mylist)-1
#         start+=1


