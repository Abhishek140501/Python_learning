class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = sum(item['amount'] for item in self.ledger)
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    spends = []
    total_spent = 0

    for cat in categories:
        spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spends.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 10) * 10 for spent in spends]

    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "|"
        for percent in percentages:
            if percent >= i:
                res += " o "
            else:
                res += "   "
        res += " \n"

    res += "    -" + "---" * len(categories) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        res += "     "
        for cat in categories:
            if i < len(cat.name):
                res += cat.name[i] + "  "
            else:
                res += "   "
        res += "\n"

    return res.rstrip("\n")

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "initial deposit")
food.withdraw(150.25, "groceries")
food.withdraw(50.75, "restaurant")
food.transfer(100, entertainment)
entertainment.withdraw(30)
business.deposit(500)

print(food)
print(create_spend_chart([food, entertainment, business]))
