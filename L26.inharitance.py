
# inharitance in Python:-

    # it is a mechanism or feature of OOPS where a new class can be derived from an existing class
    # the existing class is called base class or parent class or super class
    # the new class is called derived class or child class or sub class
    # the derived class inherits the properties and methods of the base class
    # it makes code reusability possible
    # it makes the code more organized and manageable



# class regexeduhub:          # parent class
#     profit = "10cr"
#     founder = "Tushar Goyal"

# class regexsoftware(regexeduhub):    # child class inheriting parent class:               
#     employees = 5000


# # now the child class regexsoftware has access to the properties of parent class regexeduhub
# print(regexsoftware.profit)        # accessing parent class variable using child class
# regexsoftware.founder = "Tushar Goyal Updated"    # updating parent class variable

# print(regexsoftware.founder)      # accessing updated parent class variable using child class
# print(regexeduhub.founder)        # accessing parent class variable using parent class

# notice how the changes made to parant using the child class does not reflect in the parent class 





# class tatamoter:
#     cars = 2000
#     revenue = 400

#     def details(self):
#         print(f"Tata motors has sold {self.cars} cars and revenue is {self.revenue} crores")

# class tataharrier(tatamoter):
#     price = "25 lakhs"

# tata1 = tataharrier()
# print(tata1.cars)
# t2=tatamoter()
# t2.details()
# tatamoter.details(t2)




# class tatamoter:
#     cars = 2000
#     revenue = 400

#     def details(self):
#         print(f"Tata motors has sold {self.cars} cars and revenue is {self.revenue} crores")

# class tataharrier(tatamoter):
#     price = "25 lakhs"

#     def infoharrier(self):
#         print(f"Tata Harrier is priced at {self.price} ")
    
# th1=tataharrier()
# th1.details()
# th1.infoharrier()



# you cant call the parant methods inside the child class normally 
# but there is keyword called super() which is used to access the properties and methods of the parent class inside the child class



# class tatamoter:
#     cars = 2000
#     revenue = 400

#     def details(self):
#         print(f"Tata motors has sold {self.cars} cars and revenue is {self.revenue} crores")

# class tataharrier(tatamoter):
#     price = "25 lakhs"

#     def infoharrier(self):
#         print(f"Tata Harrier is priced at {self.price} ")
#         super().details()        # accessing parent class method using super() function
    
# th1=tataharrier()
# th1.infoharrier()







# class customer :
#     def __init__(self,name,email,wallet):
#         self.name=name
#         self.email=email
#         self.wallet=wallet
    
#     def info(self):
#         print(f"Customer name ==> {self.name} :: email ==> {self.email} :: and wallet balance ==> {self.wallet}")

# class driver(customer):
#     def __init__(self, a,b,c):
#         super().__init__(a,b,c)

# d1=driver("isha","isha@gmail.com",5000)
# d1.info()







# make a class and make a method that prints hi
# make another class that has same named method that prints hello
# make a third class that inharits both classes(a,b)
# and run those two methods using the object of third class
# then change the order of inharitance and see the difference
# it is called multiple inharitance 
# read about it



# class first :
#     def f1(self):
#         print("hey")
    
# class second:
#     def f1(self):
#         print("hello")

# class third (first,second):
#     def f2(self):
#         print("bitch")

# o1=third()
# o1.f1()             # if we had writter f1 is place of f2 in class third then it would print bitch


# there is a technical term for it called MRO(Method Resolution Order):-
    # it says that in case of multiple inharitance the method of first inharited class will be given preference
    # the child class will look for method in itself first then in first parent class then in second parent class and so on





# class a :
#     def __init__(self):
#         print("inside class a")
        
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("inside class b")

# b1=b()          # see how the parent class constructor is called when super() keyword is read by compiler then the remaining child class constructor is executed
