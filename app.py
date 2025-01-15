import csv
from datetime import datetime

# File to store expenses
file_name = "expenses.csv"


# Function to add an expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (e.g., Food, Transport): ")
    date = input(
        "Enter date (YYYY-MM-DD, leave blank for today): "
    ) or datetime.now().strftime("%Y-%m-%d")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added!")


# Function to view all expenses
def view_expenses():
    print("\nDate       | Category       | Amount")
    print("-" * 30)
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<10} | {row[1]:<13} | ${row[2]:>7}")


# Function to calculate total expenses
def calculate_total():
    total = 0
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[2])
    print(f"\nTotal Expenses: ${total:.2f}")


# Menu
def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Initialize file
with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)
    if file.tell() == 0:  # If file is empty, add headers
        writer.writerow(["Date", "Category", "Amount"])

# Start the program
menu()
