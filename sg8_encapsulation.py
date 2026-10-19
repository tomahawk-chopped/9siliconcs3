class BankAccount:
    def __init__(self, account_number: int, balance: float):
        # Initialize private attributes using setters for validation
        self.account_number = account_number
        self.balance = balance

    # Getter for account_number
    @property
    def account_number(self):
        return self._account_number

    # Setter for account_number
    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    # Getter for balance
    @property
    def balance(self):
        return self._balance

    # Setter for balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("The balance must be not be a negative number.")
        else:
            self._balance = value


# --- Demonstration matching the Sample Output ---

# Create an object of class BankAccount
a1 = BankAccount(12345, 1000)

# Display initial account details
print("Output:")
print()
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

# Attempt to update balance to a negative number
print()
print("Update balance to -100")
a1.balance = -100

# Display account details to verify balance was not changed
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")
