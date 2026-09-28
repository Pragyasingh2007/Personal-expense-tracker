"""
budget.py
Budget evaluation and monthly expense filtering.
Author: Pragya Singh
"""


def evaluate_budget(budget: float, total_spent: float) -> dict:
    """
    Compare spending against monthly budget and return status details.
    Status can be UNDER_BUDGET, EXACT_BUDGET, or OVER_BUDGET.
    """
    budget = round(budget, 2)
    total_spent = round(total_spent, 2)
    difference = round(budget - total_spent, 2)

    if budget > 0:
        percentage_used = round((total_spent / budget) * 100.0, 2)
    else:
        percentage_used = 0.0

    if total_spent < budget:
        status = "UNDER_BUDGET"
        message = (
            f"Within budget: you have spent INR {total_spent:.2f} of INR {budget:.2f}. "
            f"Remaining balance: INR {difference:.2f} ({100.0 - percentage_used:.1f}% remaining)."
        )
    elif total_spent == budget:
        status = "EXACT_BUDGET"
        message = (
            f"Budget reached exactly: you have spent INR {total_spent:.2f} of INR {budget:.2f}. "
            f"Remaining balance: INR 0.00."
        )
    else:
        status = "OVER_BUDGET"
        overspent = abs(difference)
        message = (
            f"Budget exceeded: you have spent INR {total_spent:.2f}, which is over "
            f"the budget of INR {budget:.2f} by INR {overspent:.2f} ({percentage_used:.1f}% used)."
        )

    return {
        "budget": budget,
        "total_spent": total_spent,
        "difference": difference,
        "percentage_used": percentage_used,
        "status": status,
        "message": message,
    }


def filter_expenses_by_month(expenses: list[dict], year_month: str) -> list[dict]:
    """Filter expenses for a specific month (format: YYYY-MM)."""
    monthly = []
    for exp in expenses:
        if exp["date"].startswith(year_month):
            monthly.append(exp)
    return monthly
