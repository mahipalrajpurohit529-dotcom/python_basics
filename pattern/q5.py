"""
print the pattern :-

E
DE
CDE
BCDE
ABCDE

"""


for i in range (1,6):
    c = 70-i
    for j in range (1,i+1):
        print(chr(c),end="")
        c+=1
    print(" ")



