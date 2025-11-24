# 20. Print all characters of the string="Data" reversed using a for loop (do not use reversed() or slicing).

string='data'

for i in range (len(string)-1,-1,-1):
    print(string[i])