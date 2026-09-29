# Flowcharts: Personal Expense Tracker

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

---

## 1. Main Program Workflow

```mermaid
flowchart TD
    Start(["Start Main Program"]) --> LoadData["Load expenses.json and budget.json"]
    LoadData --> DisplayMenu[/"Display Main Menu Options 1 to 9"/]
    DisplayMenu --> ReadChoice[/"Read User Choice"/]
    ReadChoice --> ValidateChoice{"Is choice valid integer 1 to 9?"}
    
    ValidateChoice -- "No" --> ShowErr[/"Display Invalid Option Message"/] --> DisplayMenu
    ValidateChoice -- "Yes" --> RouteChoice{"Check Choice Value"}

    RouteChoice -- "1" --> M1["Call prompt_add_expense()"] --> DisplayMenu
    RouteChoice -- "2" --> M2["Call handle_view_expenses()"] --> DisplayMenu
    RouteChoice -- "3" --> M3["Call handle_search_expenses()"] --> DisplayMenu
    RouteChoice -- "4" --> M4["Call handle_update_expense()"] --> DisplayMenu
    RouteChoice -- "5" --> M5["Call handle_delete_expense()"] --> DisplayMenu
    RouteChoice -- "6" --> M6["Call handle_expense_analysis()"] --> DisplayMenu
    RouteChoice -- "7" --> M7["Call handle_budget_management()"] --> DisplayMenu
    RouteChoice -- "8" --> M8["Call handle_monthly_summary()"] --> DisplayMenu
    RouteChoice -- "9" --> SaveData["Save data to expenses.json & budget.json"] --> Stop(["Stop / Exit"])
```

---

## 2. Add Expense Flow

```mermaid
flowchart TD
    A(["Start: Add Expense"]) --> B[/"Prompt for Date (YYYY-MM-DD)"/]
    B --> C{"validate_date(date)"}
    C -- "Invalid" --> D[/"Display Date Error Message"/] --> B
    C -- "Valid" --> E[/"Prompt for Category from Default Tuple"/]

    E --> F{"validate_category(choice)"}
    F -- "Invalid" --> G[/"Display Category Error Message"/] --> E
    F -- "Valid" --> H[/"Prompt for Expense Amount"/]

    H --> I{"validate_amount(amt) > 0 and numeric?"}
    I -- "Invalid" --> J[/"Display Amount Error Message"/] --> H
    I -- "Valid" --> K[/"Prompt for Description"/]

    K --> L{"validate_non_empty(desc)"}
    L -- "Invalid" --> M[/"Display Description Error Message"/] --> K
    L -- "Valid" --> N["Compute new_id = max(existing IDs) + 1"]

    N --> O["Create Dictionary: {id, date, category, amount, description}"]
    O --> P["Append Dictionary to expenses list"]
    P --> Q["Call save_expenses() to write JSON"]
    Q --> R[/"Display Success Confirmation"/]
    R --> S(["End: Return to Main Menu"])
```

---

## 3. Expense Analysis Flow

```mermaid
flowchart TD
    StartA(["Start: Expense Analysis"]) --> CheckEmpty{"Is expenses list empty?"}
    CheckEmpty -- "Yes" --> ShowEmpty[/"Display: No expenses recorded"/] --> EndA(["End: Return"])

    CheckEmpty -- "No" --> InitVars["Initialize total = 0.0, count = 0, cat_totals = {}"]
    InitVars --> SetExtremes["Set highest = expenses[0], lowest = expenses[0]"]
    
    SetExtremes --> LoopStart{"For each expense in expenses"}
    LoopStart -- "Has Next Item" --> Accumulate["count = count + 1<br/>total = total + expense.amount"]
    Accumulate --> CheckHigh{"expense.amount > highest.amount?"}
    CheckHigh -- "Yes" --> UpdateHigh["highest = expense"] --> CheckLow
    CheckHigh -- "No" --> CheckLow{"expense.amount < lowest.amount?"}
    CheckLow -- "Yes" --> UpdateLow["lowest = expense"] --> DictCat
    CheckLow -- "No" --> DictCat["Accumulate category: cat_totals[cat] += amount"]
    DictCat --> LoopStart

    LoopStart -- "Done Iterating" --> CalcAvg["avg = total / count"]
    CalcAvg --> CalcPct["Calculate percentage for each category: (cat_total / total) * 100"]
    CalcPct --> DisplayStats[/"Display Total, Count, Average, Highest, Lowest, Unique Categories"/]
    DisplayStats --> DisplayBars[/"Display Category Table with ASCII Progress Bars"/]
    DisplayBars --> AskSort[/"Prompt: View sorted by amount?"/]
    AskSort --> SortDecision{"User selected Yes?"}
    SortDecision -- "Yes" --> BubbleSort["Execute Bubble Sort on expenses by amount"] --> DisplaySorted[/"Display Sorted Table"/] --> EndA
    SortDecision -- "No" --> EndA
```

---

## 4. Budget Evaluation Flow

```mermaid
flowchart TD
    StartB(["Start: Evaluate Budget"]) --> ReadVals["Read monthly_budget and total_spending"]
    ReadVals --> CalcDiff["difference = monthly_budget - total_spending"]
    CalcDiff --> CalcPct["pct_used = (total_spending / monthly_budget) * 100"]
    
    CalcPct --> CheckUnder{"total_spending < monthly_budget ?"}
    CheckUnder -- "Yes" --> StatusUnder["status = 'UNDER_BUDGET'<br/>message = 'Within Budget. Remaining balance available.'"] --> ReturnDict

    CheckUnder -- "No" --> CheckExact{"total_spending == monthly_budget ?"}
    CheckExact -- "Yes" --> StatusExact["status = 'EXACT_BUDGET'<br/>message = 'Budget Reached Exactly. Remaining: 0.00'"] --> ReturnDict

    CheckExact -- "No" --> StatusOver["status = 'OVER_BUDGET'<br/>overspent = abs(difference)<br/>message = 'ALERT: Budget Exceeded'"] --> ReturnDict

    ReturnDict[/"Display Budget Status, Utilization Rate, and Balance Details"/]
    ReturnDict --> AskUpdate[/"Prompt: Update monthly budget?"/]
    AskUpdate --> UpCheck{"User wants to update?"}
    UpCheck -- "Yes" --> InputNew[/"Input & Validate New Budget Amount"/] --> SaveNew["Save to budget.json"] --> EndB(["End: Return"])
    UpCheck -- "No" --> EndB
```

---

## 5. Search & Filter Flow

```mermaid
flowchart TD
    StartS(["Start: Search / Filter"]) --> ShowMenu[/"Display Search Sub-menu:<br/>1. Category  2. Date/Month  3. Min Amount  4. Back"/]
    ShowMenu --> GetChoice[/"Input sub-choice"/]

    GetChoice --> C1{"Choice == 1?"}
    C1 -- "Yes" --> InCat[/"Enter category keyword"/] --> LinearCat["Iterate list, filter matching category substring"] --> TableView

    C1 -- "No" --> C2{"Choice == 2?"}
    C2 -- "Yes" --> InDate[/"Enter date (YYYY-MM-DD) or Month (YYYY-MM)"/] --> LinearDate["Iterate list, filter where date starts with input"] --> TableView

    C2 -- "No" --> C3{"Choice == 3?"}
    C3 -- "Yes" --> InAmt[/"Enter minimum amount threshold"/] --> LinearAmt["Iterate list, filter where amount >= threshold"] --> TableView

    C3 -- "No" --> C4{"Choice == 4?"}
    C4 -- "Yes" --> EndS(["End: Return to Main Menu"])
    C4 -- "No" --> ShowErr[/"Display Invalid Option"/] --> ShowMenu

    TableView[/"Format and Display Filtered Results in ASCII Table"/] --> ShowMenu
```
