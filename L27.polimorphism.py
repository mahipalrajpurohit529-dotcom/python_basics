
# polimorpharism:- 
# it is a feature of oops which is used to behave the object of a class or the method or the operators in different ways
    # in python polimorpharism means that the same function name can be used for different types
    # for example we can use the same method name in different classes and it will work differently based on the class
    # treating methods differently based on the object that is calling them is called polimorpharism
    
# for eg:-
# print(1+2)      # 3
# print([1]+[2])    # [1,2]

# see how the same + operator is used for both integers and lists but it works differently based on the type of data



# same thing on methds :-


# class cat:
#     def sound(self):
#         print("meow meow")

# class dog:
#     def sound(self):
#         print("bark bark")

# c1=cat()
# d1=dog()

# c1.sound()      # meow meow
# d1.sound()      # bark bark

# check how the same method name sound() is used in both classes but it produces different outputs based on the class









# there are tw ways to achieve polimorpharism :-
    # 1. method overloading :- 
            # same method name with different parameters in the same class
            # in same class we have two functions of same name but different parameters
            # focus on the fact that both methods are in the same class

# class mathops:
#     def info(self):
#         print("first function with no parameters")

#     def info(self,a):
#         print(f"second function with one parameter a={a}")

# m1=mathops()        
# m1.info()   # if we had ran in any language that supports method overloading,then the first info() method would have been called   
# m1.info(5)  # if we had ran in any language that supports method overloading,then the second info(a) method would have been called

# but python does not support method overloading
        # main reason is because of dynamic typing in python
        # in python when we define a method it only keeps the last defined method with that name
        # the second reason we have something called Variable length arguments in python 
        # so we can achieve method overloading using that and so we do not need method overloading in python



# namespace :-
    # in simple terms,it just make sure that every variable,function,class has a unique name so that they do not conflict with each other
    # it is a container that holds a set of identifiers(names) and their corresponding objects
    # in python each class has its own namespace
    # so when we define two methods with same name in the same class    

# x=10
# x=20

# this is allowed in python but the first x=10 is lost
# because both variables are in the same namespace(global namespace)

# the same thing happens with methods in a class:-

# class test:
#     def func(self):
#         print("first function")
#     def func(self):
#         print("second function")

# t1=test()
# t1.func()       # second function









# 2. method overriding :- same method name in different classes (usually in parent and child class)

# class distributor:
#     def shopping(self):
#         print("30% discount on all products")
    
# class shopper(distributor):
#     price=1000

# customer1=shopper()
# customer1.shopping()        # 30% discount on all products



#  but if shopkeeper gives a 30% disccount then he doesnt get any profit
# so he wants to give only 10% discount
# so he overrides the shopping() method of parent class(distributor) in child class(shopper)




# class distributor:
#     def shopping(self):
#         print("30% discount on all products")
    
# class shopper(distributor):
#     price=1000
#     def shopping(self):
#         print("10% discount on all products")

# customer1=shopper()
# customer1.shopping()        # 10% discount on all products



# here you can see the parant and child have the same method name shopping() and same parameters
# but child is overriding the parent method for its own needs
# this is called method overriding

# in other words, method overriding is a feature where parant class and child class have same method name and same parameters
# but the execution or working is different based on the object that is calling the method
# this is called method overriding and it is a type of polimorpharism

# another importatnt point is that method overriding is usually done in parent and child class




# what about constructors?
# see constructors are also methods
# so can we override constructors too? 
# and only last defined constructor will be used for object creation


# class parent:
#     def __init__(self):
#         print("parent constructor called")

#     def __init__(self):
#         print("second parent constructor called")

# p1=parent()      # second parent constructor called







# operator overloading :-
# it is a type of polimorpharism where the same operator behaves differently based on the data type
# it is also a machenism through which we can achieve polimorpharism


# class twoAdd:
#     def info(self):
#         print("hey")

# t1=twoAdd()
# t2=twoAdd()
# print(t1,t2)        # memory addresses of t1 and t2

# print(t1 + t2)     # adding memory addresses of t1 and t2
#                    # will show error if we try to perform addition on two objects of a class without operator overloading

# see how the + operator is not working and if i want to change that behaviour i can overload the + operator in the class using __add__() method


# every operator in python is defined by a method called dunder method
# when we write a+b ,internally python calls a.__add__(b)
# so if we want to change the behaviour of + operator for our class we can define __add__() method in our class


# class twoAdd:
#     def __init__(self):
#         print("inside constructor")

#     def __add__(self,other):
#         print("inside add method",other)

# t1=twoAdd()
# t2=twoAdd() 
# print(t1 + t2)     # inside add method


# see how the + operator is now working and it is calling the __add__() method of the class
# this is called operator overloading