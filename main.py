"""
main.py
Personal Expense Tracker
Console application for tracking daily spending and managing monthly budgets.
Author: Pragya Singh (CSE1021 Project - VIT)
"""

import sys
import analysis
import budget
import data
import expense_manager
import reports
import validation


def prompt_add_expense(expenses: list[dict]) -> None:
    """Prompt the user to enter details for a new expense and save it."""
    print("\n" + "=" * 50)
    print("                ADD NEW EXPENSE")
    print("=" * 50)

    # 1. Date input
    while True:
        date_input = input("Enter date (YYYY-MM-DD) [Press Enter for today: 2026-09-28]: ").strip()
        if not date_input:
            date_input = "2026-09-28"

        valid, result = validation.validate_date(date_input)
        if valid:
            date_val = result
            break
        print(result)

    # 2. Category selection
    print("\nSelect Category:")
    for idx, cat_name in enumerate(data.DEFAULT_CATEGORIES, start=1):
        print(f"  {idx}. {cat_name}")
    print(f"  {len(data.DEFAULT_CATEGORIES) + 1}. Other (Custom Category)")

    while True:
        cat_choice = input("Enter choice number or category name: ").strip()
        if cat_choice.isdigit():
            c_int = int(cat_choice)
            if 1 <= c_int <= len(data.DEFAULT_CATEGORIES):
                category_val = data.DEFAULT_CATEGORIES[c_int - 1]
                break
            elif c_int == len(data.DEFAULT_CATEGORIES) + 1:
                custom_cat = input("Enter custom category name: ").strip()
                valid, result = validation.validate_non_empty(custom_cat, "Category")
                if valid:
                    category_val = result.title()
                    break
                print(result)
            else:
                print("Invalid choice. Please select an option from the list above.")
        else:
            valid, result = validation.validate_non_empty(cat_choice, "Category")
            if valid:
                category_val = result.title()
                break
            print(result)

    # 3. Amount input
    while True:
        amt_input = input("Enter amount in INR (e.g. 250.00): ").strip()
        valid, result = validation.validate_amount(amt_input)
        if valid:
            amount_val = result
            break
        print(result)

    # 4. Description input
    while True:
        desc_input = input("Enter a short description: ").strip()
        valid, result = validation.validate_non_empty(desc_input, "Description")
        if valid:
            description_val = result
            break
        print(result)

    # Save to memory and disk
    new_record = expense_manager.add_expense(
        expenses,
        date=date_val,
        category=category_val,
        amount=amount_val,
        description=description_val,
    )
    data.save_expenses(expenses)

    print("\nExpense added successfully!")
    print(
        f"  ID: {new_record['id']} | Date: {new_record['date']} | "
        f"Category: {new_record['category']} | Amount: INR {new_record['amount']:.2f}"
    )


def handle_view_expenses(expenses: list[dict]) -> None:
    """Show all expenses in an aligned table."""
    print("\n" + reports.format_expense_table(expenses, title="ALL EXPENSE RECORDS"))


def handle_search_expenses(expenses: list[dict]) -> None:
    """Search and filter expenses by category, date, or minimum amount."""
    while True:
        print("\n" + "-" * 40)
        print("          SEARCH / FILTER EXPENSES")
        print("-" * 40)
        print("1. Search by Category")
        print("2. Search by Date / Month")
        print("3. Filter by Minimum Amount")
        print("4. Return to Main Menu")
        print("-" * 40)

        choice = input("Enter search option (1-4): ").strip()

        if choice == "1":
            cat_query = input("Enter category name (e.g., Food, Travel): ").strip()
            if not cat_query:
                print("Category query cannot be empty.")
                continue
            matched = expense_manager.search_by_category(expenses, cat_query)
            print("\n" + reports.format_expense_table(matched, title=f"SEARCH RESULTS: '{cat_query}'"))

        elif choice == "2":
            date_query = input("Enter date (YYYY-MM-DD) or Month (YYYY-MM): ").strip()
            if not date_query:
                print("Date query cannot be empty.")
                continue
            matched = expense_manager.search_by_date(expenses, date_query)
            print("\n" + reports.format_expense_table(matched, title=f"SEARCH RESULTS: '{date_query}'"))

        elif choice == "3":
            amt_query = input("Enter minimum amount in INR: ").strip()
            valid, min_amt = validation.validate_amount(amt_query)
            if not valid:
                print(min_amt)
                continue
            matched = expense_manager.filter_by_min_amount(expenses, min_amt)
            print("\n" + reports.format_expense_table(matched, title=f"EXPENSES >= INR {min_amt:.2f}"))

        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")


def handle_update_expense(expenses: list[dict]) -> None:
    """Edit an existing expense record by ID."""
    print("\n" + "=" * 50)
    print("               UPDATE EXPENSE RECORD")
    print("=" * 50)

    id_str = input("Enter the ID of the expense to update: ").strip()
    try:
        exp_id = int(id_str)
    except ValueError:
        print("Error: Expense ID must be a number.")
        return

    record, _ = expense_manager.find_expense_by_id(expenses, exp_id)
    if record is None:
        print(f"Error: No expense found with ID {exp_id}.")
        return

    print("\nCurrent Record Details:")
    print(f"  ID          : {record['id']}")
    print(f"  Date        : {record['date']}")
    print(f"  Category    : {record['category']}")
    print(f"  Amount (INR): {record['amount']:.2f}")
    print(f"  Description : {record['description']}")
    print("\n(Press Enter to leave a field unchanged)\n")

    # Update Date
    new_date = None
    while True:
        date_in = input(f"New Date [{record['date']}]: ").strip()
        if not date_in:
            break
        valid, res = validation.validate_date(date_in)
        if valid:
            new_date = res
            break
        print(res)

    # Update Category
    new_category = None
    cat_in = input(f"New Category [{record['category']}]: ").strip()
    if cat_in:
        new_category = cat_in.title()

    # Update Amount
    new_amount = None
    while True:
        amt_in = input(f"New Amount in INR [{record['amount']:.2f}]: ").strip()
        if not amt_in:
            break
        valid, res = validation.validate_amount(amt_in)
        if valid:
            new_amount = res
            break
        print(res)

    # Update Description
    new_desc = None
    desc_in = input(f"New Description [{record['description']}]: ").strip()
    if desc_in:
        new_desc = desc_in

    updated = expense_manager.update_expense(
        expenses,
        expense_id=exp_id,
        new_date=new_date,
        new_category=new_category,
        new_amount=new_amount,
        new_description=new_desc,
    )

    if updated:
        data.save_expenses(expenses)
        print(f"\nExpense #{exp_id} updated successfully!")
    else:
        print("\nError: Could not update expense.")


def handle_delete_expense(expenses: list[dict]) -> None:
    """Delete an expense record after asking for confirmation."""
    print("\n" + "=" * 50)
    print("               DELETE EXPENSE RECORD")
    print("=" * 50)

    id_str = input("Enter the ID of the expense to delete: ").strip()
    try:
        exp_id = int(id_str)
    except ValueError:
        print("Error: Expense ID must be a number.")
        return

    record, _ = expense_manager.find_expense_by_id(expenses, exp_id)
    if record is None:
        print(f"Error: No expense found with ID {exp_id}.")
        return

    print("\nSelected Record:")
    print(
        f"  ID: {record['id']} | Date: {record['date']} | "
        f"Category: {record['category']} | Amount: INR {record['amount']:.2f} | "
        f"'{record['description']}'"
    )

    confirm = input("\nAre you sure you want to delete this expense? (y/n): ").strip().lower()
    if confirm in ("y", "yes"):
        deleted = expense_manager.delete_expense(expenses, exp_id)
        if deleted:
            data.save_expenses(expenses)
            print(f"Expense #{exp_id} deleted successfully.")
        else:
            print("Error: Could not delete record.")
    else:
        print("Deletion cancelled.")


def handle_expense_analysis(expenses: list[dict]) -> None:
    """Display analytics: totals, averages, extremes, and category breakdown."""
    print("\n" + "=" * 68)
    print("                   EXPENSE ANALYTICS")
    print("=" * 68)

    if not expenses:
        print("No expenses recorded yet to analyze.")
        return

    total = analysis.calculate_total_expense(expenses)
    count = analysis.count_expenses(expenses)
    avg = analysis.calculate_average_expense(expenses)
    highest = analysis.find_highest_expense(expenses)
    lowest = analysis.find_lowest_expense(expenses)
    unique_cats = expense_manager.get_unique_categories(expenses)

    print(f"  * Total Transactions Recorded : {count}")
    print(f"  * Total Expenditure           : INR {total:.2f}")
    print(f"  * Average Expense Amount      : INR {avg:.2f}")
    print(f"  * Unique Expense Categories   : {len(unique_cats)} ({', '.join(sorted(unique_cats))})")

    if highest:
        print(f"  * Highest Single Transaction  : INR {highest['amount']:.2f} (ID #{highest['id']} - {highest['category']})")
    if lowest:
        print(f"  * Lowest Single Transaction   : INR {lowest['amount']:.2f} (ID #{lowest['id']} - {lowest['category']})")

    print("\n" + reports.format_category_summary(expenses))

    # Optional bubble sort
    sort_choice = input("\nWould you like to view transactions sorted by amount? (y/n): ").strip().lower()
    if sort_choice in ("y", "yes"):
        sorted_records = analysis.sort_expenses_by_amount(expenses, descending=True)
        print("\n" + reports.format_expense_table(sorted_records, title="EXPENSES SORTED BY AMOUNT (DESCENDING)"))


def handle_budget_management(expenses: list[dict], current_budget: float) -> float:
    """Display budget status and allow setting a new budget amount."""
    print("\n" + "=" * 50)
    print("               BUDGET MANAGEMENT")
    print("=" * 50)

    total_spent = analysis.calculate_total_expense(expenses)
    status_dict = budget.evaluate_budget(current_budget, total_spent)

    print(f"  Current Monthly Budget : INR {status_dict['budget']:.2f}")
    print(f"  Total Spending to Date : INR {status_dict['total_spent']:.2f}")
    print(f"  Budget Status          : {status_dict['status']}")
    print(f"  Utilization Rate       : {status_dict['percentage_used']:.1f}%")
    print(f"  Details                : {status_dict['message']}")

    print("\nOptions:")
    print("1. Set a New Monthly Budget")
    print("2. Keep Current Budget and Return")
    choice = input("Enter choice (1-2): ").strip()

    if choice == "1":
        while True:
            new_b_str = input("Enter new monthly budget in INR: ").strip()
            valid, result = validation.validate_amount(new_b_str)
            if valid:
                new_budget = result
                data.save_budget(new_budget)
                print(f"Monthly budget updated to INR {new_budget:.2f}.")
                return new_budget
            print(result)

    return current_budget


def handle_monthly_summary(expenses: list[dict], monthly_budget: float) -> None:
    """Generate summary report and allow exporting to a text file."""
    full_report = reports.generate_full_report(expenses, monthly_budget)
    print("\n" + full_report)

    export_choice = input("\nWould you like to export this report to 'expense_report.txt'? (y/n): ").strip().lower()
    if export_choice in ("y", "yes"):
        success = reports.export_report_to_file(full_report, "expense_report.txt")
        if success:
            print("Report saved successfully to 'expense_report.txt'.")
        else:
            print("Error: Could not export report to file.")


def print_main_menu() -> None:
    """Display main menu options."""
    print("\n" + "=" * 48)
    print("        PERSONAL EXPENSE TRACKER")
    print("=" * 48)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Search / Filter Expenses")
    print("  4. Update Expense")
    print("  5. Delete Expense")
    print("  6. Expense Analysis")
    print("  7. Set / View Monthly Budget")
    print("  8. Monthly Summary Report")
    print("  9. Save and Exit")
    print("=" * 48)


def main() -> None:
    """Main program loop."""
    print("\n========================================================")
    print("   Personal Expense Tracker (VIT - CSE1021 Project)")
    print("                   by Pragya Singh")
    print("========================================================")

    # Load stored data
    expenses = data.load_expenses()
    monthly_budget = data.load_budget()

    print(f"Loaded {len(expenses)} expense records. Current budget: INR {monthly_budget:.2f}.")

    while True:
        print_main_menu()
        user_choice = input("Enter your choice (1-9): ").strip()

        valid, choice_or_err = validation.validate_menu_choice(user_choice, 1, 9)
        if not valid:
            print(f"\n{choice_or_err}")
            continue

        choice = choice_or_err

        if choice == 1:
            prompt_add_expense(expenses)
        elif choice == 2:
            handle_view_expenses(expenses)
        elif choice == 3:
            handle_search_expenses(expenses)
        elif choice == 4:
            handle_update_expense(expenses)
        elif choice == 5:
            handle_delete_expense(expenses)
        elif choice == 6:
            handle_expense_analysis(expenses)
        elif choice == 7:
            monthly_budget = handle_budget_management(expenses, monthly_budget)
        elif choice == 8:
            handle_monthly_summary(expenses, monthly_budget)
        elif choice == 9:
            # Save data before quitting
            data.save_expenses(expenses)
            data.save_budget(monthly_budget)
            print("\n" + "=" * 50)
            print("  All expenses and budget saved successfully.")
            print("  Thanks for using Personal Expense Tracker!")
            print("=" * 50 + "\n")
            break


if __name__ == "__main__":
    main()
