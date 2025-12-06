# Q. duplicate check



# mylist = [10,20,30,10,50,60,40,40,20]
# duplicat=[]

# for i in range (0,len(mylist)):
#     for j in range (i+1,len(mylist)):
#         if(mylist[i]==mylist[j]):
#             duplicat.append(mylist[i])
#             break
#     i+=1
# print(duplicat)






# Q.two sum problem

# a=[10,20,30,40,10,60,20]
# target=100


# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if(a[i]+a[j]==target):
#             print(f"the required numbers are {a[i]} and {a[j]}")





# Q.  purchase and sell later for max profit and print the purchase and sell date and price 

# prices = [7,1,5,3,6,4]
# date=[]
# profit=[]
# a=0

# for i in range (0,len(prices)):
#     for j in range (i+1,len(prices)):
#         if(prices[j]-prices[i]>a):
#             a=prices[j]-prices[i]
#             date=[i,j]
#             profit=[prices[i],prices[j]]

# print("max possible profit =",a)
# print(f"the buy date is {date[0]} and sell date is {date[1]}")
# print(f"the buy price is {profit[0]} and the sell price is {profit[1]}")





# Q. sorting a list without sort function

# a = [10,20,4,6,12,24]

# for i in range (0,len(a)+1):
#     for j in range (i,len(a)):
#         if(a[i]>a[j]):
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(a) 





# Q. add 1 to 10 in a list

# a=[]

# for i in range (1,11):
#     a.append(i)

# print(a)





# Q.add 1 to 10 in a list where every element is itself a list

# a=[]

# for i in range (1,11):
#     b=[i]
#     a.append(b)
# print(a)






#Q. pascal triangle

n=int(input("Enter n:"))
mylist=[]

for i in range (1,n+1):
    temp=[]
    for j in range (n,0,-1):
        if(j<=i):
            if(j==i or j==1):
                print("1",end=" ")
                temp.append(1)
            else:
                m=mylist[i-2][j-1]+mylist[i-2][j-2]
                print(m,end=" ")
                temp.append(m)
        else:print(" ",end="")
    mylist.append(temp)
    print("")
print(mylist)


