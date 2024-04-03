import csv
import datetime
from collections import defaultdict

class BudgetTracker:
    def __init__(self, data_file="budget_data.csv"):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.DictReader(file)
                self.transactions = list(reader)
        except FileNotFoundError:
            self.transactions = []

    def save_data(self):
        with open(self.data_file, 'w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'type']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

    def add_transaction(self):
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        transaction_type = input("Enter type (income/expense): ")

        self.transactions.append({
            'date': date,
            'category': category,
            'amount': amount,
            'type': transaction_type
        })
        self.save_data()
        print("Transaction added!")

    def view_balance(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = income - expenses
        print(f"Current balance: {balance}")

    def view_expenses_by_category(self):
        category_expenses = defaultdict(float)
        for t in self.transactions:
            if t['type'] == 'expense':
                category_expenses[t['category']] += t['amount']

        print("Expenses by category:")
        for category, amount in category_expenses.items():
            print(f"{category}: {amount}")

    def view_spending_trends(self):
        monthly_expenses = defaultdict(float)
        for t in self.transactions:
            if t['type'] == 'expense':
                date_obj = datetime.datetime.strptime(t['date'], '%Y-%m-%d').date()
                month_key = date_obj.strftime('%Y-%m')  # Group by year-month
                monthly_expenses[month_key] += t['amount']

        print("Monthly spending trends:")
        for month, amount in monthly_expenses.items():
            print(f"{month}: {amount}")

    def run_budget_tracker(self):
        print("*** Welcome to the Budget Tracker ***")

        while True:
            print("\nOptions:")
            print("1. Add transaction")
            print("2. View balance")
            print("3. View expenses by category")
            print("4. View spending trends")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_transaction()
            elif choice == '2':
                self.view_balance()
            elif choice == '3':
                self.view_expenses_by_category()
            elif choice == '4':
                self.view_spending_trends()
            elif choice == '5':
                print("Exiting budget tracker...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run_budget_tracker()
