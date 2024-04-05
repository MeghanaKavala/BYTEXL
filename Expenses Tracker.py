# Function to add a new expense
def add_expense(transactions, date, category, amount, description):
    transactions.append((date, category, amount, description))
    print("Expense added successfully.")

# Function to view expenses by category
def view_expenses_by_category(transactions, category):
    for transaction in transactions:
        if transaction[1] == category:
            print(transaction)

# Function to calculate total expenditure over a specified period
def calculate_total_expenditure(transactions, start_date, end_date):
    total = 0
    for transaction in transactions:
        if start_date <= transaction[0] <= end_date:
            total += transaction[2]
    return total

def main():
    transactions = []  # List to store transactions
    while True:
        print("\nExpense Tracking System:")
        print("1. Add new expense")
        print("2. View expenses by category")
        print("3. Calculate total expenditure over a specified period")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(transactions, date, category, amount, description)

        elif choice == "2":
            category = input("Enter category to view expenses: ")
            print("Expenses under category", category, ":")
            view_expenses_by_category(transactions, category)

        elif choice == "3":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            total_expenditure = calculate_total_expenditure(transactions, start_date, end_date)
            print("Total expenditure between", start_date, "and", end_date, ":", total_expenditure)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
