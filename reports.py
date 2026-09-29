"""
reports.py
Report generation and table formatting utilities.
Author: Pragya Singh
"""

import analysis
import budget


def make_progress_bar(percentage: float, width: int = 20) -> str:
    """Create a simple text-based progress bar for percentages."""
    bounded = max(0.0, min(percentage, 100.0))
    filled = int(round(width * (bounded / 100.0)))
    empty = width - filled
    bar = "=" * filled + "-" * empty
    return f"[{bar}] {percentage:5.1f}%"


def format_expense_table(expenses: list[dict], title: str = "EXPENSE RECORDS") -> str:
    """Format expenses into an aligned ASCII table."""
    if not expenses:
        return f"\n--- {title} ---\nNo expense records found.\n"

    # Column widths
    id_w = 4
    date_w = 10
    cat_w = 15
    amt_w = 12
    desc_w = 34
    total_width = id_w + date_w + cat_w + amt_w + desc_w + 16

    header = (
        f"+{'-' * (total_width - 2)}+\n"
        f"| {title.center(total_width - 4)} |\n"
        f"+{'-' * (id_w + 2)}+{'-' * (date_w + 2)}+{'-' * (cat_w + 2)}+{'-' * (amt_w + 2)}+{'-' * (desc_w + 2)}+\n"
        f"| {'ID':^{id_w}} | {'Date':^{date_w}} | {'Category':^{cat_w}} | {'Amount (INR)':^{amt_w}} | {'Description':^{desc_w}} |\n"
        f"+{'-' * (id_w + 2)}+{'-' * (date_w + 2)}+{'-' * (cat_w + 2)}+{'-' * (amt_w + 2)}+{'-' * (desc_w + 2)}+"
    )

    rows = []
    grand_total = 0.0

    for exp in expenses:
        grand_total += exp["amount"]
        desc = exp["description"]
        # Shorten long descriptions so the table stays aligned.
        if len(desc) > desc_w:
            desc = desc[: desc_w - 3] + "..."

        row = (
            f"| {exp['id']:>{id_w}} | "
            f"{exp['date']:^{date_w}} | "
            f"{exp['category']:<{cat_w}} | "
            f"{exp['amount']:>{amt_w}.2f} | "
            f"{desc:<{desc_w}} |"
        )
        rows.append(row)

    footer = (
        f"+{'-' * (id_w + 2)}+{'-' * (date_w + 2)}+{'-' * (cat_w + 2)}+{'-' * (amt_w + 2)}+{'-' * (desc_w + 2)}+\n"
        f"| {'TOTAL (' + str(len(expenses)) + ' items)':<{id_w + date_w + cat_w + 6}} | "
        f"{grand_total:>{amt_w}.2f} | {'':<{desc_w}} |\n"
        f"+{'-' * (total_width - 2)}+"
    )

    return header + "\n" + "\n".join(rows) + "\n" + footer


def format_category_summary(expenses: list[dict]) -> str:
    """Format category spending totals with progress bars."""
    if not expenses:
        return "No expenses to analyze."

    grand_total = analysis.calculate_total_expense(expenses)
    cat_totals = analysis.calculate_category_totals(expenses)
    cat_percentages = analysis.calculate_category_percentages(cat_totals, grand_total)

    lines = [
        "=" * 68,
        "               CATEGORY-WISE SPENDING BREAKDOWN",
        "=" * 68,
        f"{'Category':<16} | {'Total (INR)':>12} | {'Share of Total':<30}",
        "-" * 68,
    ]

    for cat in sorted(cat_totals.keys()):
        total = cat_totals[cat]
        pct = cat_percentages[cat]
        bar = make_progress_bar(pct, width=16)
        lines.append(f"{cat:<16} | {total:>12.2f} | {bar}")

    lines.append("-" * 68)
    lines.append(f"{'Grand Total':<16} | {grand_total:>12.2f} | 100.0%")
    lines.append("=" * 68)

    return "\n".join(lines)


def generate_full_report(expenses: list[dict], monthly_budget: float) -> str:
    """Generate a clean summary report of spending and budget status."""
    total_spent = analysis.calculate_total_expense(expenses)
    count = analysis.count_expenses(expenses)
    avg_expense = analysis.calculate_average_expense(expenses)
    highest = analysis.find_highest_expense(expenses)
    lowest = analysis.find_lowest_expense(expenses)
    b_status = budget.evaluate_budget(monthly_budget, total_spent)

    lines = [
        "*" * 68,
        "          PERSONAL EXPENSE TRACKER - MONTHLY REPORT",
        "*" * 68,
        "",
        "--- OVERVIEW ---",
        f"  Total Number of Transactions : {count}",
        f"  Total Expenditure            : INR {total_spent:.2f}",
        f"  Average Expense / Transaction: INR {avg_expense:.2f}",
    ]

    if highest:
        lines.append(
            f"  Highest Single Expense       : INR {highest['amount']:.2f} "
            f"({highest['category']} - '{highest['description']}' on {highest['date']})"
        )
    else:
        lines.append("  Highest Single Expense       : None")

    if lowest:
        lines.append(
            f"  Lowest Single Expense        : INR {lowest['amount']:.2f} "
            f"({lowest['category']} - '{lowest['description']}' on {lowest['date']})"
        )
    else:
        lines.append("  Lowest Single Expense        : None")

    lines.append("")
    lines.append("--- BUDGET STATUS ---")
    lines.append(f"  Designated Monthly Budget    : INR {b_status['budget']:.2f}")
    lines.append(f"  Actual Monthly Spending      : INR {b_status['total_spent']:.2f}")
    lines.append(f"  Utilization Rate             : {b_status['percentage_used']:.1f}%")
    lines.append(f"  Budget Status                : {b_status['status']}")
    lines.append(f"  Details                      : {b_status['message']}")

    lines.append("")
    lines.append(format_category_summary(expenses))

    return "\n".join(lines)


def export_report_to_file(report_content: str, filename: str = "expense_report.txt") -> bool:
    """Save the generated report text to a file on disk."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        return True
    except OSError:
        return False
