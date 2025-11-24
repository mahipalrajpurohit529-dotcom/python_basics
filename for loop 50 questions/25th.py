# 25. Given text = "Level" check (using a for loop and case normalization) whether the text
#     is a palindrome and print Palindrome or Not palindrome


text = "Level"
end = len(text)-1
ind = "palindrome"

for i in range (0,len(text)):
    if(text[i] != text[end]):
        ind="not palindrome"
        break
    end-=1
print(ind)