

# exception handelling :-

    # exception is an event when occured will disturb the flow of the program
    # sometimes they are also called unwanted events
    # we go with exceptional handelling to tackle this
    # there are two blocks that helps tackle it :- try and except



# try :                   # we write our main code in the try block
#     print("hey")
#     a=100
#     print(b)
#     print("end")         # if error occured the remaining try block doesnt run

# except:                  # here we write the code that handle it
#     print("handle error")       # this will run if any error occur in the try block


# but we dont know what cause error 
# to tackle this we use  "except as :" 
# there is a class called exception that has all types of errors defined in it 



# we write it as :-

# try :                   
#     print("hey")
#     a=100
#     print(b)
#     print("end")         

# except Exception as abc :
#     print("handle error",abc)           # abc will show you the type of error




# it is a good habit to only define the error that you expect to happand

# try :                   
#     print("hey")
#     a=100
#     print(b)
#     c=10//0
#     print("end")         

# except (NameError,IndentationError) as abc :            # this  will check only two errors that we can expect are most likely to occur
#     print("handle error",abc)

# except Exception as x :                                 # this will check all the errors in case any unexpected error occur
#     print("Handle all exceotions ::",x)




# we can also use nested try/except :-

# try:
#     a=10
#     try:
#         b=0
#         print(a/b)
#     except:
#         print("inner error")
    
#     print("output is here")

# except:
#     print("OUTER ERROR")


# remember except will not tell you which error occured it will just run the except block as soon as an error occur
# but except (exceptions) as (name) will give the name of the error to (name) 
# and we can later print it inside this same block to see the error type



# we can also use else with try :-

# try :                   
#     print("hey")
#     a=100
#     # print(b)
#     # c=10//0
#     print("end")   
# except:
#     print("error occured")
# else:
#     print("Ended with no error")

# if there is any error in try block except block runs
# but if ther is no error in the try block then the else block will be executed
# also we can only write one else block with on try
# IRL the else block is rarely used 




# there is another block called finally 
# it will always run weather there is an error or not 


# try :                   
#     print("hey")
#     a=100
#     print(b)
#     c=10//0
#     print("end")   
# except:
#     print("error occured")
# else:
#     print("Ended with no error")
# finally:
#     print("I will always run bitch")





# there is another keyword called RAISED 
# which raises any error you want
# we use it when user entered data is undesirable or incompatable


# account = 15000
# amount = int(input("Enter n:"))
# try:
#     if(amount>account):
#         print("Account can be opened")
#     else:
#         print("Account cant be opened")
#         raise ValueError
# except:
#     print("Value is less than 15k")