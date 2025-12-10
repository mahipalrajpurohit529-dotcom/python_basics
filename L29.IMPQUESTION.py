# class user :
#     def __init__(self,name,email,password):
#         self.name=name
#         self.email=email
#         self.__wallet=0
#         self.__userpassword=password

#     def addmoney(self,amount):
#         if(amount>0):
#             self.__wallet += amount
#             print(f"{amount} money added successfully")

# class customer(user):
#     def __init__(self, name, email,order):
#         super().__init__(name, email)

# class deliver_partner(user):
#     def __init__(self, name,email):
#         super().__init__(name,email)
    
# ob=deliver_partner(1,2)







# smart house example of abstraction :- 

from abc import ABC,abstractmethod

class systemshutdown(ABC):
    @abstractmethod
    def systemoff(self):
        pass

class electricity(systemshutdown):
    def systemoff(self):
        print("Lights off and system is down")

    def runfan(Self):
        print("fan working perfectly")
    

e1=electricity()
e1.runfan()
e1.systemoff()