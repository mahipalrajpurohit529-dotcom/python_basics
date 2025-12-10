
# package:-
    # package is just a folder 
    # collection of files



# Encapsulation :- 
#             it is a feature of oops where we combine the variables and methods together
#             inside the class to provide the data accessiblity 
#             or to put limitation on data and for security of data 




# Encapsulation is of 4 types :-

# 1. Public :- 
#              when we create a varaible and then we can use it in any file or
#              folder and then we can use it anywhere in any package

# 2. Private :-
#               when we create a variable which is private to the class (not even object can access it) 
#               then it is called private variable
#               we can create it like :-   private int x = 10
#               made with two underscore (__varname)

# 3. protected :- 
#               protected variable is a variable which can be used only in the class 
#               or in another class with relation to the og class
#               made with one underscore (_varname)


# 4. default (package-protected) :-
#               makes protected by default


# python has none of these 
# but we can make a variable act like them 



# we cant access the private variables normally but we have two functions called getter and setter that allow us to do so
# getter and setter are the methodswhich are used to access or modify the private variables





# class ob:
#     var=10  # act as public 
#     _var1=19    # act as protected

# class ob2(ob):
#     def info (self):
#         print("b value ",ob._var1)

# x = ob2()
# x.info()


# if ob was not father of ob2,we could still have accessed it easily
# but we shouldnt do it 
# we are all adults here and need to do what everyone else is supposed to do 
# so that there are no confusions among the team members




# class company:
#     __salery= 500

# c1=company()

# print(company.__salery)         # not accessible shows error
# print(c1.__salery)


# but we can still access it (never do this btw its just for information)

# class company:
#     __salery= 500
#     def info (self):
#         print(f"varaible accessed {self.__salery}")


# c1=company()
# c1.info()
# print(company._company__salery)     # another way to access it directly

# once again dont do that in real life 
# it would ruin the codes as there are multiple people working on every project




# imp example :-


import random


class bankaccount :
    def __init__(self,user_name,bank_balance):          # remember that even self is local variable 
        self.user_name=user_name
        self.bank_balance=bank_balance
        self.account_number=random.randint(10000000,10099999)
    
    def info(self):
        print(self.user_name,self.bank_balance)
    
    def deposite(self,amount):
        if(amount>0):
            self.bank_balance += amount
        else:
            raise ValueError
    
    def withderaw(self,amount):
        if(self.bank_balance > amount and amount >0):
            self.bank_balance -= amount
        else:
            raise ValueError
        
class saving_account(bankaccount):
    def __init__(self,user_name,bank_balance):
        super().__init__(user_name,bank_balance)

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



b1=bankaccount("mahipal",20000000)
b1.deposite(19999)
b1.info()
b1.withderaw(2000000)
b1.info()


# def deposite(self):
#         self.amount=int(input("Enter the deposite ammount :"))
#         if(self.amount>0):
#             self.bank_balance += self.amount
#         else:
#             raise ValueError



# getter and setter methods for accessing private variable :-

class Student:
    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age     # private variable
    
    # Getter method (to read data)
    def get_age(self):
        return self.__age
    
    # Setter method (to update data safely)
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

obj = Student("Mahipal", 21)
print(obj.get_age())  # Accessing through getter

obj.set_age(22)       # Changing value safely
print(obj.get_age())
