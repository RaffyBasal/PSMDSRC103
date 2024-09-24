class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []  # Store transaction history

    def __str__(self):
        return f"ATM Machine [Serial Number: {self.serial_number}]"

    # Method to deposit money
    def deposit(self, account, amount):
        account.current_balance += amount
        transaction = f"Deposited {amount} to Account {account.account_number}."
        self.transactions.append(transaction)
        print("Deposit Complete")
    
    # Method to withdraw money
    def withdraw(self, account, amount):
        if account.current_balance >= amount:
            account.current_balance -= amount
            transaction = f"Withdrew {amount} from Account {account.account_number}."
            self.transactions.append(transaction)
            print("Withdraw Complete")
        else:
            print("Insufficient balance")

    # Method to check current balance
    def check_current_balance(self, account):
        print(f"Current balance: {account.current_balance}")

    # Method to view transaction summary and log to a file
    def view_transactionsummary(self):
        # Print transactions to the console
        if self.transactions:
            print("\nTransaction Summary:")
            for transaction in self.transactions:
                print(transaction)
            # Write transactions to a text file
            with open("transaction_log.txt", "w") as f:
                for transaction in self.transactions:
                    f.write(transaction + "\n")
            print("\nTransaction summary logged to transaction_log.txt")
        else:
            print("No transactions made yet.")