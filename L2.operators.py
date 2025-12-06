
#operators are symbols that perform some specific work
# 1+5
# + is operator and 1 and 5 are opeands

"""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""






"""
1.Arithematic operators :-

+	    Addition	        x + y	
-	    Subtraction	        x - y	
*	    Multiplication	    x * y	
/	    Division	        x / y	   normal true division
%	    Modulus	            x % y	
**	    Exponentiation	    x ** y	   x raised to the power of y
//	    Floor division	    x // y     intiger division(gives answer in pure int)

"""

#if in an operation one data type is int and other is float then the answer will be in float

# 20+6/2*5-1
# the answer is 34.0 which is in float
# 20+6-1+3**2*2

# ** has higher presidence and will be executed and calculated before others

# 20*3//2+6


"""
presidency in python 

exponent multiply divide floor division modulus

addition subtraction

"""
# also the second line those who come first will be solved first from left to right

# usually those which have same precidency are calculated from left to right
# but in ** the once on the right are calculated fist
# eg => 2**3**2 will be calculated as 3^2=9 and then 2^9=512 





"""
2.comparision operators 
- they return boolen value


==	    Equal	                        x == y	
!=	    Not equal	                    x != y	
>  	    Greater than	                x > y	
<	    Less than                	    x < y	
>=  	Greater than or equal to	    x >= y	
<=	    Less than or equal to	        x <= y	


"""




"""
3.Assignment operator :-

=	       x = 5	        x = 5	
+=	       x += 3	        x = x + 3	
-=	       x -= 3	        x = x - 3	
*=	       x *= 3	        x = x * 3	
/=	       x /= 3	        x = x / 3	
%=	       x %= 3	        x = x % 3	
//=	       x //= 3        	x = x // 3	
**=	       x **= 3        	x = x ** 3



if a = 5
and we print (a+4)
it will give 9 as answer 
but a will remain as 5

## you can only change the value of a variable using assignment operator ##

"""





"""
4.Logical operators:-

and 	Returns True if both statements are true	                    x < 5 and  x < 10	
or	    Returns True if one of the statements is true	                x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true     	not(x < 5 and x < 10)

you can ofc use as many ands or ors as you want 

if a = 10
=> a>3 or a>5 and a>15
=>(a>3) or (a>5 and a>15)
=> a>3 or false
=> true or false
=> true


or has higher presidency that means we solve ands first and then we check them by conparin with ors
 we can simple put () on whole statements on both sides of all ors


"""


"""
5.Membership operators

- used to check if any data belongs to a string,list,tupple,dictionary or not
- Membership operators are used to test if a sequence is presented in an object:

in   	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	        Returns True if a sequence with the specified value is not present in the object	x not in y

- checks if x is a member of y or not


"""






"""
6.Identity operators

- used to compare variables based on memory address
- we use id(x) to check memory address of x

is 	          Returns True if both variables are the same object	    x is y	
is not	      Returns True if both variables are not the same object	x is not y

- it manely checks the memory address of two variables


- 'is'  is not same as ==
==   checks if the value of two variables is same or not
is   checks if the memory address of two variables is same or not


- if values of variables are small then memory address is same for two variables
  but for larger values it wont be same 


"""







"""
7.Bitwise operators:-

As we know everything works in binary language or bits
everything can be written in the zero or one format

we write 0-15 in 4 blocks

---- ---- ---- 8421
write 5        0101

0101 is code for 5 because we add 4 and 1 to get 5 so we write 1 under them 
and since we dont use 8 or 2 ,we write 0 under them

other eg => 13  8421
                1101

so the code for 13 is 1101


# If we write a number larger then 15 then we use the second block

----  ----  128,64,32,16   8,4,2,1

this should allow us to write till 255 and as for higher numbers, we use the next block and so on




# The bitwise operators operate on the bits 







1. AND operator (&)

- set a bit to 1 if both bits are 1

- eg => 5 & 8 
                 8 4 2 1
             5=> 0 1 0 1     4+1=5
             8=> 1 0 0 0     8 = 8
           ans=> 0 0 0 1     

so 5 and 8 is 0001 which is code for 1

hence 5&8 = 1





2. bitwise "OR" operator (|)

- sets a value to 1 if either of the values is 1

- eg => 7 or 4

                8 4 2 1
            7 =>0 1 1 1     4+2+1=7
            4 =>0 1 0 0     4 = 4
          ans =>0 1 1 1

so 7 or 4 is 0111 which is code for 7

- hence 7 or 4 = 7






3.

"""

