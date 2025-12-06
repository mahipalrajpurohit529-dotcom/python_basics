

# lambda function :-
    # it is an annonamous function that has no name 
    # it makes the code simple and readable
    # it is also called as one lined function
    # it doesnt print but return by default

# def sq (num):
#     return(num*num)
# sq(10)

# this above code is way too long by normal way 
# so we will use lambda fnc

# syntax :- lambda parameter, parameter2:expression

# lambda n:n*n  # this is way too easy and simple but it is of no use unless we store it in a variable
# x=lambda n:n*n
# print(x(5))     # gives 25




# high order lambda example :-

# sq=lambda a:a*a
# sq(4)

# cube=lambda x,y : x*y(x)

# print(cube(3,sq))







# def fnc (s):
#     print("string in function:",s)
#     print(s.split(" ")[1])
# fnc ("hey hello user")

# same thing with lambda :-

# x= lambda s: s.split(" ")[-1]
# print(x("hey you bro"))










