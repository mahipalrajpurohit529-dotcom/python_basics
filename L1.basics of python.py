
"""python :-
- interpretor based
- develoment is easy
- begginer friendly
- syntax is easy

used in :- 

- data science , data enginering and data analysis
- web development - django,flask , bottle 
- software development - tkinter
- automation and testing - selenium , pyautogui(library)
- hacking """


#in python we use print and not printf 
#print("hello world")

#this will print hello world 

""" when we use two prints in two lines they print the text continues in c
 but in python they directly start in new line 
 because in python the default value of end = "\n"
 end is basically the code with which your line ends
 we can change that value of end"""

#print("hello", end =" a " )
#print("world ")
#print("guyz")

#notice how the second print function still has \n as end value by default

#you can also make your string varaible multi lined using triple quotes
#so that it will always be printed in multiple lines 

m = """hi
i am 
mahipal"""

print(m)

"""if you want to print multiple things in python you just do them with a comma 
print("hello","world","bitch")
you can use comma as many times as you wish
the two text in the same print are separated by space " " by default 
 you can change that using sep = "" function"""

# print("hello","world",sep = "-")



# in c we used format specifiers to print variables
#  and gave data types while declaring a variable
#  but in python we can just declare variables simply
 
x = 45  #here x is an integer type data
y = "hello"  #here y is a string type data
z = "234"   #here z is also string type data

#you can use either of double or single quotes to make strings

# we can use  print(type(variable name))  to check the type of data in a variable

#print(type(x))

#to print a variable you write it outside the double inverted commas 

#print("the value of z is ",z)
#print("the value of z is ",z,"and the value of x is",x)

"""notice how we have to use double inverted commas again and again
this could be very furstrating work
 to avoid this we can use f in the print just before double strings
 f stands for formating and in that pertical string whatever you write will be 
 printed and you can specify a character to be treated as a variable by using {}
"""

#print(f"the value of x is {x} and the value of z is {z}")


