
"""
STRING 

- contains a lot of charactors 
- position of a charactor is called as index
- indexing starts from 0 then goes onwards
- we also have negative indexing

eg = "MAHIPAL"

index of M = 0
index of A = 1

index of L = 6 as well as -1 (which is 6-7)
- last character is (total charectors - 1)


to check a charactor at a index we use

#  print( a[3] )






- SLICING

- it is extracting some portion of data
- syntax => [starting : ending : step]

- default value of step is = 1 , so it is not neccesory to write it every time unless you want to change it
- if we dont give starting or ending value they start from 0 and goes till the last charector by default
- remember that ending itself is not included

if we write [0:3]
you would think it gives 0,1,2,3
but its not true 
this only gives the value 0,1,2

- hence the end index itself is not included


-if we change step size then it skips some charactor as you could easily guess

eg=>

m = "MAHIPAL"
print(m[0:7:2])
ans=> 'MHPL'

- you can give step size in negative but then remember that the starting position should be higher than the ending
- [0:5:-1] wont give any result
- [5:0:-1] will give result




- when you use both negative ending and negative starting then remember your step size is still +1
- so [-1 : -4] will not give you any result
- but [-4 : -1 ] will give you result
- also [-1 : -4 : -1] will give you result


- just remember that you can manuplate it however you wish but the range and step size matter


- # if step size is negative then it starts from the ending and goes to start
- [0:6:-1] will start from 5th index and will go to 4,3,2,1,0








"""


