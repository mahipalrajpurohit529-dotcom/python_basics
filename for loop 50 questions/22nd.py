# 22.Given a string sentence = "this is a test" count and print the number of words using a
#    for loop (assume words are separated by single spaces).

sentence = "this is a test"

count = 0

for i in sentence:
    if(i != ' '):count += 1
print(count)