# # LCM 

# m = int(input("Enter m:"))
# n = int(input("Enter n:"))
# lcm=1
# k=m+n
# i=2
# while(i<k):
#     if(m%i==0 or n%i==0):
#         if(m%i==0 and n%i==0):
#             m/=i
#             n/=i
#             lcm*=i        
#         elif(m%i==0):
#             m=m/i
#             lcm*=i
#         elif(n%i==0):
#             n/=i
#             lcm*=i
#     else:i+=1
# print(lcm)





# Q.sum of digits


# n = int(input("Enter n:"))

# sum = 0

# while(n>0):
#     sum += n%10
#     n//=10
# print(sum)






# Q.strong

# n = int(input("Enter n:"))
# temp = n
# sum = 0

# while (temp>0):
#     x=temp%10
#     fact = 1
#     for i in range (2,x+1):
#         fact *= i
#     sum+=fact
#     temp//=10

# if(sum==n):print("Strong")
# else:print("Not strong")





# print a to z

# for i in range (97,123):
#     print(chr(i))





# Q. find all factors of a number

# n = int(input("Enter n:"))

# for i in range(1,n+1):
#     if(n%i==0):print(i)






# Q.prime factors

# n = int(input("Enter n:"))
# i=2
# while (n>1):
#     if(n%i==0):
#         print(i)
#         n//=i
#     else:i+=1



#Q.print reverse

# n = int(input("Enter n:"))
# rev=0

# while(n>0):
#     rev=rev*10 + n%10
#     n//=10

# print(rev)




#Q.prime numbers between 1 and n

# n = int(input("Enter n:"))



# for i in range(2,n+1):
#     count=0

#     for j in range (2,(i//2)+1):
#             if(i%j==0):count=1
#     if(count==0):print(i)



arr=[1,2,3,4]
for _ in arr :
    arr.pop(0)
    print(arr)