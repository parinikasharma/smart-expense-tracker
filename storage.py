import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

EXPENSE_FILE = DATA_DIR / "expenses.json"
BUDGET_FILE = DATA_DIR / "budget.json"


def load_expenses():

    DATA_DIR.mkdir(exist_ok=True)

    if not EXPENSE_FILE.exists():
        return []

    try:

        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):

        return []


def save_expenses(expenses):

    DATA_DIR.mkdir(exist_ok=True)

    with open(EXPENSE_FILE, "w") as file:

        json.dump(
            expenses,
            file,
            indent=4)


def load_budget():

    DATA_DIR.mkdir(exist_ok=True)

    if not BUDGET_FILE.exists():
        return 0

    try:

        with open(BUDGET_FILE, "r") as file:

            data = json.load(file)

            return float(
                data.get("budget", 0)
            )

    except (json.JSONDecodeError, FileNotFoundError):

        return 0


def save_budget(amount):

    DATA_DIR.mkdir(exist_ok=True)

    with open(BUDGET_FILE, "w") as file:

        json.dump(
            {"budget": amount},
            file,
            indent=4
        )
