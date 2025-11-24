# Q8 Write a program that checks if a username and password entered by the user match the pre-set values
# username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
# "Login Failed".

username = "admin"
password = "1234"

a = input("Enter your username:")
b = input("Enter your password: ")

if(a == username and b == password):print("Ligin susseccful")
else:print("Login failed")



