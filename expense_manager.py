"""
expense_manager.py
Functions to manage expense records: adding, finding, editing, deleting,
and filtering expenses.
Author: Pragya Singh
"""


def generate_new_id(expenses: list[dict]) -> int:
    """Find the highest existing ID and return the next number."""
    if not expenses:
        return 1

    max_id = 0
    for expense in expenses:
        if expense["id"] > max_id:
            max_id = expense["id"]

    return max_id + 1


def add_expense(
    expenses: list[dict],
    date: str,
    category: str,
    amount: float,
    description: str,
) -> dict:
    """Create a new expense entry and append it to the expenses list."""
    new_id = generate_new_id(expenses)
    new_expense = {
        "id": new_id,
        "date": date,
        "category": category,
        "amount": round(amount, 2),
        "description": description,
    }
    expenses.append(new_expense)
    return new_expense


def find_expense_by_id(expenses: list[dict], expense_id: int) -> tuple[dict | None, int]:
    """Search for an expense by ID. Returns (record, index) or (None, -1)."""
    for index in range(len(expenses)):
        if expenses[index]["id"] == expense_id:
            return expenses[index], index
    return None, -1


def search_by_category(expenses: list[dict], category_query: str) -> list[dict]:
    """Find all expenses where category contains the query (case-insensitive)."""
    query = category_query.strip().lower()
    matches = []
    for expense in expenses:
        if query in expense["category"].lower():
            matches.append(expense)
    return matches


def search_by_date(expenses: list[dict], date_query: str) -> list[dict]:
    """Find expenses matching an exact date (YYYY-MM-DD) or month (YYYY-MM)."""
    query = date_query.strip()
    matches = []
    for expense in expenses:
        if expense["date"].startswith(query):
            matches.append(expense)
    return matches


def filter_by_min_amount(expenses: list[dict], min_amount: float) -> list[dict]:
    """Return all expenses with an amount greater than or equal to min_amount."""
    matches = []
    for expense in expenses:
        if expense["amount"] >= min_amount:
            matches.append(expense)
    return matches


def update_expense(
    expenses: list[dict],
    expense_id: int,
    new_date: str | None = None,
    new_category: str | None = None,
    new_amount: float | None = None,
    new_description: str | None = None,
) -> bool:
    """Update fields of an existing expense record. Returns True if updated."""
    expense, _ = find_expense_by_id(expenses, expense_id)
    if expense is None:
        return False

    if new_date is not None:
        expense["date"] = new_date
    if new_category is not None:
        expense["category"] = new_category
    if new_amount is not None:
        expense["amount"] = round(new_amount, 2)
    if new_description is not None:
        expense["description"] = new_description

    return True


def delete_expense(expenses: list[dict], expense_id: int) -> bool:
    """Remove an expense record by ID. Returns True if found and removed."""
    _, index = find_expense_by_id(expenses, expense_id)
    if index != -1:
        expenses.pop(index)
        return True
    return False


def get_unique_categories(expenses: list[dict]) -> set[str]:
    """Collect all unique category names used across expenses."""
    categories = set()
    for expense in expenses:
        categories.add(expense["category"])
    return categories
