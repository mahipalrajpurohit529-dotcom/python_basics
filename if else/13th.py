# Q13 Write a program that simulates a simple ATM. The user should be able to:
# Check balance
# Deposit money
# Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's

balance = 10000

a = input("what would you like to do(check balance,withdraw,deposit):").lower()

if(a == 'check balance'): print(f"Your current balance is {balance}")

elif(a == 'deposit'):
    deposit = float(input("Enter the amount you want to deposit"))
    if(deposit > 0):
        balance += deposit
        print("Your new balance is",balance)
    else:print("Please make sure the deposite is a valid number ")

elif(a == 'withdraw'):
    withdraw = float(input("Enter the amount you want to withdraw:"))
    
    if(withdraw <= 0): print("Please enter a valid amount to withdraw")
    else:
        if(0 < withdraw <= balance): 
            balance -= withdraw
            print("Your new balance is ",balance)

else:print("Please enter a valid operation")