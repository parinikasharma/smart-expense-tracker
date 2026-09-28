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


# -----------------------------
# VALIDATION TESTS
# -----------------------------

def test_validate_amount():

    assert validate_amount("500") is True
    assert validate_amount("0") is False
    assert validate_amount("-100") is False
    assert validate_amount("abc") is False


def test_validate_category():

    assert validate_category("Food") is True
    assert validate_category("") is False
    assert validate_category("   ") is False


def test_validate_description():

    assert validate_description("Lunch") is True
    assert validate_description("") is False
    assert validate_description("   ") is False


def test_validate_date():

    assert validate_date("2026-09-28") is True
    assert validate_date("28-09-2026") is False
    assert validate_date("invalid") is False


# -----------------------------
# ANALYTICS TESTS
# -----------------------------

def test_category_summary():

    expenses = [
        {
            "id": 1,
            "amount": 100,
            "category": "Food",
            "description": "Lunch",
            "date": "2026-09-28"
        },
        {
            "id": 2,
            "amount": 200,
            "category": "Travel",
            "description": "Bus",
            "date": "2026-09-28"
        },
        {
            "id": 3,
            "amount": 150,
            "category": "Food",
            "description": "Dinner",
            "date": "2026-09-28"
        }
    ]

    result = category_summary(expenses)

    assert result["Food"] == 250
    assert result["Travel"] == 200


def test_highest_expense():

    expenses = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 500},
        {"id": 3, "amount": 200}
    ]

    result = highest_expense(expenses)

    assert result["amount"] == 500


def test_average_expense():

    expenses = [
        {"amount": 100},
        {"amount": 200},
        {"amount": 300}
    ]

    result = average_expense(expenses)

    assert result == 200


print("All project tests completed successfully!")
