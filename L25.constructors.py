# constructors in Python:-

# it is a method which is used to initialize the memory address for the object
# it is created using a special method called __init__()
# it always runs when an object of the class is created
# constructor is like an enginear who makes changes to the blueprint before making the house

# class read():
#     def __init__(self):
#         print("This is constructor of read class")
#     def display(self):
#         print("This is display method of read class")
    
# # if we define an objeect using this class the  constructor will be called automatically and the message will be printed
# r1=read()      # constructor called here
#                # but when we assign the object the other method will not be called automatically





# class housedesign:
#     colour="white"
#     price=50000

#     def __init__(self):             # constructor method(always defined with this name)
#         print("This is constructor method called automatically when object is created")

# print(housedesign())     # when we create the object the constructor is called automatically
# h1=housedesign()   # again creating object will call the constructor again




# SELF keyword :-
        # it is the first parameter of the constructor which refers to the current object of the class
        # self is a keyword that store current object address(refference)
        # it creates instance variables for the object
        # instance variables are variables that are unique to each object 
        # and can be accessed only by that object and not even the class itself

# class housedesign:
#     def __init__(self,a,b):             # constructor method(always defined with this name)
#         self.colour=a              # instance variable
#         self.price=b                 # instance variable

# h1=housedesign("red",60000)
# print(h1.colour)            # accessing instance variable using object

# h2=housedesign("blue",70000)
# print(h2.price)             # accessing instance variable using object


# but you see we have a lot of variables for each object
# that is why we usually make the same type of variable 
# we should have written colour and price in place of a and b to make things easy








# class new :
#     a=0

# v1=new()
# print(f"old value of a is {v1.a} and  old value of new.a is {new.a}")
# v1.a=5
# print(f"new value of a is {v1.a} and  new value of new.a is {new.a}")

# notice how changing v1.a did not change new.a 
# that is because v1.a is an instance variable unique to object v1 
# and changing the instance variable does not change the class variable



class simple:
    x=0             # class variable which can be accessed by all objects or methods of the class
    def __init__(self):
        simple.x += 1         

a1=simple()
print(a1.x)           
a2=simple()
print(a2.x)


# notice how the value of x is changing for every object
# that is because x is a class variable and is accessed using the class name inside the constructor
# so every time an object is made the constructor runs and increases the value of x by 1
# and since x is a class variable the change is reflected for all objects



# but if the chages were made using object name then the changes would have been unique to that object only

a1.x=10
print(a1.x)
a3=simple()
print(a3.x)



# also if we had used self.x in place of simple.x in the constructor,then also the changes would have been unique to that object only


class valuecount:
    x = 0           # this is a class variable which can be accessed by all objects or the methods of the class
    def __init__(self):
        self.x += 1          # this is an instance variable which is unique to each object

v1 = valuecount()
print(v1.x)            # accessing instance variable using object
                    # accessing instance variable using object
v2 = valuecount()
print(v2.x)            # accessing instance variable using object







# types of constructors :-
    # 1. Default constructor :- which takes no parameters
    # 2. Parameterized constructor :- which takes parameters

