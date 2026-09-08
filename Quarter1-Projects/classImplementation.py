class Equipment:
    def __init__(self, item_name: str, unit_price: float, is_available: bool, quantity: int):
        self.item_name = item_name
        self.unit_price = unit_price
        self.is_available = is_available
        self.__quantity = quantity  # Private attribute

    # Method 1: Reads/returns private attribute safely
    def get_quantity(self) -> int:
        return self.__quantity

    # Method 2: Takes a parameter and modifies a private attribute safely
    def update_quantity(self, amount: int):
        if self.__quantity + amount >= 0:
            self.__quantity += amount
            if self.__quantity == 0:
                self.is_available = False
            else:
                self.is_available = True
        else:
            print(f"Error: Cannot reduce quantity below 0 for {self.item_name}.")

    # Method 3: Reads object details
    def display_details(self):
        print(f"Item: {self.item_name} | Price: ${self.unit_price:.2f} | Available: {self.is_available} | Stock: {self.__quantity}")


# --- Step 6: Instantiate Two Objects ---
item1 = Equipment("Baseball Bat", 45.00, True, 10)
item2 = Equipment("Soccer Ball", 25.00, True, 15)

# --- Step 8: Produce a Test Run ---
print("--- BEFORE ---")
item1.display_details()
item2.display_details()

print("\nPerforming action on Object 1 (Updating quantity by -10)...")
# --- Step 7: Change Only One Object ---
item1.update_quantity(-10)

print("\n--- AFTER ---")
item1.display_details()
item2.display_details()
