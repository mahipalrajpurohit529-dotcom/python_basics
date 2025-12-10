# it is feature of OOPS where we try to hide unwanted details from the user


# class rbiloan:
#     amount=50000
#     def intrest(self):
#         print("we have 5% intrest rate ")
    
# class hdfcloan(rbiloan):  
#     tenure=7
#     def intrest(self):
#         print("we have 10% intrest rate ")

# h1=hdfcloan()
# h1.intrest()


# here the customer has nothing to do with how much loanrate rbi gives
# because user is taking loan from hdfc
# so why should we show it to the user ?
# user doesnt need it 
# so we hide it and it is called abstraction

# to achive abstraction we create a class called abstract class
# it is a class where we define an abstract method
# we declare it but dont implement it

# the above eg is not an eg of abstraction 
# to create the abstract class we need abc package




from abc import ABC,abstractmethod            # abc => package  ,  ABC => abstract base class
                                            # every abstract class will inharit abstract base class


class rbiloan(ABC):     # abstract class which inharit ABC
    amount=50000
    
    @ abstractmethod                # this is a decorator whose work is to change the behavior of a method without changing the code
    def intrest(self):          #abstract method
        pass

# remember we cant make an object of an abstract class


class hdfcloan(rbiloan):  
    tenure=7
    def intrest(self):              # we must always create this method (abstract) in the child otherwise it will show error
        print("HDFC has 10% intrest rate ")

class sbi(rbiloan):     # second child of abstract class rbiloans
    tenure = 10

    def intrest(self):      # must always be created even if we only write pass in it
        pass

h1=hdfcloan()
h1.intrest()

s1=sbi()
s1.intrest

# only use abstraction when a function of parant must always be used by all child classes
# child class must always implement the parant class abstract method 
# the abstract class work as a blueprint for all child class






# we read about three types of vars :- class,instance and local
# mehods are also of three types 



# classmethod ,staticmethod and isinstancemethod:-

# Difference between Instance Method, Class Method, and Static Method

class Example:
    class_variable = "I belong to the class"

    # 1️⃣ Instance Method
    # - Most common type
    # - Takes 'self' as first parameter
    # - Can access instance variables + class variables
    def instance_method(self):
        return "This is an Instance Method. I can access: " + self.class_variable

    # 2️⃣ Class Method
    # - Takes 'cls' as first parameter
    # - Can only access class-level data, not object(instance) data
    # - Often used for factory methods (creating objects in different ways)
    @classmethod
    def class_method(cls):
        return "This is a Class Method. I can access: " + cls.class_variable

    # 3️⃣ Static Method
    # - No 'self' or 'cls'
    # - Doesn't access class or instance variables
    # - Behaves like a normal function inside class (just grouped logically)
    @staticmethod
    def static_method():
        return "This is a Static Method. I cannot access class or instance variables."


# obj = Example()

# print(obj.instance_method())   # Called using object
# print(Example.class_method())  # Called using class
# print(Example.static_method()) # Called using class

# Summary:
# Instance Method -> Access instance + class data (uses self)
# Class Method    -> Access only class data (uses cls)
# Static Method   -> No access to instance/class data (no self/cls)




class a:
    def f1(self):        # instance method 
        print("hy from f1")
    
    # def f2 ():          # this is not exactly static 
    #     print("hey")

    @staticmethod
    def f2():       # static
        print("hey from staticmethod")

    @staticmethod
    def f3(x,y):    # also static with parameters
        print("hey from ",x,y)

    @classmethod
    def f4(cls):        #class method 
        print("hey from cls",cls)


# self => object reference
# cls => class reference

a1=a()
a1.f1

a1.f2()
a.f2()
a1.f3(10,20)
a1.f4()
a.f4()
    
