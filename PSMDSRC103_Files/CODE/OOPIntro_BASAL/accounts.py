"""
Accounts.py
"""

class Accounts:
     def __init__(self, account_number=0, account_firstname="", account_lastname="", current_balance=0.0, address="", email=""):
        # Initializing the class with the parameters
        self.account_number = account_number
        self.account_firstname = account_firstname
        self.account_lastname = account_lastname
        self.current_balance = current_balance  # This line is essential
        self.address = address
        self.email = email
    # use to identify a certain accounts to be called
        def update_address(self, new_address):
            self.address = new_address  # Use self to modify the object's attribute

        def update_email(self, new_email):
            self.email = new_email  # Use self to modify the object's attribute