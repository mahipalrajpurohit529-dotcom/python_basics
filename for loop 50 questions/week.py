
# Q.you have been provided the number of days by the user 
#   you have to calculate the total amount recieved by the user 
#   if we started from monday the amount user recieve is 1 doller tuesday is two doller and so on to sunday at 7 doller
#   but the next monday he starts on monday with 2 doller and so on to sunday on 8 dollers
#   next monday starts from 3 doller and so on to sunday at 9 doller
#    

#  if user enter 7 then we add the money he recieved for 7 days (1+2+3+4+5+6+7=28)
# and so on


# x= int(input("enter n:"))
# sum=0
# start = 1
# temp=start

# for i in range (1,x+1):
    
#     sum+=temp
#     temp+=1

#     if(i%7==0):
#         start+=1
#         temp=start

    

# print(sum)





# Q.2  longest subsequent list


# list =[10,14,15,3,7]
# longest=0

# for i in range (0,len(list)):
#     temp=list[i]
#     length=1
#     for j in range(i+1,len(list)):
#         if(temp<list[j]):
#             temp=list[j]
#             length+=1
#         else:
#             break
#     if(length>longest):
#         longest=length
    
# print(longest)




# Q. you have been given a string . And you have to print the max rep chr

# s = "aaaabbssskkkddyyvhffeeekooooooahjhhhh"
# longest=0

# for i in range(0,len(s)):
#     temp=1
#     for j in range (i+1,len(s)):
#         if(s[i]==s[j]):
#             temp+=1
#         else:
#             break
    
#     if(temp>longest):
#         longest=temp
# print(longest)




# Q. frequency of each chr

# s="abcab"
# mylist=[]
# mydict={}

# for i in range (0,len(s)):
#     temp=""
#     temp += s[i]
#     print(temp)
#     for j in range (i+1,len(s)):
#         temp += s[j]
#         print(temp)
    


s="abcab"
mylist=[]
mydict={}

for i in range (0,len(s)):
    temp=""
    temp += s[i]
    if(s[i] not in mydict):mydict[s[i]]=1
    else:mydict[s[i]]+=1

    for j in range (i+1,len(s)):
        temp += s[j]
        if(temp not in mydict):mydict[s[i]]=1

        print(temp)
    

