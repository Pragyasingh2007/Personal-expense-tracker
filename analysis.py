"""
analysis.py
Analytical calculations for spending: sums, counts, averages, extremes,
category totals, and bubble sort.
Author: Pragya Singh
"""


def count_expenses(expenses: list[dict]) -> int:
    """Count the total number of expense entries using a loop."""
    count = 0
    for _ in expenses:
        count += 1
    return count


def calculate_total_expense(expenses: list[dict]) -> float:
    """Calculate total spending across all recorded expenses."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return round(total, 2)


def calculate_average_expense(expenses: list[dict]) -> float:
    """Calculate the average spending per transaction."""
    count = count_expenses(expenses)
    if count == 0:
        return 0.0
    total = calculate_total_expense(expenses)
    return round(total / count, 2)


def find_highest_expense(expenses: list[dict]) -> dict | None:
    """Find the single expense with the highest amount."""
    if not expenses:
        return None

    # Start with the first record as current max
    highest_record = expenses[0]
    for expense in expenses[1:]:
        if expense["amount"] > highest_record["amount"]:
            highest_record = expense

    return highest_record


def find_lowest_expense(expenses: list[dict]) -> dict | None:
    """Find the single expense with the lowest amount."""
    if not expenses:
        return None

    # Start with the first record as current min
    lowest_record = expenses[0]
    for expense in expenses[1:]:
        if expense["amount"] < lowest_record["amount"]:
            lowest_record = expense

    return lowest_record


def calculate_category_totals(expenses: list[dict]) -> dict[str, float]:
    """Calculate total money spent in each category."""
    totals: dict[str, float] = {}

    for expense in expenses:
        cat = expense["category"]
        amt = expense["amount"]
        if cat in totals:
            totals[cat] += amt
        else:
            totals[cat] = amt

    for cat in totals:
        totals[cat] = round(totals[cat], 2)

    return totals


def calculate_category_percentages(
    category_totals: dict[str, float], grand_total: float
) -> dict[str, float]:
    """Calculate what percentage of total spending each category takes up."""
    percentages: dict[str, float] = {}

    if grand_total <= 0:
        for cat in category_totals:
            percentages[cat] = 0.0
        return percentages

    for cat, total in category_totals.items():
        pct = (total / grand_total) * 100.0
        percentages[cat] = round(pct, 2)

    return percentages


def sort_expenses_by_amount(expenses: list[dict], descending: bool = True) -> list[dict]:
    """
    Sort expenses by amount using bubble sort.
    Creates a copy so the original order isn't changed.
    """
    sorted_list = list(expenses)
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            should_swap = False
            if descending:
                if sorted_list[j]["amount"] < sorted_list[j + 1]["amount"]:
                    should_swap = True
            else:
                if sorted_list[j]["amount"] > sorted_list[j + 1]["amount"]:
                    should_swap = True

            if should_swap:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list
