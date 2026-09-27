"""
validation.py
Input validation helpers for dates, amounts, and user choices.
Author: Pragya Singh
"""


def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year."""
    # Leap year rule: divisible by 4, not by 100 unless also divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def validate_amount(amount_str: str) -> tuple[bool, float | str]:
    """Validate that the entered amount is a positive number."""
    cleaned = amount_str.strip()
    if not cleaned:
        return False, "Error: Amount cannot be empty."

    try:
        val = float(cleaned)
    except ValueError:
        return False, "Error: Amount must be a valid number (e.g. 150 or 49.50)."

    if val <= 0:
        return False, "Error: Amount must be strictly greater than zero."

    # Keep two decimal places for rupees and paise
    return True, round(val, 2)


def validate_date(date_str: str) -> tuple[bool, str]:
    """
    Validate that a date string is in YYYY-MM-DD format and has valid calendar values.
    Also handles leap years for February.
    """
    cleaned = date_str.strip()
    if not cleaned:
        return False, "Error: Date cannot be empty."

    parts = cleaned.split("-")
    if len(parts) != 3:
        return False, "Error: Date format must be YYYY-MM-DD (e.g. 2026-09-28)."

    year_str, month_str, day_str = parts

    # All three parts must be numeric
    if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
        return False, "Error: Year, month, and day must contain digits only."

    if len(year_str) != 4 or len(month_str) != 2 or len(day_str) != 2:
        return False, "Error: Date must have 4-digit year, 2-digit month, and 2-digit day (YYYY-MM-DD)."

    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        return False, "Error: Unable to parse date numbers."

    # Realistic range for student expense records
    if year < 2000 or year > 2099:
        return False, "Error: Year must be between 2000 and 2099."

    if month < 1 or month > 12:
        return False, "Error: Month must be between 01 and 12."

    # Days in month: index 0 unused, 1=Jan (31), 2=Feb (28), etc.
    days_in_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    max_days = days_in_month[month]
    if month == 2 and is_leap_year(year):
        max_days = 29

    if day < 1 or day > max_days:
        return False, f"Error: Day must be between 01 and {max_days:02d} for month {month:02d}."

    return True, f"{year:04d}-{month:02d}-{day:02d}"


def validate_non_empty(text: str, field_name: str = "Input") -> tuple[bool, str]:
    """Check that user input is not blank or just spaces."""
    cleaned = text.strip()
    if not cleaned:
        return False, f"Error: {field_name} cannot be empty."
    return True, cleaned


def validate_menu_choice(choice_str: str, min_choice: int, max_choice: int) -> tuple[bool, int | str]:
    """Validate that the menu option entered is an integer within the allowed range."""
    cleaned = choice_str.strip()
    if not cleaned:
        return False, "Error: Choice cannot be empty."

    try:
        choice = int(cleaned)
    except ValueError:
        return False, f"Error: Please enter a valid number between {min_choice} and {max_choice}."

    if choice < min_choice or choice > max_choice:
        return False, f"Error: Invalid option. Please choose between {min_choice} and {max_choice}."

    return True, choice
