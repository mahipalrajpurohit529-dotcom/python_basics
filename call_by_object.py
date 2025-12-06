

"""


CALL BY OBJECT REFERENCE

check in notebook

if you make a int variable python saves 0 to 255 in its chachhe memory  and so if
x = 200
and y = 200
then they have same memory address

but after that it changes memory variable
so if a = 300 
and y = 300

they have different memory address



but if x = 345
and y = x
then y and x have same memory address no matter what the value of x you give

"""



# def func(z):
#     print(z,id(z))
# a=10
# print(a,id(a))
# func(a)







"""
call by object reference :-
    the ref will depend on the type of value/object we pass on
    works defferently for int,string or float

    
there are two types of data types :- 
    mutable :- list,set,sictionary
    immutable:- float,int,complex number,tupple,string,frozenset,boolean

    
    mutable and immutable are decided by memory
    when making a change to a data types if the memory address change then the data is immutable 
    otherwise if the memory address stay same then the data is mutable

"""

# a=10
# print(a,id(a))
# a+=2
# print(a,id(a))


# you can see the memory address changed therefor int is an immutable type of data




# if the data type is immutable then:-(call by value)
# when we assign z = a then z access the memory address of a 
# and if we make changes to z then the memory address of z changes and any changes made to z will only be applied to z


# def func(z):
#     print(z,id(z))

# a=10
# print(a,id(a))
# func(a)



# a=10
# z=a
# z+=12
# print(a,id(a))
# print(z,id(z))





# if the data type is mutable then:-(call/pass by reference)
# when we assign z=a then z access the memory address of a 
# and any changes made on z will also affect a
# because it doesnt make new memory address


# def func(z):
#     z.append(60)
#     print(z,id(z))


# a=[10,40]
# print(a,id(a))
# func(a)

# a=[10,29]
# z=a
# z.append(12)
# print(a,id(a))
# print(z,id(z))


# num=10
# def test():
#     num=20
#     print(num)

# test()        # this prints 20 (local memory)
# print(num)  # this prints 10 (globle memory)


# if we want local changes to affect the globale memory we use global keyword:-

# num=10
# def test():
#     global num
#     num=20
#     print(num)
# test()
# print(num)


