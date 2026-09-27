"""
data.py
Data storage and starter dataset for the expense tracker.
Saves and loads records using local JSON files.
Author: Pragya Singh
"""

import json
import os

# Default categories commonly used by students
DEFAULT_CATEGORIES: tuple[str, ...] = (
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Entertainment",
    "Bills",
    "Other",
)

EXPENSES_FILE = "expenses.json"
BUDGET_FILE = "budget.json"


def get_sample_expenses() -> list[dict]:
    """Starter sample expenses from campus life to test the tracker right away."""
    return [
        {
            "id": 1,
            "date": "2026-09-02",
            "category": "Education",
            "amount": 1200.00,
            "description": "Semester reference textbooks and stationery",
        },
        {
            "id": 2,
            "date": "2026-09-05",
            "category": "Food",
            "amount": 350.00,
            "description": "VIT food court lunch with hostel friends",
        },
        {
            "id": 3,
            "date": "2026-09-08",
            "category": "Travel",
            "amount": 220.00,
            "description": "Auto fare to Katpadi railway station",
        },
        {
            "id": 4,
            "date": "2026-09-12",
            "category": "Bills",
            "amount": 499.00,
            "description": "Monthly high-speed mobile data recharge",
        },
        {
            "id": 5,
            "date": "2026-09-15",
            "category": "Entertainment",
            "amount": 300.00,
            "description": "Weekend movie ticket",
        },
        {
            "id": 6,
            "date": "2026-09-18",
            "category": "Shopping",
            "amount": 850.00,
            "description": "Replacement scientific calculator and bag",
        },
        {
            "id": 7,
            "date": "2026-09-22",
            "category": "Food",
            "amount": 180.00,
            "description": "Evening snacks and juice at Gazebo",
        },
        {
            "id": 8,
            "date": "2026-09-25",
            "category": "Education",
            "amount": 450.00,
            "description": "Lab record notebook and project printouts",
        },
    ]


def load_expenses(filepath: str = EXPENSES_FILE) -> list[dict]:
    """Load expense records from JSON. If missing or invalid, load sample data."""
    if not os.path.exists(filepath):
        initial_data = get_sample_expenses()
        save_expenses(initial_data, filepath)
        return initial_data

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return get_sample_expenses()
    except (json.JSONDecodeError, OSError):
        # Fallback to sample data if file is unreadable or empty
        return get_sample_expenses()


def save_expenses(expenses: list[dict], filepath: str = EXPENSES_FILE) -> bool:
    """Save the expense list to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError:
        return False


def load_budget(filepath: str = BUDGET_FILE) -> float:
    """Load monthly budget from JSON file. Default is 5000.00."""
    if not os.path.exists(filepath):
        default_budget = 5000.00
        save_budget(default_budget, filepath)
        return default_budget

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict) and "monthly_budget" in data:
                return float(data["monthly_budget"])
            return 5000.00
    except (json.JSONDecodeError, OSError, ValueError):
        return 5000.00


def save_budget(budget_amount: float, filepath: str = BUDGET_FILE) -> bool:
    """Save the monthly budget to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump({"monthly_budget": round(budget_amount, 2)}, file, indent=4)
        return True
    except OSError:
        return False
