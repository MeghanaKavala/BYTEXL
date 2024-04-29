class GroceryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"{quantity} {item}(s) added to inventory.")

    def update_quantity(self, item, new_quantity):
        if item in self.inventory:
            self.inventory[item] = new_quantity
            print(f"Quantity of {item} updated to {new_quantity}.")
        else:
            print(f"Item '{item}' not found in inventory.")

    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]
            print(f"Item '{item}' removed from inventory.")
        else:
            print(f"Item '{item}' not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")


if __name__ == "__main__":
    grocery_system = GroceryManagementSystem()
    while True:
        print("\n1. Add item\n2. Update quantity\n3. Remove item\n4. Display inventory\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            grocery_system.add_item(item, quantity)
        elif choice == "2":
            item = input("Enter item name: ")
            new_quantity = int(input("Enter new quantity: "))
            grocery_system.update_quantity(item, new_quantity)
        elif choice == "3":
            item = input("Enter item name: ")
            grocery_system.remove_item(item)
        elif choice == "4":
            grocery_system.display_inventory()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
