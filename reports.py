from analytics import category_summary
import csv


def generate_report(expenses):

    print("\n")
    print("=" * 45)
    print("          EXPENSE REPORT")
    print("=" * 45)


    if not expenses:

        print("No expenses available.")

        print("=" * 45)

        return


    total = sum(
        expense["amount"]
        for expense in expenses
    )


    print(
        f"Total Expenses: "
        f"Rs. {total:.2f}"
    )


    print("\nCategory-wise Spending:")


    summary = category_summary(
        expenses
    )


    for category, amount in summary.items():

        print(
            f"{category}: "
            f"Rs. {amount:.2f}"
        )


    print("=" * 45)


def export_to_csv(expenses):

    if not expenses:

        print(
            "No expenses available "
            "to export."
        )

        return


    with open(
        "expense_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)


        writer.writerow([
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ])


        for expense in expenses:

            writer.writerow([
                expense["id"],
                expense["amount"],
                expense["category"],
                expense["description"],
                expense["date"]
            ])


    print(
        "Report exported successfully "
        "as expense_report.csv"
    )
