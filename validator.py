from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_category(category):
    return bool(category.strip())


def validate_description(description):
    return bool(description.strip())


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False
