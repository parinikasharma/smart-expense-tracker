from expense import Expense
from storage import load_expenses, save_expenses


class ExpenseManager:

    def __init__(self):
        self.expenses = load_expenses()

    def generate_id(self):

        if not self.expenses:
            return 1

        return max(
            expense["id"]
            for expense in self.expenses
        ) + 1

    def add_expense(
        self,
        amount,
        category,
        description,
        date
    ):

        expense_id = self.generate_id()

        expense = Expense(
            expense_id,
            amount,
            category,
            description,
            date
        )

        self.expenses.append(
            expense.to_dict()
        )

        save_expenses(self.expenses)

        return expense

    def get_all_expenses(self):
        return self.expenses

    def delete_expense(self, expense_id):

        for expense in self.expenses:

            if expense["id"] == expense_id:

                self.expenses.remove(expense)

                save_expenses(self.expenses)

                return True

        return False

    def search_by_category(self, category):

        return [
            expense
            for expense in self.expenses
            if expense["category"].lower()
            == category.lower()
        ]

    def get_total_expenses(self):

        return sum(
            expense["amount"]
            for expense in self.expenses
        )
