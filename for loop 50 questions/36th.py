# 36.Given the list seq = [1,2,3,4,5], print all possible pairs (i, j) where i comes before j
# using nested for loops.


seq = [1,2,3,4,5]

for i in range(0,len(seq)):
    for j in range(i+1,len(seq)):
        print(i,j)



