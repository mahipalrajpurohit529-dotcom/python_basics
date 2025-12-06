

"""
syntax

if(condition):
    code in if
    code in if
    
else:
    code in else 
    code in else


if(condition):
    code in if
code outside if  #it is outside because it starts with same line as "if" 

# we dont end the if else in python like we do in c. In python we simply just start writting without the indentation
# the 4 space (or tab) we leave is called as indentation
    

other way:-

if(codition): code
else: code

"""




#Q. write a prigram to check if a number is divisible by both 2 and 3 

n = 13746

if(n%2 == 0 and n%3 == 0): 
    print("Divisible by both 2 and 3")
else :
    print=("Not divisible by 2 and 3")





#Q. write a program to check if a number is even as well as not divisible by 4 then print the number else print false

a=18
if(a%2==0 and a%4 != 0):
    print(a)
else :
    print("condition is false")


#Q. write a program to check if the number is not divisible by 3 and grreater than 70 then print condition is true else print condition is false

b=24

if(b%3 != 0 and b>70):
    print("condition is true")
else:
    print("Condition is false")





"""
else if in python is => elif

"""

num = 5

if(num > 10): print("Number is greater than 10")
elif(num > 5): print("Number is greater than 5")
elif (num == 5): print("Number is 5")
else:print("Number is less than 5")


#Q. number divisible by 2 then print divisible by 2 and if the number is divisible by 3 print it is divisible by 3

new = 5

if(new%2 == 0): print("The number is divisible by 2")
elif(new%3 == 0):  print("The number is divisible by 3")
else: print("not divisible")


#Q. take the salery as a variable . if the salery is more than 3k print good salery , if greater than 7k pront high salery and if 15k then very high salery otherwise low salery

salery = 12343

if(salery>15000):print("very high salery")
elif(salery>7000):print("high salery")
elif(salery>3000):print("good salery")
else: print("low salery")



#Q. if a number is divisible by 2 ,divisible by 3 and divisible by both and divisible by  none

q=123

if(q%2 == 0 and q%3==0): print("divisible by both")
elif(q%2 == 0): print("divisible by 2")
elif(q%3==0): print("divisible by 3")
else:print("divisible by none")



# nested if else works just fine just like in c 
# but beware of the indentations

#Q. if a number is less then 27 then print condition is false otherwise check if it is divisible by 2 . if yes
#   then print both conditions are true otherwise say only one condition is true

l=1234

if(l>27):
    if(l%2 == 0):print("both conditions are true")
    else: print("Only one condition is true")
else:print("condition is false")




#Q. leap year

year = 2024

if(year%100 == 0):
    if(year%400 == 0):print("leap year")
    else: print("not a leap year")
else:
    if(year%4 == 0): print("leap year")
    else: print("not a leap year")





