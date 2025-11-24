# 10.Write a program to enter a number and print its reverse.

n = input("Enter thr number:")

count = len(n) - 1

while(count >= 0):
    print(n[count],end="")
    count -= 1



