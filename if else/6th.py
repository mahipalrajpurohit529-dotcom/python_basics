# Q6. Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and
# performs the specified operation. Print the result based on the operation.

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

o = input("Enter the operation(a,s,m,d) you wish to conduct:")

if(o == 'a'): print(f"The sum of {a} and {b} is {a+b}")
elif(o == 's'): print(f"The subtraction of {a} and {b} is {a-b}")
elif(o == 'm'): print(f"The multiplication of {a} and {b} is {a*b}")
elif(o == 'd'): 
    if(b != 0):print(f"The division of {a} and {b} is {a/b}")
    else:print("Division by zero is not possible")
else: print(f"please make sure operation is valid(a,s,m,d)")


