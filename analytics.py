from collections import defaultdict


def category_summary(expenses):

    summary = defaultdict(float)

    for expense in expenses:
        summary[expense["category"]] += expense["amount"]

    return dict(summary)


def highest_expense(expenses):

    if not expenses:
        return None

    return max(
        expenses,
        key=lambda expense: expense["amount"]
    )


def average_expense(expenses):

    if not expenses:
        return 0

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    return total / len(expenses)
