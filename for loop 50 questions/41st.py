# 41.Given the string s = 'MixEdCase', count uppercase and lowercase letters separately
# using a for loop and print both counts.


s = 'MixEdCase'

up=0
low=0

for x in s :
    if(x==x.upper()):
        up+=1
    else:
        low+=1
print(up,low)