# list collection of elements 
# it is a data type 
# it is mutable 

#iterable :- it can be any value or datatype on which we can directly run for loop


mylist=[10,200,45.30,"hey","c"]

print(mylist[0]) #print element at 0 index


mylist[3]=600  #update
print(mylist)

mylist[1:3]= [20,30]  #updating multiple index
print(mylist)



# append adds extra item to the end of a list 
# you cannot add multiple items using append

mylist.append (90)
print(mylist)

mylist.append("hey")
print(mylist)


# to add multiple items in a list we use .extend


mylist.extend("abc")  #this will add 3 items a,b,c in mylist
print(mylist)

mylist.extend([12,300,"hi","btc"]) # this is how to add multiple numbers or strrings in a list
print(mylist)


# to delete a data in a list we use .pop
# by default it errase the last data but we can give the index which we want to errase

mylist.pop()
print(mylist)

mylist.pop(0)
print(mylist)

# reverse is a function that reverses the whole list

mylist.reverse()
print(mylist)




#sort is a function that make the list in ascending order
# but it will only work if all the data in the list is of same type 
# if some data is int and some is string it wont work
# float and int are considered to be of same type here

# mylist.sort()
# print(mylist) #it wont work here


a=[3,300,52,67.8,110,-24]
print(a)
a.sort()
print(a)




# count is a function used to count the occurance of any data in the list

print(mylist.count(600)) # it prints 1 because 600 has only one occurance




#insert is a function used to insert a data at the index of your choise 

print(a)
a.insert(1,44) #add 44 at the index 1
print(a)


