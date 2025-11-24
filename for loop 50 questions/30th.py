# 30.Given string s = 'Python3.10', extract and print all digits in the string using a for loop.

s ='Python3.10'

for i in s :
    if(i in "0123456789"):
        print(i)