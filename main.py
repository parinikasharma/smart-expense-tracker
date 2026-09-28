from expense_manager import ExpenseManager
from budget import Budget

from validator import (
    validate_amount,
    validate_category,
    validate_description,
    validate_date
)

from analytics import (
    category_summary,
    highest_expense,
    average_expense
)

from reports import (
    generate_report,
    export_to_csv
)


def add_expense(manager):

    print("\n--- ADD EXPENSE ---")


    amount = input(
        "Enter amount: "
    )


    if not validate_amount(amount):

        print("Invalid amount!")

        return


    category = input(
        "Enter category: "
    )


    if not validate_category(category):

        print(
            "Category cannot be empty!"
        )

        return


    description = input(
        "Enter description: "
    )


    if not validate_description(
        description
    ):

        print(
            "Description cannot be empty!"
        )

        return


    date = input(
        "Enter date (YYYY-MM-DD): "
    )


    if not validate_date(date):

        print(
            "Invalid date! "
            "Use YYYY-MM-DD."
        )

        return


    manager.add_expense(
        float(amount),
        category,
        description,
        date
    )


    print(
        "Expense added successfully!"
    )


def view_expenses(manager):

    expenses = manager.get_all_expenses()


    print("\n--- ALL EXPENSES ---")


    if not expenses:

        print("No expenses found.")

        return


    print("-" * 80)


    for expense in expenses:

        print(
            f"ID: {expense['id']} | "
            f"Amount: Rs. "
            f"{expense['amount']:.2f} | "
            f"Category: "
            f"{expense['category']} | "
            f"Description: "
            f"{expense['description']} | "
            f"Date: {expense['date']}"
        )


    print("-" * 80)


def delete_expense(manager):

    print("\n--- DELETE EXPENSE ---")


    try:

        expense_id = int(
            input(
                "Enter expense ID: "
            )
        )

    except ValueError:

        print(
            "Please enter a valid ID."
        )

        return


    if manager.delete_expense(
        expense_id
    ):

        print(
            "Expense deleted successfully!"
        )

    else:

        print(
            "Expense ID not found."
        )


def search_expense(manager):

    print(
        "\n--- SEARCH BY CATEGORY ---"
    )


    category = input(
        "Enter category: "
    )


    results = manager.search_by_category(
        category
    )


    if not results:

        print(
            "No expenses found "
            "in this category."
        )

        return


    for expense in results:

        print(
            f"ID: {expense['id']} | "
            f"Rs. {expense['amount']:.2f} | "
            f"{expense['description']} | "
            f"{expense['date']}"
        )


def set_budget(budget):

    print(
        "\n--- SET MONTHLY BUDGET ---"
    )


    amount = input(
        "Enter monthly budget: "
    )


    if not validate_amount(amount):

        print("Invalid budget amount!")

        return


    budget.set_budget(
        float(amount)
    )


    print(
        "Monthly budget saved "
        "successfully!"
    )


def show_budget_status(
    manager,
    budget
):

    print(
        "\n--- BUDGET STATUS ---"
    )


    total = manager.get_total_expenses()


    print(
        f"Total Expenses: "
        f"Rs. {total:.2f}"
    )


    if budget.monthly_budget == 0:

        print(
            "Budget has not been set."
        )

        return


    print(
        f"Monthly Budget: "
        f"Rs. {budget.monthly_budget:.2f}"
    )


    print(
        f"Status: "
        f"{budget.budget_status(total)}"
    )


def show_analytics(manager):

    expenses = manager.get_all_expenses()


    print(
        "\n--- EXPENSE ANALYTICS ---"
    )


    if not expenses:

        print("No data available.")

        return


    total = manager.get_total_expenses()


    average = average_expense(
        expenses
    )


    highest = highest_expense(
        expenses
    )


    summary = category_summary(
        expenses
    )


    print(
        f"\nTotal Spending: "
        f"Rs. {total:.2f}"
    )


    print(
        f"Average Expense: "
        f"Rs. {average:.2f}"
    )


    print(
        f"Highest Expense: "
        f"Rs. {highest['amount']:.2f}"
    )


    print(
        f"Highest Category: "
        f"{highest['category']}"
    )


    print(
        "\nCategory-wise Analysis:"
    )


    for category, amount in summary.items():

        print(
            f"{category}: "
            f"Rs. {amount:.2f}"
        )


def main():

    manager = ExpenseManager()

    budget = Budget()


    while True:

        print("\n")
        print("=" * 50)
        print(
            "       SMART EXPENSE TRACKER"
        )
        print("=" * 50)


        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Search by Category")
        print("5. Set Monthly Budget")
        print("6. Check Budget Status")
        print("7. View Analytics")
        print("8. Generate Report")
        print("9. Export Report to CSV")
        print("10. Exit")


        print("=" * 50)


        choice = input(
            "Enter your choice: "
        )


        if choice == "1":

            add_expense(manager)


        elif choice == "2":

            view_expenses(manager)


        elif choice == "3":

            delete_expense(manager)


        elif choice == "4":

            search_expense(manager)


        elif choice == "5":

            set_budget(budget)


        elif choice == "6":

            show_budget_status(
                manager,
                budget
            )


        elif choice == "7":

            show_analytics(manager)


        elif choice == "8":

            generate_report(
                manager.get_all_expenses()
            )


        elif choice == "9":

            export_to_csv(
                manager.get_all_expenses()
            )


        elif choice == "10":

            print(
                "\nThank you for using "
                "Smart Expense Tracker!"
            )

            break


        else:

            print(
                "Invalid choice. "
                "Please try again."
            )


if __name__ == "__main__":
    main()
