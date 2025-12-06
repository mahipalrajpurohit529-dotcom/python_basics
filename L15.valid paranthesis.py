# Q. valid paranthesis

s="([])"
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




