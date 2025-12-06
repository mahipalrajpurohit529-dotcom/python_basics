
# Q.for n=8 print:-
# *        
# * *
# * - *
# * - - *
# * - - - *
# * - - - - *
# * - - - - - *
# * * * * * * * *



# n=int(input("Enter n:"))

# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if (j<=i):
#             if(j==1 or i==j or i==n):print("*",end=" ")
#             else:print("-",end=" ")
#         else:print(" ",end="")
#     print("")








# Q. for n = 8 print :-
    
# * * * * * * * * 
# * - - - - - *
# * - - - - *
# * - - - *
# * - - *
# * - *
# * *
# *
    

# n=int(input("Ener n:"))

# for i in range (n,0,-1):
#     for j in range (1,n+1):
#         if (j<=i):
#             if(j==1 or i==j or i==n):print("*",end=" ")
#             else:print("-",end=" ")
#         else:print(" ",end=" ")
#     print("")


n = int(input("Enter n:"))
for i in range (1,n+1):
     for j in range (n,0,-1):
         if(j<=i):
            print("*",end="*")
         else:print("-",end="")
     print("")