
# map:-
    # map is a high order function which is used to run(itterate) a loop on list,tupple or string
    # it is just like a loop that takes a function and an itterable from us 
    # performs function on each item of itterable and returns the value
    # it always return the value in the form of the inputed itterable
    # syntax :- 
    #        map(function,itterable)

# Eg=>

# nums = [1, 2, 3]
# result = map(lambda x: x * 2, nums)

# print(next(result))   




# # difference between map and for loop :-

# # for loop execute a code at the same time(imediately)     but     map run a code on demand

# # mylist=[80,55,64]

# # for i in mylist:
# #     print(i*10)    

# # # it creates and run the code for all the i and if we want to access it later then we have to store it in another variable
# # but it will take a lot of memory


# # a=map(len , ["regexhi","regex","hi"])
# # print(a)            # this will give you memory address and it wont access the data unless we ask it 
# #                     # it is called as lazy evaluation
# #                     # this saves memory unlike the for loop
                    

# # # we use "next" function to do the evaluation and call the function

# # print(next(a))          # this only gives you the len of "regexhi" because of the lazy evaluation 
# # print(next(a))          # now it prints the len of next item of itterable
# # print(next(a))          # now it prints the len of the last element

# # print(next(a))          # now it shows error as there is  no data in the itterable anymore because we have accessed it all 
# #                         # this error is called as 'stop itteration' error




# # eg=>

# def custom (num):
#     return(num**3)

# # print(custom(4))

# mylist = [5,8,10,64]

# x = map(custom,mylist)   # it is memory address
# print(next(x))


# # there is a function called 'list" that will run the whole map again and again 

# a=list(map(custom,mylist))        # this expression will create a list called a with every element having gone through map
# print(a)


# # we have seen two ways to call the map elements (one using next other using list function)
# # there is another way using for loop :-

# for i in x :
#     print(i)    # you can notice it doesnt work for first element because we accessed it earlier


# short way :-

# x = map(lambda a :a**3,[10,34,13,17])
# for i in x :
#     print(i)

# # even shorter way :-

# y = list(map(lambda a :a**3,[10,34,13,17]))
# print(y)






# there is a function called filter that filters the list and gives it to you

# mylist = [2,45,23,66,8,16]
# a=list(filter(lambda x :x%2==0,mylist))    #this(filter)0 will only work if the expression of lambda is boolean or comparision 
# print(a)            # this prints even number





# learning assignment :-
# generators,why we use it and how are they different from normal functions
# exceptional handelling