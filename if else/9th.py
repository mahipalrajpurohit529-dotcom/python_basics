# Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
# triangle. A triangle is valid if the sum of any two sides is greater than the third side.
# Check conditions like a + b > c, b + c > a, and a + c > b.


a = int(input("Enter the  first side of triangle:"))
b = int(input("Enter the second side of triangle:")) 
c = int(input("Enter the third side of the triangle:"))


if(a+b>c and b+c>a and c+a>b): print("Valid triangle")
else:print("Invalid triangle")

