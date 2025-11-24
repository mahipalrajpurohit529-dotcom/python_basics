# 44,Given text = 'abracadabra', print the index positions of each occurrence of the letter
# 'a'; using a for loop.

text = 'abracadabra'

for i in range (0,len(text)):
    if(text[i]=='a'):
        print(i)