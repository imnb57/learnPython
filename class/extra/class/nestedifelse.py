balance = 5000
print('Welcome to ATM!')
print('1.Balance Inquiry')
print('2.Withdraw Cash')
print('3.Deposit Cash')
print('4.Exit')

choice = int(input('Please enter your choice(1-4):\n'))

if choice ==1:
    print(f'Your current balance is {balance}')

elif choice == 2:
    amount = int(input('Enter the amount to withdraw:\n'))
    if amount>balance:
        print('Insufficient balance')
    else:
        balance -= amount
        print(f"Withdrawl successfull ! Your new balance is :${balance}")
elif choice ==3:
    amount = int(input('Enter the amount to deposit:\n'))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    else:
        balance += amount
        print(f"Deposit successful Your new balance is: ${balance}")
elif choice ==4:
    print('Thank you for using the ATM. Goodbye!')

else:
    print('Invalid choice. Please try again.')