# 35. Given text = "a b c d e" replace every space with "-" and print the new string using a
# for loop.


text = "a b c d e"
newtext=""

for i in range (0,len(text)) :
    if(text[i]==' '):
        newtext+='-'
    else:
        newtext+=text[i]
    
print(newtext)

