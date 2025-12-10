# Q. two sum problem

# a=[-1,0]
# target=-1
# ans=[]

# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if(a[i]+a[j]== target):
#             ans.append(i)
#             ans.append(j)
#             break
# print(ans)


#Q.duplicate check


# nums=[1,1,1,3,3,4,3,2,4,2]
# ans = 'false'

# for i in range (0,len(nums)):
#     for j in range (i+1,len(nums)):
#         if(nums[i]==nums[j]):
#             ans='true'
#             break

# print(ans)



#Q. maximum check

# a =[1,2,4,18,11,9]
# max=a[0]

# for i in range (0,len(a)):
#     if(max<a[i]):
#         max=a[i]
# print(max)



# Q. print the secondd largest in the list

# a=[5,7,21,34,11,1,19]

# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if(a[i]<a[j]):
#             a[i],a[j]=a[j],a[i]
# print(a[1])





#Q.print duplicate element from the list

# a=[0,1,13,2,1,13]

# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if(a[i]==a[j]):print(a[i])





#Q.reversing the list 

# a=[13,56,9,12,2,29]
# b=[]

# for i in range (len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)




#Q. number of even and odd elements

# a=[7,221,19,0,-13,56]
# even=0

# for i in range (0,len(a)):
#     x=a[i]
#     if(x%2==0):even+=1

# print("even =",even)
# print("odd =",len(a)-even)




#Q. add duplicates to a new list 

# a=[10,9,56,98,10,56]
# newlist=[]

# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if(a[i]==a[j]):
#             newlist.append(a[i])
#             break
# print(a)
# print(newlist)




#Q.for n=4 print
#    *   
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# n=int(input("Enter n:"))

# for i in range (1,n+1):
#     for j in range (n,0,-1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     for j in range (2,n+1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     print("")
# for i in range (n-1,0,-1):
#     for j in range (n,0,-1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     for j in range (2,n+1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     print("")





#Q.for n=5 print

#A
#BB
#CCC
#DDDD
#EEEEE

# n=int(input("Enter n:"))
# m=65

# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if(j<=i):print(chr(m),end="")
#         else:print(" ",end="")
#     m+=1
#     print(" ")






# Q for n =5 print
#     A    
#    A C
#   A   E
#  A     G
# A       I
#  A     G
#   A   E
#    A C
#     A



# n = int(input("Enter n:"))

# for i in range (1,n+1):
#     m=65
#     for j in range (n,0,-1):
#         if(j<=i):
#             if(i==j):print(chr(m),end="")
#             else:print(" ",end="")
#             m+=1
#         else:print(" ",end="")
#     for j in range (2,n+1):
#         if(j<=i):
#             if(i==j):print(chr(m),end="")
#             else:print(" ",end="")
#             m+=1
#         else:print(" ",end="")
#     print("")
# for i in range (n-1,0,-1):
#     m=65
#     for j in range (n,0,-1):
#         if(j<=i):
#             if(i==j):print(chr(m),end="")
#             else:print(" ",end="")
#             m+=1
#         else:print(" ",end="")
#     for j in range (2,n+1):
#         if(j<=i):
#             if(i==j):print(chr(m),end="")
#             else:print(" ",end="")
#             m+=1
#         else:print(" ",end="")
#     print("")





# Q. for n=4 print 
#    *   
#   * *
#  *   *
# *******


# n=int(input("Enter n:"))

# for i in range (1,n+1):
#     for j in range (n,0,-1):
#         if(j==i or i==n):print("*",end="")
#         else:print(" ",end="")
#     for j in range (2,n+1):
#         if(j==i or i==n):print("*",end="")
#         else:print(" ",end="")
#     print("")





#Q. for n=5 print
# ABCDE
#  ABCD
#   ABC
#    AB
#     A

# n = int(input("Enter n:"))

# for i in range (n,0,-1):
#     m=65
#     for j in range (n,0,-1):
#         if(j<=i):
#             print(chr(m),end="")
#             m+=1
#         else:print(" ",end="")
#     print("")






#Q. pascel triangle

# n=int(input("Enter n:"))
# mylist=[]

# for i in range (1,n+1):
#     temp=[]
#     for j in range (n,0,-1):
#         if(j<=i):
#             if(j==i or j==1):
#                 print("1",end=" ")
#                 temp.append(1)
#             else:
#                 m=mylist[i-2][j-1]+mylist[i-2][j-2]
#                 print(m,end=" ")
#                 temp.append(m)
#         else:print(" ",end="")
#     mylist.append(temp)
#     print("")

# print(mylist)





#Q. for n = 5 print 
# *********
# **** ****
# ***   ***
# **     **
# *       *
# **     **
# ***   ***
# **** ****
# *********


# n=int(input("Enter n:"))


# for i in range (n,0,-1):
#     for j in range (1,n+1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     for j in range (n-1,0,-1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     print("")
# for i in range (2,n+1):
#     for j in range (1,n+1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     for j in range (n-1,0,-1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     print("")






# n = int(input("enterr n:"))

# for i in range (n,0,-1):
#     for j in range (n,0,-1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     for j in range(2,n+1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     print("")
# for i in range (2,n+1):
#     for j in range(n,0,-1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     for j in range(2,n+1):
#         if(j<=i):print("*",end="")
#         else:print(" ",end="")
#     print("")



# list = [x for x in range (1,101) if x%5==0]
# print(list)

# mydict = {i:"hey" for i in range (10,16)}
# print(mydict)


# Q.you have been provided the number of days by the user 
#   you have to calculate the total amount recieved by the user 
#   if we started from monday the amount user recieve is 1 doller tuesday is two doller and so on to sunday at 7 doller
#   but the next monday he starts on monday with 2 doller and so on to sunday on 8 dollers
#   next monday starts from 3 doller and so on to sunday at 9 doller
#    

#  if user enter 7 then we add the money he recieved for 7 days (1+2+3+4+5+6+7=28)
# and so on




# Task: Create a list of squares for numbers 1–10 using list comp

# a = [x*x for x in range (1,11)]
# print(a)



# Task: Use filter to get only even numbers from numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers = [1,2,3,4,5,6,7,8,9,10]
# a = list(filter(lambda x :x%2==0 , numbers))
# print(a)


# Task: Add 5 to each number in numbers = [1,2,3,4,5,6,7,8,9,10] using map + lambda

# numbers = [1,2,3,4,5,6,7,8,9,10]

# a = list(map(lambda x : x+5 , numbers))
# print(a)


# Task: From numbers = [1,2,3,4,5,6,7,8,9,10], 
# keep only numbers greater than 5 using filter + lambda

# numbers = [1,2,3,4,5,6,7,8,9,10]
# a = list(filter(lambda x : x>5 ,numbers))
# print(a)



# Task: From numbers = [1,2,3,4,5,6,7,8,9,10], create a list of only even numbers.

# numbers = [1,2,3,4,5,6,7,8,9,10]

# a = [x for x in numbers if (x%2==0)]
# print(a)



# Task: Create a list of squares of even numbers from numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers = [1,2,3,4,5,6,7,8,9,10]

# a = [x*x for x in numbers if(x%2==0)]
# print(a)



# ask: From words = ["apple", "kiwi", "banana"], create a list of words in uppercase.

# words = ["apple", "kiwi", "banana"]

# a = [s.upper() for s in words ]
# print(a)


# Task: From numbers = [1,2,3,4,5,6], create a new list where
# even numbers are squared, and odd numbers remain unchanged using list comprehension

# numbers = [1,2,3,4,5,6]
# a = [x*x if(x%2==0) else x for x in numbers]
# print(a)



# Task: From matrix = [[1,2,3],[4,5,6],[7,8,9]],
# create a single list of all elements multiplied by 2

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# new = [x fwtfor x in ]


# Create a lambda that returns the square of a number

# x = lambda x : x*x
# print(x(7))


# ask: Create a lambda that adds two numbers and test it with numbers 5 and 3.

# x = lambda a,b:a+b
# print(x(5,3))


# Task: Create a lambda that returns True if a number is even, False if it’s odd,

# x = lambda x : x%2==0
# print(x(6))



#Task: From numbers = [1,2,3,4,5], use map + lambda to multiply each number by 3

# numbers = [1,2,3,4,5]
# a = map(lambda x : x*3 , numbers) 
# for x in a :print(x)




# Alright! Here’s Moderate Question 2:

# Task: From words = ["apple", "kiwi", "banana", "fig"], use filter + lambda to keep
# only words longer than 3 letters

# words = ["apple", "kiwi", "banana", "fig"]
# x = list(filter(lambda i:len(i)>3,words))
# print(x)



# ask: From words = ["apple", "kiwi"], 
# use map + lambda to convert all words to uppercase.

# words = ["apple", "kiwi"]
# x = list(map(lambda x:x.upper(),words))
# print(x)


# Task: From numbers = [1,2,3,4,5,6,7,8,9,10], multiply all numbers by 3,
#  then keep only numbers greater than 15

# numbers = [1,2,3,4,5,6,7,8,9,10]

# x = list(map(lambda i :i*3 , numbers))
# x = list(filter(lambda i : i>15 , x))
# print(x)


# Task: From numbers = [1,2,3,4,5,6], create a new list where 
# even numbers are doubled and odd numbers are tripled

# numbers = [1,2,3,4,5,6]

# i = list(map(lambda x : x*2 if (x%2==0) else x*3,numbers))
# print(i)


# sort list without sort()

# mylist = [10,3,54,23,555,22,86]

# for i in range(0,len(mylist)):
#     for j in range (i+1,len(mylist)):
#         if(mylist[i]>mylist[j]):
#             mylist[i],mylist[j]=mylist[j],mylist[i]
    
# print(mylist)

"""
hi i am mahipal
i come from a city called barmer where finished my school
then i moved to jaipur for my bsc

currently i am doing my aprenticeship at regex software jaipur and pursueing a career as a data scientist 
since i am not from an itt background everything about coding is new to my 
but that is also why everything is so exciting to me 

i have always been good at critical and logical thinkin plus i love maths 
and to become a data scientist you need exactly these skills so it complements me well
and that is why i am chasing it 

my main motivation is to prove it to my family that govt job is not the only way to succeed in life and that i can do it on my own terms 

my dream is to succeed as a data scientist and move to germany for a better quality of life 

"""



# febonacci series using generators :-

# def febonacci():
#     a=0
#     b=1
#     while(1):
#         if(a==0 and b==1):
#             yield a
#             yield b
#             temp=a+b
#             a=b
#             b=temp
#         else:
#             yield b
#             temp=a+b
#             a=b
#             b=temp

# g=febonacci()
# nn = int(input("Enter n:"))
# for i in range (0,nn):
#     print(next(g))



# # what if we want nth element:-
# g1=febonacci()
# nn = int(input("Enter n:"))
# i=0
# x="none"
# while(i!=nn):
#     x=next(g1)
#     i+=1

# print(x)






# Write a generator numbers() that yields natural numbers forever.
    # Use it to print 0, 1, 2 and then stop it with close(), making it print "stopped" from inside the generator


# def numbers():
#     i = 0
#     try:
#         while True:          
#             yield i
#             i += 1
#     except GeneratorExit:     
#         print("stopped")

# g = numbers()
# print(next(g))  
# print(next(g))  
# g.close()       





# class Employee:
#     company = "TechCorp"  # Class variable
    
#     def __init__(self):
#         self.name = "Alice"  # Instance variable
#         # company=input("Enter something:")
#         print(Employee.company)
#         self.company="hello"
#         print(self.company)

# e1=Employee()
# print(e1.company)

# e1 = Employee()






# class and obj ==>


# class student :
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# me = student("maahi",22)

# print(me.age,me.name)




# class car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
    
#     def fullname(self):
#         return f"{self.brand} {self.model}"
    
# car1=car("audi","a8","2025")
# x=car1.fullname()
# print(x)

# car2=car("BMW","M4","2024")
# y=car2.fullname()
# print(y)
        



# class dog :
#     species="golden retriever"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def description(self):
#         print(dog.species,self.name,self.age)
        

# d1=dog("bruno",12)
# d2=dog("muku",8)
# d3=dog("nigga",2)

# d1.description()
# d2.description()
# d3.description()




# class bankaccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=int(balance)

#     def deposite (self):
#         dep=int(input("Enter the amount you want to deposite:"))
#         self.balance+=dep
#         print(f"new balance = {self.balance}")

#     def withdraw (self):
#         wd=int(input("Enter the amount you want to withdraw:"))
#         if(wd<=self.balance):
#             self.balance-=wd
#             print(f"new balance = {self.balance}")
#         else:
#             print("Insuficient ammount")
        
#     def showbalance(self):
#         print(f"current balance = {self.balance}")
    
# me=bankaccount("Mahipal",20000)
# me.deposite()
# me.withdraw()
# me.showbalance()















# create three classes a,b,c
# make a normal variable in class a,b,c
# inharit a in b and b in c
# make 1 a class object and print the variable of all classes using that object of class a 
# make 1 b class object and print the variable of all classes using that object of class b
# make 1 c class object and print the variable of all classes using that object of class c


# class a:
#     x="hey"
# class b(a):
#     y="hello"
# class c(b):
#     z="bitch"


# o1=a()
# print(o1.x)
# # print(o1.y)
# # print(o1.z)

# o2=b
# print(o2.x)
# print(o2.y)
# # print(o2.z)


# o3=c
# print(o3.x)
# print(o3.y)
# print(o3.z)







# # make a class and make a method that prints hi
# # make another class that has same named method that prints hello
# # make a third class that inharits both classes(a,b)
# # and run those two methods using the object of third class
# # then change the order of inharitance and see the difference
# # it is called multiple inharitance 
# # read about it



# class first :
#     def f1(self):
#         print("hey")
    
# class second:
#     def f1(self):
#         print("hello")

# class third (second,first):
#     def f2(self):
#         print("bitch")

# o1=third()
# o1.f1()







# Parent Class: Person
# Attributes: name, age (passed into __init__)
# Method: show_person() → print name & age

# Child Class: Student(Person)
# Extra attribute: course (passed into constructor)
# Use super() to call Person’s constructor
# Method: show_student() → print all 3 details (name, age, course)

# Task
# Create a Student object → give example data
# Call both method


# class person :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def showperson(self):
#         print(f"age ==> {self.age}  ::  name ==> {self.name}")

# class student (person):
#     def __init__(self,name,age,course):
#         self.course=course
#         super().__init__(name,age)

#     def showstudent(self):
#         print(self.course ,self.age,self.name)  

# class A:
#     x=1
#     def __init__(self):
#         print("A init")
#         self.x = 5

# class B(A):
#     def __init__(self):
#         print("B init")
# obj = B()
# print(obj.x)




# stO1 = student("mahipal",25,"data science")
# stO1.showstudent()
# stO1.showperson()









# features of oops :-
# 1. encapsulation:-
    # bundling of data and methods that operate on that data within one unit
    # helps to restrict direct access to some of the object's components
    # helps to prevent accidental modification of data
# 2. inheritance
# 3. polymorphism:-
    # ability of different classes to be treated as instances of the same class through a common interface
    # allows methods to do different things based on the object it is acting upon
    # helps to reduce complexity by allowing the same interface to be used for different underlying forms (data types)
# 4. abstraction
# 5. security
# 6. reusability
# why oops :-
# 1. normal function doesnt give security to the data, anyone can access and modify the data
# 2. reusability: classes can be reused in other programs, functions cannot be reused easily
        # you might think that functions can also be reused but in large programs it becomes difficult to   manage
        # also anyone can use the function and modify it, which can lead to errors  
        # but classses provide better reusability and security
# 3. easy to manage: in large programs it is easier to manage classes and objects rather than functions
# 4. data hiding: classes can hide data from outside world, functions cannot hide data 



#imp example :-

import random
from abc import ABC,abstractmethod

class bankaccount(ABC) :
    def __init__(self,user_name,bank_balance):          # remember that even self is local variable 
        self.user_name=user_name
        self.bank_balance=bank_balance
        self.account_number=random.randint(10000000,10099999)
    
    def info(self):
        print(self.user_name,self.bank_balance)

    @abstractmethod
    def deposite(self):
        pass
    
    def withderaw(self,amount):
        if(self.bank_balance > amount and amount >0):
            self.bank_balance -= amount
        else:
            raise ValueError
        
class saving_account(bankaccount):
    def __init__(self,user_name,bank_balance):
        super().__init__(user_name,bank_balance)

    def deposite(self, amount):
        if(amount > 0):
            self.bank_balance+=amount

    def balance(self):
        print(self.__bank_balance)
        return self.__bank_balance

    def withderaw(self,amount):   # method overriding
        if self.bank_balance >= amount and self.bank_balance - amount >5000:
            self.bank_balance -= amount
        else :
            print("Minimum balance required is 5000")


s1=saving_account("shubham",2000)
print(s1.user_name)
s1.withderaw(2000)
s1.deposite(1000)
print(s1.bank_balance)









# abstraction 
# list deep copy and shallow copy (practicle way)