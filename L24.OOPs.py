# OOPS stands for Object Oriented Programming Systems
# it is a software design pattern based on the concept of objects


# what is object?
# object is a collection of data (attributes) and methods (functions) that operate on the data
# object is a real time entity that has characteristics and behavior
# example: car is an object, it has attributes like color, model, speed and behaviour like start, stop, accelerate
# we use class to create objects



# what is class?
# class is a blueprint for creating objects
# it defines a set of attributes and methods that the created objects will have
# it is just a template, it does not occupy any memory
# class can be used to create multiple objects with same attributes and methods



# why dont we use functions and variables instead of classes and objects?
# 1. normal function doesnt give security to the data, anyone can access and modify the data
# 2. reusability: classes can be reused in other programs, functions cannot be reused easily 
        # you might think that functions can also be reused but in large programs it becomes difficult to manage
        # also anyone can use the function and modify it, which can lead to errors
        # but classses provide better reusability and security





# class housedesign:
#     colour="white"
#     price=50000
    
# tusharhome=housedesign()                        # object=class()
# print(tusharhome,tusharhome.price,tusharhome.colour)

# t2=housedesign()
# print(t2)                       # every object has a different memory address




# every object made will have the properties by class
# but if we want to change some  attributes we can do it by simply assigning it for that perticular object
# but those changes will only apply to that perticular object 
# the class(blueprint) will retain its original values


# tusharhome.colour='green'
# print(tusharhome.colour)
# print(housedesign.colour)      # class attribute remains same



# but if we want the changes to be applied to all objects then we have to change the class attribute itself
# housedesign.colour='yellow'


# by the way any variable made inside the class is called as class variable
# class variables are accessed using the object name or class name




# we can also make functions inside the class
# these functions are called methods
# class housedesign:
#     colour="white"
#     price=50000

#     def details(self):                      # method
#         print (f"The colour of the house is {self.colour} and price is {self.price}")

# notice how we have used self parameter
# self parameter is used to refer to the current object
# we have to use self parameter in every method of the class

# h3=housedesign()
# h3.details()



# class employsignup:
#     company="regex"
#     c_mail="regex@gmail.com"
#     turnover="100cr"


#     def inform (self):
#         print("employee details",self.c_mail,self.c_mail.split("@")[1])

# e1=employsignup()
 # e1.inform()






