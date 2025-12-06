# when we have to make a code and execute many times at different places then we make a blueprint or template of that block of code 
# and call it function

# function is a block of code or set of instructions that we can reuse again and again as per the requirment
# its main work is to make the code readable and reusable 

# how to make a function:-

# def fnct():             #def is keyword and fnct is the name of the function
#                         # also called as WORM
#                         # this is also called the user defined function 
#     print("hey")
#     print("niqqa")

# print(fnct())      # always use () to call a function





# def userdata():
#     x=input("enter number :")
#     print("User inserted =>",x)

# userdata()






# def greatings(name):            # name is a varaible   and in technical terms it is called a parameter  
#     print("Hey user good morning:",name)

# greatings("aman")    # aman is the value of the varaible "name" and in tech terms it is called argument




# parameter is a variable made during creation of a function
# the value of parameter that we give while calling a function is called as argument 




# def addtwo (z):
#     print(z+15)

# addtwo(30)
# addtwo(24)




# def addtwo(x,y):
#     print(x+y)

# addtwo(20,10)






# lifescope :-

# the lifescope of a variable is the accessesiblity or the place till which we can access the variable 
# the lifescope of a parameter is only inside the function 
# and the parameters do not exist outside the function
# they are called local varaibles

# course ="python"        # this types of variables can be accessed everywhere and are called as globle varaibles






# def me (a1):
#     print("local scope ",a1)

# me(43)   
# print(a1)        # cant be accessed outside the me as it is local 







# total=30          # global scope and can be accessed everywhere
# def me (a1):
#     total=100
#     print("local scope ",a1)
#     print("global scope",total)        # can be aceessed and modified locally and the cchanges will only stay in the local memory 
# me(43)  
# print(total)        # but the global value stay same  






# def naturalsum(num):
#     total = 0
#     for i in range (1,num+1):
#         total+=i

#     print(total)

# naturalsum(3)     # it will give the sum of first 3 numbers
# naturalsum(8)     # it will give the sum of first 8 numbers





# Q. find lcm



# def lcmo(m,n):
#     lcm=1

#     i=2
#     while(m>1 or n>1):
#         if(m%i==0 and n%i==0):
#             m//=i
#             n//=i
#             lcm*=i
#         elif(m%i==0):
#             m//=i
#             lcm*=i
#         elif(n%i==0):
#             n//=i
#             lcm*=i
#         else:
#             i+=1
#     print(lcm)

# lcmo(32,48)


# other way:-

# def lcmo(a,b):
#     c=0
#     if(a>b):
#         c=a
#     else:c=b

#     while(1):
#         if(c%a==0 and c%b==0):
#             print("lcm is =>",c)
#             break
#         else:
#             c+=1

# lcmo(32,48)








# types of arguments:-



# def test(a,b):
#     print(f"a : {a} :: b : {b} :: c : {c}")



# 1. Required argument:-
#       the type of argument where number of parameter should be equal to number of arguments



# 2. positional  argument :-
#        where the data is passed based on positional argument
#        first parameter gets the first argument value and the next one gets the next and so on



# 3. Keyword argument :-
#        where value goes to the named variable

# test(a=10,b=6,c=23)
# test(b=10,a=6,c=23)

# as long as we define every parameter and assign them arguments it works 
# but if we give argument to some parameters and not all then it may or may not work

# Eg=>
#     test(a=10,c=23,10)   # this will give error as c gets two values i.e, 23 and 10
#                          #   WE give no parameter to 10 so it by default goes to the positional argument i.e, c
#   test(a=10,6,23)        # this will work as we give a=110 then 6 by default goes to b and 23 to c



 
# 4. Default argument :-
        #  where we define default value to the parameter
        #  default argument allows you to asign a default value to a function parameter 

# def test (a,b,c=50):   # we give default value 50 to c . Unless user specifically changes value of c ,it will use value of c as 50
#     print(a,b,c)




# 5. Variable length argument (*args):-
  
            # its value change as per the requirement
            # we cant give keyword argument in it while calling the function
            # if we enter multiple values the system takes them 
            # and run the function for multiple entered arguments one after amother 
            # it always return a tupple  
            # it send items to the tupple in the sequeance we enter it


# def insta (*pic):                  # way to define VLA
#     print("we uplaoded :",pic)
# insta("tushar","aman","raj")
# insta(23,56,12,3)




# 6. Keyword variable length argument (**kwargs):-

    # uses two stars 
    # returns a dictionary
    # we may also make keys by ourselves and take argument by user

# def userdetails(**info):                  # way to define KVLA
#     print("we uplaoded :",info)

# userdetails(name="tushar",age=34,email="tushar@gmail.com")


# def googleform (**ans):
#     print(ans)

# googleform(Q1='a',Q2='c')










#  Return keyword in a function :-

    # once the compiler sees a return it exits the function
    # if you want to print a value we use the print but if we want to use it again later on then we use return    
    # we cant just simply give it to a varaible because it wont be worked outside the function because it is local memory


# def shaadi (num):
#     print("lifafa is for rupees :",num)
#     return(num+100)    #this will make sure whenever we call shaadi it returns nums

# x= shaadi(100)   # if we had not used return keyword the value of x would be nothing (none)
# print(x)         # but since we used return it will give that value



# # once we use return the function ends 


# def shaadi (num):
#     print("lifafa is for rupees :",num)
#     return(num+100)    
#     return (num//2)   # this line will never be read by the compiler as compiler dont read anything after the first return it sees

# print(shaadi(100))

# x= shaadi(100)   
# print(x)          # this will give you (nums+100) and never the (num//2)

# def ra (a):
#     return(a+x)

# print(ra(20))







# first class function :-

    # function can be saved to a varaible
    # can be used as an argument to another function
    # also be used in a list ,tupple or dictionary
    # can return another function

# if we use paranthesis when calling a funtion then we are calling the function
# but if we only use the name of the function without () then we get the memory address of the function

# def func():
#     print("hey")

# mylist=[10,40,func]
# mylist[-1]      # gives memory address of func
# mylist[-1]()    # gives "hey"

# # but if we 
# mylist=[10,40,func()]         # gives none as the value of func() 
# print(mylist)                 # also if we had used return in func then it wouldnt give none but rather the value of the return







# high order function :-
    # passing a function to another function as an argument
    # every high order function is first class function but not vice versa


# def adn (num):
#     print(num+1)
#     return(num+1)

# adn(10)

# def twn (x,y):
#     print("value inside two number function",x,y)

# twn(20,adn(30))                 # if we hadnt used return in adn this would have print 20,none




# def twn (x,y):
#     print("value inside two number function",x,y)
#     y(100)              # it shouldnt work and should give error, unless y becomes a function
# twn(20,adn)             # we give y the value - "adn" which is a function



# eg =>

# def sq (n):
#     return(n*n)

# def cube (a,func):
#     print(a*func(a))

# cube(2,sq)


# VLA and KVLA together:-

# def test(*y,**x):
#     print(y,x)
# test(94,54,66,33,"thf",45,hi=375,hello=475)



# def test(a,b=[]):
#     print(a,b)

# test(10,[433,55,257,1345,33])

# def test (a,b=[]):
#     b.append(a)
#     print(a,b)
# test(10)
# test(20)
# test(50)
# test(100,[])
# test(101,[12,56,344])