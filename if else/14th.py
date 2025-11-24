#  Q14 Write a program that categorizes a given age into different groups:
#  Infant (0-1 year)
#  Toddler (2-4 years)
#  Child (5-12 years)
#  Teenager (13-19 years)
#  Adult (20-59 years)
#  Senior (60 years and above)


age = int(input("Enter your age:"))

if(age < 0):print("Please enter a valid age")
elif(age <= 1): print("Infant")
elif(age <= 4):print("Toddler")
elif(age <= 12):print("Child")
elif(age <= 19):print("Teenager")
elif(age <= 59):print("Adult")
else:print("Senior")