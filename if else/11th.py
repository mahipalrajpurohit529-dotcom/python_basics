# Q11 Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.

price = float(input("Enter the price:"))

if(price<500):
    print("No discount ")
    print(f"the final price after discount is {price}")

elif(price<1000):
    print("Discount is 5%")
    print(f"The final price after discount is {0.95*price}")
else:
    print("The discount is 10%")
    print(f"The final price after discount is {0.9*price}")
