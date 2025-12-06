# it is a machenism where we can read or write data of a file for latter use
# it can be used to handle file for reading and writing purpose 

#open()
#operator(read/write)
#close


# open (read,write,read/write)

# f = open("data.txt")   # this allows you to read the file 
                         # by default it is 'r' mode which allows you to read

# print(f.read())
# f.close

# f=open("data.txt",'w')      # the 'w' mode allows you to add data to the file but the allready axisting data will be override
# f.write("tushar")
# f.close()


# f=open("data2.txt",'w')     #if no such file exist then the w mode will create a new file
# f.write("chal bhagg")
# f.close()

# but r mode lets you only read and w mode only let you write 
# we use r+ mode to both togher
# the r+ mode doesnt override anything but rather just add new data

# f= open("data.txt","r+")
# print(f.read())
# f.write("ja na be")
# f.close()


# f= open("data.txt","r+")
# f.write("ja na be")
# print(f.read())             # here you see that the output is just ja na be but  the r+ mode doesnt override so it should also include hey hello niqqa
# f.close()                   # this happens because it depends on curser position 
#                             # BEWARE: when we add new data our curser changes its positon


#  there is also w+ mode which will do the same thing for us but 'w' always override


# now in the w+ or r+ mode the position of the curser is very crucial
# but we dont always know the position of the curser
# so we have other ways to find the position of the curser 

# tell function:-


# f= open("data.txt","r+")
# print(f.read())
# print(f.tell())
# f.write("ja na be")
# print(f.tell())
# f.close()


# we can also change the location of curser using the seek function:-


# f= open("data.txt","r+")
# f.seek(1)           # this will send your curser to 1st index
# print(f.tell())
# print(f.read())
# f.close()


# there also a mode called 'a' mode which only appends the data at the end



# this was the old syntax and not much used now a days 
# the new way :-

# with open ("data.txt","w") as f:        # this same as f=open() and close()
#     f.write("my name is mahipal")       # whateven we do in here will be done and when we do outside it closes the file automatically







# functions of file handelling :-


# with open ("data.txt","r") as f:       
#         x=f.read(2)             # this reads two bites (one english chr is one byte)
#         print(x)   


# with open ("data.txt","r") as f:       
#         x=f.readline()          # this will read first          
#         print(x)   



# but what if we had 100 line and we needed to read them all?
# we use loops :-

# with open ("data.txt","r") as f:       
#         for a in f:
#             print(a) 

# but loops will run on all the data and wont give us the control
# so we use maps 


# with open ("data2.txt","r") as f:       
#         mylist=f.readlines()          # this will read all lines and return them as list      
#         ourmap=map(lambda x :x.split(" ")[1],mylist) 
# print(next(ourmap))
# print(next(ourmap))

import csv          # csv is comma separated values(or data)

f = open("csv.txt","r")
f_csv = csv.reader(f)

for line in f_csv:
    print(line)
    for data in line:
        print(data)