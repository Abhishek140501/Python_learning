# 💰 Budget App

This project is a **budget management app** written in Python. It includes a `Category` class that helps you manage finances by allowing you to deposit, withdraw, and transfer money across various budget categories such as `Food`, `Clothing`, and `Entertainment`. Additionally, a function `create_spend_chart` generates a bar chart representing spending percentages across the categories.

---

## 📂 Project Structure

budget_app/
│
├── budget.py # Contains Category class and create_spend_chart function
└── README.md # Project documentation

---

## 🧠 Features

### ✅ Category Class
- **Instantiate** budget categories (e.g. Food, Clothing).
- **Deposit** money into a category.
- **Withdraw** money from a category if funds are sufficient.
- **Transfer** money from one category to another.
- **Check Funds** available in a category.
- **View Ledger** with formatted string output showing transactions and balance.

### ✅ Spending Chart
- Generate a **text-based bar chart** showing percentage of total spending per category.
- Categories are displayed vertically at the bottom of the chart.
- Spending is calculated only from withdrawals.

---

## 📘 Example Usage

```python
from budget import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing, entertainment]))

🖥️ Sample Output

*************Food*************
Initial deposit        1000.00
Groceries               -10.15
Restaurant              -15.89
Transfer to Clothing    -50.00
Total: 923.96

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  E  
     o  l  n  
     o  o  t  
     d  t  e  
        h  r  
        i  t  
        n  a  
        g  i  
           n  
           m  
           e  
           n  
           t  
🛠️ Requirements
Python 3.x

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Abhishek Anand

If you found this helpful, feel free to ⭐ the repository!