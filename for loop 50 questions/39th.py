# 39.Given list words = ['red', 'blue', 'green', 'red,'blue'], print each unique word only
# once using a for loop (do not use set()).


words = ['red', 'blue','green', 'red' , 'blue']
new=[]

for x in words :
    if(x not in new):
        new.append(x)
print(new)
