# Given text = "abracadabra" count how many times the letter &#39;a&#39; appears using a for loop

text = "abracadabra"
count=0

for i in text:
    if(i=='a'):
        count+=1
print(f"the total appearances of latter a is {count}")