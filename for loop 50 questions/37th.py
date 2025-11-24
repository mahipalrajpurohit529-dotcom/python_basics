# 37.Given the string s = "aaabbbccc" compress consecutive characters and print the
# result as "a3b3c3" using a for loop.

s = "aaabbbccc" 
cp=""

for x in s:
    if(x not in cp):
        print(f"{x}{s.count(x)}",end="")
        cp+=x