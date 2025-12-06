# generators are the special type of iterators that yield items one at a time and only when requested.
# they are defined using functions and the 'yield' keyword.
# generators are memory efficient because they generate items on-the-fly and do not store the entire sequence in memory.
# they are commonly used for large datasets or infinite sequences where storing all items would be impractical.



# def func():
#     print("this is first line ")
#     return 1



# normal function use return to give back a value and exit the function but 
# the generator uses yield to give back a value and pause the function state


def func():
    print("this is first line ")
    yield 1
    print("this is second line ")
    yield 2
    print("this is third line ")
    yield 3


gen=func()          # this will give the generator object
print(next(gen))    # this will run the function till the first yield and give back the value 
                #remeber that this function will print as well as return the value (like using print and return both in normal function)
print(next(gen))    # this will resume the function from where it left and run till next yield or end of function
print(next(gen))    # this will resume the function from where it left and run till next yield or end of function
# print(next(gen))    # this will give error as there is no more yield or return

# the generators remember where they left off and continue from there on subsequent calls to next()
# also the yeild stops the compiler at their location and when we call next() it resumes from there
# it can be very helpfull when used inside a loop


# generators have some functions like
# send() :- it sends a value to the generator(to yeild) and resumes its execution
# throw() :- it raises an exception inside the generator at the point where it was paused(just like manually adding raise statement)
# close() :- it terminates the generator and raises a StopIteration exception inside it