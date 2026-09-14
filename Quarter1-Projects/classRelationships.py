class Equipment:
    """Tracks sports equipment details and status."""
    def __init__(self, equipment_id: str, name: str, condition: str = "Good"):
        self.equipment_id = equipment_id
        self.name = name
        self.condition = condition
        self.is_available = True

    def __repr__(self):
        return f"Equipment({self.equipment_id}, '{self.name}', condition='{self.condition}', available={self.is_available})"


class Borrower:
    """Tracks borrower details and checked-out equipment references."""
    def __init__(self, borrower_id: str, name: str):
        self.borrower_id = borrower_id
        self.name = name
        self.borrowed_equipment = []  # Stores references to Equipment objects

    def check_out(self, equipment: Equipment):
        if equipment.is_available:
            equipment.is_available = False
            self.borrowed_equipment.append(equipment)
            print(f"[{self.name}] successfully checked out {equipment.name}.")
        else:
            print(f"[{equipment.name}] is currently unavailable.")

    def return_item(self, equipment: Equipment):
        if equipment in self.borrowed_equipment:
            equipment.is_available = True
            self.borrowed_equipment.remove(equipment)
            print(f"[{self.name}] returned {equipment.name}.")
        else:
            print(f"[{self.name}] does not have {equipment.name}.")

    def __repr__(self):
        items = [eq.name for eq in self.borrowed_equipment]
        return f"Borrower({self.borrower_id}, '{self.name}', items={items})"


# --- Test Run Execution ---
if __name__ == "__main__":
    # Create Equipment Instances
    ball = Equipment("EQ01", "Basketball", "Excellent")
    bat = Equipment("EQ02", "Baseball Bat", "Good")

    # Create Borrower Instance
    player = Borrower("B101", "Alex Morgan")

    # Execute Checkout
    player.check_out(ball)
    player.check_out(bat)

    # Output States
    print("\n--- Current State ---")
    print(player)
    print(ball)
    print(bat)
