# 45.Given list numbers = [11,22,33,44,55], create and print a new list where each
# element is the original element minus the previous element (for the first element,
# subtract 0).

numbers = [11,22,33,44,55]
newlist=[]

sub=0

for x in numbers:
    newlist.append(x-sub)
    sub=x
print(newlist)
