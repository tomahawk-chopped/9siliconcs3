MANGAOANG, KARL   IX - SILICON

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
