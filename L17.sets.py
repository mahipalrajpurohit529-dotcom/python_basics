
# SETS


# set is a data type in python 
# it collects unique values
# it is mutable
# it has no indexing
# they are not ordered
# they are used to perform mathematical operations
# combine to results (like union  and intersection )


myset = set({})    # empty set

# set(nameoflist)  # to convert a list into a set

marks = {10,20,30,10,10}   #this is the way to write a set 

print(marks)     # notice how it ignores the repeted marks


marks.add(80)    # adding single elements
print(marks)

marks.update([110,30,25,26])    # adding multiple values using iterable
print(marks)

othermarks = {110,34,56,78,92,46}    # other section of class


print(marks.union(othermarks))   # adding two sets to print
print(marks.intersection(othermarks))   # intersection of two sets

# we can also assign the union or intersection to either of the variables or another variable 
# or we can simply print these like above


marks.intersection_update(othermarks)  # updating marks (the first variable)   marks = anb
print(marks)


print (marks.symmetric_difference(othermarks))

# check these out :- 

# Symmetric Difference : aUb - anb
# difference_update :  a = a - anb
# issubset 
# isdisjoint




# Q. print unique words



s = "hey i am here i"
x=s.split(" ")

p = set(x)
print(p)


