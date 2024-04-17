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
    grocery_system.add_item("Apple", 10)
    grocery_system.add_item("Banana", 15)
    grocery_system.add_item("Orange", 20)
    grocery_system.add_item("Mangos",30)
    grocery_system.display_inventory()
    grocery_system.update_quantity("Apple", 5)
    grocery_system.remove_item("Banana")
    grocery_system.display_inventory()
