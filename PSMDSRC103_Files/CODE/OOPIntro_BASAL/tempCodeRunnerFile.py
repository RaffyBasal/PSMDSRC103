from accounts import Accounts
from atm import ATM

# Create an instance of the Accounts class, passing arguments to the constructor
Account1 = Accounts(account_number=123456, account_firstname="Royce",
                    account_lastname="Chua", current_balance=1000,
                    address="Silver Street Quezon City",
                    email="roycechua123@gmail.com")

# Print a header for the first account
print(f"Account 1: {Account1.account_number}")

# Print the attributes of the first account
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

# Create another instance of the Accounts class, passing arguments to the constructor
Account2 = Accounts(account_number=654321, account_firstname="John",
                    account_lastname="Doe", current_balance=2000,
                    address="Gold Street Quezon City",
                    email="johndoe@yahoo.com")

# Print a header for the second account
print()
print(f"Account 2: {Account2.account_number}")

# Print the attributes of the second account
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

print()
print("Account 1")

# Create an instance of the ATM class with a serial number
ATM1 = ATM(serial_number=987654321)

# Deposit 500 into Account1 using the ATM
ATM1.deposit(Account1, 500)

# Check the current balance of Account1
ATM1.check_current_balance(Account1)

# Display the ATM serial number
print(f"\nATM Machine Serial Number: {ATM1.serial_number}")

print()
print("Account 2")
# Deposit 300 into Account2 using the ATM
ATM1.deposit(Account2, 300)

# Check the current balance of Account2
ATM1.check_current_balance(Account2)
print(f"\nATM Machine Serial Number: {ATM1.serial_number}")
print()

print()
print("Account 2")
# Deposit 300 into Account2 using the ATM
ATM1.deposit(Account2, 300)

# Check the current balance of Account2
ATM1.check_current_balance(Account2)

print()
ATM1.view_transactionsummary(Account1)