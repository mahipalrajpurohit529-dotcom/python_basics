# # 50.Given a string of digits s = '121332441' using for loops only, find and print the
# # length of the longest palindrome substring that is centered at any single character (odd-
# # length palindromes).


# s = '121332441'
# long=0

# for i in range(0,len(s)):
#     for j in range (i,len(s),2):
#         pal=1
#         end=j
#         for k in range (i,j+1):
#             if(s[k]!=s[end]):
#                 pal=0
#                 break
#             end-=1
#         if(pal==1 and long<j+1-i):
#             long=j+1-i
             
# print(long)






# second way:-

# s = '121332441'
# long=0

# for centre in range (0,len(s)):
#     for j in range (0,len(s)):
#         left=centre-j
#         right=j+centre

#         if(left <0 or right>=len(s)):
#             break
#         if(s[left]==s[right]):
#             length=right-left+1
#             if(long<length):long=length
#         else:
#             break
# print(long)









# third  way :-

s = '121332441'
long=0

for centre in range (0,len(s)) :
    temp=1
    for lenght in range (1,len(s)):
        left = centre - lenght
        right = centre + lenght

        if(left<0 or right>=len(s)):
            break
        
        if(s[left]==s[right]):
            temp+=2
        else:
            break
    
    if(long<temp):
        long=temp

print(long)
