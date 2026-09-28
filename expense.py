class Expense:

    def __init__(
        self,
        expense_id,
        amount,
        category,
        description,
        date
    ):
        self.expense_id = expense_id
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):

        return {
            "id": self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):

        return Expense(
            data["id"],
            data["amount"],
            data["category"],
            data["description"],
            data["date"]
        )
