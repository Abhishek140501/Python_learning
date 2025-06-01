#  Expense Tracker (Python CLI)

A simple command-line **Expense Tracker** built with Python that allows users to add expenses, view them, calculate total expenses, and filter by category — all using functional programming concepts like **lambda**, **map**, and **filter**.

##  Features

- ➕ **Add Expenses** with amount and category.
- **List All Expenses** in a readable format.
- **Show Total Expenses** using `lambda` and `map`.
- 🔍 **Filter Expenses by Category** using `lambda` and `filter`.
-  **Exit Program** safely.

##  Concepts Used

- **Functions** and **control flow**
- **Lambda expressions**
- **`map()` and `filter()` functions**
- **Dictionaries** and **lists**
- **While loops** and **user input**

## 🛠️ How It Works

Run the Python script:

```bash
python expense_tracker.py

Then follow the menu:

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit

📂 Example

Enter your choice: 1
Enter amount: 50
Enter category: Food

Enter your choice: 3
Total Expenses: 50.0

Sample Code Snippet
python

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

Future Improvements:

Save/load expenses to/from a file (e.g., using json)

Add dates to expenses

GUI or web interface

Export reports