import json
from datetime import datetime

# File to store expense data
expense_file = "expenses.json"

# Function to load expenses from file
def load_expenses():
    try:
        with open(expense_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save expenses to file
def save_expenses(expenses):
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add an expense
def add_expense(amount, category, description):
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

# Function to view expenses by month
def view_monthly_expenses():
    expenses = load_expenses()
    monthly_summary = {}
    
    for expense in expenses:
        month = expense["date"][:7]  # YYYY-MM
        monthly_summary.setdefault(month, 0)
        monthly_summary[month] += expense["amount"]

    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

# Function to view expenses by category
def view_category_expenses():
    expenses = load_expenses()
    category_summary = {}
    
    for expense in expenses:
        category = expense["category"]
        category_summary.setdefault(category, 0)
        category_summary[category] += expense["amount"]

    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

# Function to prompt user for input and handle different actions
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount spent: $"))
                category = input("Enter category (e.g., Food, Transport): ")
                description = input("Enter a brief description: ")
                add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        
        elif choice == "2":
            view_monthly_expenses()
        
        elif choice == "3":
            view_category_expenses()
        
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
