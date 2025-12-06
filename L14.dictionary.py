
# lists are usually too long and it is harder to find data in it
# so we introduced aanother data type called dictionary
# dictionary is like an index page of your notebook
# dictionaries are mutable
# dictionary saves data in the form of key and value
# the time taken to find a data is :- O(1) #big o of 1

# we use curly braces for dictionary{}

# key are unique and should be of immutable datatype 
# values can be unique as well as duplicate 

# there is no index in dictionary unlike tupple,strings or list


# mydict={104:"ishaa",106:"preksha"}

# to access we use mydict[104]

# print(mydict[104])

# mydict[104]= 3   # way to update
# print(mydict[104])

# mydict[105]="uk"  # if the key doesnt exist in the dictionary it will add a new key and value

# you cant change key of a value directly
# but you can obiously change the value of a key


#to delete we use .pop(key)

# mydict.pop(104)
# print(mydict)




# you can also make keys in string form not just int
# if we make two same keys while making the dictionary then it wont show error 
# but when we try to access that key then the last in sequance will be accessed



# mydict["SALERY"]=45
# print(mydict)

# here the value is 45 and its key is "SALERY"
# always use "" to access a key in string form

# if the value is int we can also perform arithematic operations on it 

# mydict["SALERY"] += 10
# print(mydict)




#Q.change value using loop

# num ={"count":0}
# for i in range (1,11):
#     num["count"] += 1
# print(num)


#Q.

# num ={"count":0}

# for i in range (2,8):
#     k=0
#     for j in range (2,i):
#         if(i%j==0):
#             k=1
#             break
#     if(k==0):
#         num["count"]+=1

# print(num)



#Q.

# nums = "rajulala"
# mydict={"cold":0}
# vowels="aeiou"

# for i in range (0,len(nums)):
#     if(nums[i] in vowels):
#         mydict["cold"]+=1
# print(mydict)



#Q.
# mydict={100:"ram",101:"shyam",102:"gopal",103:"gala"}

# if(100 not in mydict):
#     print(mydict[100])
# else:
#     print(mydict[101])

# if(102 not in mydict):
#     print(mydict[102])
# else :
#     print(mydict[103])





#Q add charactors of a string as key and their index as their value to a new dictionary

# data = "abdgdhuaickjhaiy"
# mydict={}

# for i in range (0,len(data)):
#     mydict[data[i]]=i
# print(mydict)



#Q. find index of c

# data = "abdgdhuaickjhaiy"
# mydict={}

# for i in range (0,len(data)):
#     mydict[data[i]]=i

# print(mydict['c'])





# Q. add a string to a dictionary with charactors as keys and 1 as value 


# data = "hey ram"
# d={}

# for i in range (0,len(data)):
#    d[data[i]]=1
# print(d)




#Q.add vowels of a string to a dictionary 


# data = "hey ramuel"
# d={}
# vowel="aeiouAEIOU"

# for i in data :
#     if(i in vowel):
#         if(i not in d):
#             d[i]=1
#         else:
#             d[i] += 1
# print(d)






# s="(){}[]"
# var=[]
# ind="valid"

# for x in s:
#     if( x=='(' or x=='[' or x == '{' ):
#         var.append(x)

#     elif(len(var)>0):
    
#         if(x == ')' and '('==var.pop()):
#             ind="valid"
#         elif(x==']' and '['==var.pop()):
#             ind="valid"
#         elif(x=='}' and '{'==var.pop()):
#             ind="valid"
#         else:
#             ind="invalid"
#             break
        
#     else:
#         ind="invalid"
#         break

# if(len(var)>0):print("invalid")
# else:print(ind)




# Q.

# list = [10,20,5,145,54,8]
# d={}

# for i in range (0,len(list)):
#     d[list[i]]=i
# print(d)




#Q.two sum problem

# mylist=[2,3,7,8,9,46]
# d={}
# target=12

# for i in range (0,len(mylist)):
#     d[mylist[i]]=i
# print(d)

# for i in mylist:
#     y = target-i

#     if(y in d):
#         print(i,y,d[y])



# Q. valid paranthesis

s="])"
var=[]
ind="valid"

for x in s:
    if( x=='(' or x=='[' or x == '{' ):
        var.append(x)

    elif(len(var)>0):
    
        if(x == ')' and '('==var.pop()):
            ind="valid"
        elif(x==']' and '['==var.pop()):
            ind="valid"
        elif(x=='}' and '{'==var.pop()):
            ind="valid"
        else:
            ind="invalid"
            break
        
    else:
        ind="invalid"
        break

if(len(var)>0):print("invalid")
else:print(ind)
