from storage import load_budget, save_budget


class Budget:

    def __init__(self):

        self.monthly_budget = load_budget()


    def set_budget(self, amount):

        if amount <= 0:
            return False

        self.monthly_budget = amount

        save_budget(amount)

        return True


    def remaining_budget(self, total_expenses):

        return (
            self.monthly_budget
            - total_expenses
        )


    def budget_status(self, total_expenses):

        if self.monthly_budget == 0:

            return "Budget has not been set."


        remaining = self.remaining_budget(
            total_expenses
        )


        if remaining > 0:

            return (
                f"Rs. {remaining:.2f} "
                "remaining."
            )


        elif remaining == 0:

            return "Budget fully used."


        else:

            return (
                f"Budget exceeded by "
                f"Rs. {abs(remaining):.2f}."
            )
