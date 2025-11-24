# Q3 Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100
# unless it is also divisible by 400.

year = int(input("Enter the year: "))

if(year%100 == 0):
    if(year%400 == 0): print("Leap year ")
    else:print("Not leap")
else:
    if(year%4 == 0):print("Leap year")
    else:print("Not leap")

    