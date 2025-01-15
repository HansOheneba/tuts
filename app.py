import csv
from datetime import datetime
import matplotlib.pyplot as plt

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


def plot_expenses():
    dates = []
    amounts = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
            amounts.append(float(row[2]))

    if not dates or not amounts:
        print("\nNo expenses to plot!")
        return

    # Sort dates and amounts for proper plotting
    sorted_data = sorted(zip(dates, amounts))
    dates, amounts = zip(*sorted_data)

    # Plotting the graph
    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker="o", linestyle="-", color="b")
    plt.title("Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()


# Menu
def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Plot Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            plot_expenses()
        elif choice == "5":
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
