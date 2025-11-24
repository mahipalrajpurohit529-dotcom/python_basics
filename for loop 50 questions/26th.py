# 26. Given the list primes = [2,3,5,7,11,13,17], print all primes that are two-digit numbers
#     using a for loop.

primes = [2,3,5,7,11,13,17]

for i in primes:
    if(i//10!=0):
        print(i)
