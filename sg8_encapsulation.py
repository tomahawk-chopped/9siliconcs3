class BankAccount:
    def __init__(self, account_number: int = 0, balance: float = 0.0):
        # Private attributes (indicated by double underscores in Python)
        self.__account_number = account_number
        self.__balance = 0.0
        
        # Initialize balance through setter logic to enforce positive balance rule
        self.set_balance(balance)

    # --- Setter Methods ---
    def set_account_number(self, account_number: int) -> None:
        """Setter for account number."""
        self.__account_number = account_number

    def set_balance(self, balance: float) -> None:
        """Setter for balance with validation against negative values."""
        if balance < 0:
            print("Warning: Balance cannot be negative. Update ignored.")
        else:
            self.__balance = float(balance)

    # --- Getter Methods (using @property decorator) ---
    @property
    def get_account_number((self) -> int:
        """Getter for account number."""
        return self.__account_number

    @property
    def get_balance(self) -> float:
        """Getter for balance."""
        return self.__balance


# --- Demonstration of Usage ---
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount()

    # Utilize public setter methods
    account.set_account_number(1001234567)
    account.set_balance(1500.75)

    # Display values using getter methods decorated with @property
    print("--- Account Information ---")
    print(f"Account Number: {account.get_account_number}")
    print(f"Formatted Balance: ${account.get_balance:,.2f}")

    # Attempt setting a negative balance to trigger the warning
    print("\n--- Testing Invalid Input ---")
    account.set_balance(-250.00)

    # Verify that the balance remained unchanged
    print(f"Current Formatted Balance: ${account.get_balance:,.2f}")
