# Pseudocode: Personal Expense Tracker

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

This document details the pseudocode for the core operations implemented in the Personal Expense Tracker.

---

## 1. Main Menu Operation
```text
ALGORITHM MainMenu
BEGIN
    expenses ← LoadExpensesFromFile("expenses.json")
    monthly_budget ← LoadBudgetFromFile("budget.json")
    running ← TRUE

    WHILE running DO
        DISPLAY "========================================"
        DISPLAY "        PERSONAL EXPENSE TRACKER        "
        DISPLAY "========================================"
        DISPLAY "1. Add Expense"
        DISPLAY "2. View All Expenses"
        DISPLAY "3. Search / Filter Expenses"
        DISPLAY "4. Update Expense"
        DISPLAY "5. Delete Expense"
        DISPLAY "6. Expense Analysis"
        DISPLAY "7. Set / View Monthly Budget"
        DISPLAY "8. Monthly Summary Report"
        DISPLAY "9. Save and Exit"
        DISPLAY "========================================"
        
        INPUT choice_str
        valid, choice ← ValidateMenuChoice(choice_str, 1, 9)

        IF NOT valid THEN
            DISPLAY "Invalid choice. Please enter a number between 1 and 9."
            CONTINUE
        END IF

        IF choice == 1 THEN
            CALL PromptAddExpense(expenses)
        ELSE IF choice == 2 THEN
            CALL HandleViewExpenses(expenses)
        ELSE IF choice == 3 THEN
            CALL HandleSearchExpenses(expenses)
        ELSE IF choice == 4 THEN
            CALL HandleUpdateExpense(expenses)
        ELSE IF choice == 5 THEN
            CALL HandleDeleteExpense(expenses)
        ELSE IF choice == 6 THEN
            CALL HandleExpenseAnalysis(expenses)
        ELSE IF choice == 7 THEN
            monthly_budget ← HandleBudgetManagement(expenses, monthly_budget)
        ELSE IF choice == 8 THEN
            CALL HandleMonthlySummary(expenses, monthly_budget)
        ELSE IF choice == 9 THEN
            CALL SaveExpensesToFile(expenses, "expenses.json")
            CALL SaveBudgetToFile(monthly_budget, "budget.json")
            DISPLAY "Records saved. Goodbye!"
            running ← FALSE
        END IF
    END WHILE
END ALGORITHM
```

---

## 2. Adding an Expense
```text
ALGORITHM AddExpense(expenses)
BEGIN
    // Step 1: Get and validate the date
    REPEAT
        INPUT date_input
        IF date_input IS EMPTY THEN
            date_input ← "2026-09-28" // Default date
        END IF
        is_valid_date, date_val ← ValidateDate(date_input)
        IF NOT is_valid_date THEN
            DISPLAY "Invalid date format. Expected YYYY-MM-DD."
        END IF
    UNTIL is_valid_date

    // Step 2: Ask the user to choose a category and validate it
    DISPLAY AvailableCategories
    REPEAT
        INPUT cat_choice
        is_valid_cat, category_val ← ValidateCategory(cat_choice)
    UNTIL is_valid_cat

    // Step 3: Get and validate the amount
    REPEAT
        INPUT amt_input
        is_valid_amt, amount_val ← ValidateAmount(amt_input)
        IF NOT is_valid_amt THEN
            DISPLAY "Amount must be a numeric value greater than zero."
        END IF
    UNTIL is_valid_amt

    // Step 4: Get a non-empty description
    REPEAT
        INPUT desc_input
        is_valid_desc, description_val ← ValidateNonEmpty(desc_input, "Description")
    UNTIL is_valid_desc

    // Step 5: Find the next available ID
    max_id ← 0
    FOR EACH item IN expenses DO
        IF item["id"] > max_id THEN
            max_id ← item["id"]
        END IF
    END FOR
    new_id ← max_id + 1

    // Step 6: Create the record and add it to the list
    new_expense ← {
        "id": new_id,
        "date": date_val,
        "category": category_val,
        "amount": amount_val,
        "description": description_val
    }
    APPEND new_expense TO expenses
    SaveExpensesToFile(expenses, "expenses.json")

    DISPLAY "Expense added successfully with ID: ", new_id
END ALGORITHM
```

---

## 3. Displaying Expenses
```text
ALGORITHM DisplayExpenses(expenses, title)
BEGIN
    IF LENGTH(expenses) == 0 THEN
        DISPLAY "No expense records found."
        RETURN
    END IF

    DISPLAY HeaderSeparator
    DISPLAY "| ID | Date | Category | Amount (INR) | Description |"
    DISPLAY HeaderSeparator

    grand_total ← 0.0
    FOR EACH item IN expenses DO
        grand_total ← grand_total + item["amount"]
        DISPLAY item["id"], item["date"], item["category"], item["amount"], item["description"]
    END FOR

    DISPLAY FooterSeparator
    DISPLAY "TOTAL (" + LENGTH(expenses) + " items): INR " + grand_total
    DISPLAY FooterSeparator
END ALGORITHM
```

---

## 4. Searching and Filtering Expenses
```text
ALGORITHM SearchByCategory(expenses, query_category)
BEGIN
    matched_list ← EMPTY LIST
    query_lower ← TO_LOWERCASE(TRIM(query_category))

    FOR EACH expense IN expenses DO
        cat_lower ← TO_LOWERCASE(expense["category"])
        IF query_lower IS IN cat_lower THEN
            APPEND expense TO matched_list
        END IF
    END FOR

    RETURN matched_list
END ALGORITHM

ALGORITHM SearchByDate(expenses, query_date)
BEGIN
    matched_list ← EMPTY LIST
    FOR EACH expense IN expenses DO
        IF STARTS_WITH(expense["date"], query_date) THEN
            APPEND expense TO matched_list
        END IF
    END FOR
    RETURN matched_list
END ALGORITHM

ALGORITHM FilterByMinAmount(expenses, min_amount)
BEGIN
    filtered_list ← EMPTY LIST
    FOR EACH expense IN expenses DO
        IF expense["amount"] >= min_amount THEN
            APPEND expense TO filtered_list
        END IF
    END FOR
    RETURN filtered_list
END ALGORITHM
```

---

## 5. Calculating Total Expenses (Summation Algorithm)
```text
ALGORITHM CalculateTotalExpense(expenses)
BEGIN
    // Add each expense amount to a running total
    total_spending ← 0.0

    FOR EACH expense IN expenses DO
        total_spending ← total_spending + expense["amount"]
    END FOR

    RETURN ROUND(total_spending, 2)
END ALGORITHM

ALGORITHM CountExpenses(expenses)
BEGIN
    // Count each record one by one
    total_count ← 0

    FOR EACH _ IN expenses DO
        total_count ← total_count + 1
    END FOR

    RETURN total_count
END ALGORITHM
```

---

## 6. Finding Maximum and Minimum Expense
```text
ALGORITHM FindHighestExpense(expenses)
BEGIN
    IF LENGTH(expenses) == 0 THEN
        RETURN NULL
    END IF

    highest_expense ← expenses[0]

    FOR i ← 1 TO LENGTH(expenses) - 1 DO
        IF expenses[i]["amount"] > highest_expense["amount"] THEN
            highest_expense ← expenses[i]
        END IF
    END FOR

    RETURN highest_expense
END ALGORITHM

ALGORITHM FindLowestExpense(expenses)
BEGIN
    IF LENGTH(expenses) == 0 THEN
        RETURN NULL
    END IF

    lowest_expense ← expenses[0]

    FOR i ← 1 TO LENGTH(expenses) - 1 DO
        IF expenses[i]["amount"] < lowest_expense["amount"] THEN
            lowest_expense ← expenses[i]
        END IF
    END FOR

    RETURN lowest_expense
END ALGORITHM
```

---

## 7. Category-Wise Analysis
```text
ALGORITHM CalculateCategoryTotals(expenses)
BEGIN
    category_totals ← EMPTY DICTIONARY

    FOR EACH expense IN expenses DO
        category ← expense["category"]
        amount ← expense["amount"]

        IF category IS IN KEYS(category_totals) THEN
            category_totals[category] ← category_totals[category] + amount
        ELSE
            category_totals[category] ← amount
        END IF
    END FOR

    RETURN category_totals
END ALGORITHM

ALGORITHM CalculateCategoryPercentages(category_totals, grand_total)
BEGIN
    percentages ← EMPTY DICTIONARY

    IF grand_total <= 0 THEN
        FOR EACH category IN KEYS(category_totals) DO
            percentages[category] ← 0.0
        END FOR
        RETURN percentages
    END IF

    FOR EACH (category, total) IN category_totals DO
        pct ← (total / grand_total) * 100.0
        percentages[category] ← ROUND(pct, 2)
    END FOR

    RETURN percentages
END ALGORITHM
```

---

## 8. Budget Calculation and Evaluation
```text
ALGORITHM EvaluateBudget(budget, total_spending)
BEGIN
    difference ← budget - total_spending

    IF budget > 0 THEN
        pct_used ← (total_spending / budget) * 100.0
    ELSE
        pct_used ← 0.0
    END IF

    IF total_spending < budget THEN
        status ← "UNDER_BUDGET"
        message ← "Within budget. Remaining: INR " + difference
    ELSE IF total_spending == budget THEN
        status ← "EXACT_BUDGET"
        message ← "Budget reached exactly. Remaining: INR 0.00"
    ELSE
        status ← "OVER_BUDGET"
        overspent ← ABSOLUTE(difference)
        message ← "Budget exceeded by INR " + overspent
    END IF

    RETURN {
        "budget": budget,
        "total_spent": total_spending,
        "difference": difference,
        "percentage_used": pct_used,
        "status": status,
        "message": message
    }
END ALGORITHM
```
