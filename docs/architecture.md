# System Architecture & Design

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

---

## 1. System Architecture

The application uses a **Top-Down Modular Architecture**. The console menu (`main.py`) acts as the controller, interacting with the student in the terminal and dispatching tasks to dedicated modules (`expense_manager`, `analysis`, `budget`, `reports`), while helper modules (`validation`, `data`) take care of input error checking and JSON file storage.

```mermaid
flowchart TD
    subgraph Presentation_Layer ["Presentation Layer (Console UI)"]
        UI["main.py (Menu Loop & Command Dispatcher)"]
    end

    subgraph Domain_Logic_Layer ["Domain Logic & Algorithms"]
        EM["expense_manager.py (CRUD, Linear Search, Filtering)"]
        AN["analysis.py (Summation, Counting, Min/Max, Bubble Sort)"]
        BM["budget.py (Budget Evaluation, Percentage Utilization)"]
        RP["reports.py (Table Formatter, Visual Progress Bars)"]
    end

    subgraph Support_and_Persistence_Layer ["Cross-Cutting & Persistence Layer"]
        VL["validation.py (Sanitization, Date/Amount Verification)"]
        DT["data.py (JSON I/O, File Serialization, Default Presets)"]
    end

    subgraph Storage ["Local Storage"]
        EF[("expenses.json")]
        BF[("budget.json")]
        RF[("expense_report.txt")]
    end

    UI --> VL
    UI --> EM
    UI --> AN
    UI --> BM
    UI --> RP
    UI --> DT

    EM --> VL
    AN --> EM
    RP --> AN
    RP --> BM
    DT --> EF
    DT --> BF
    RP -.-> RF
```

---

## 2. Use Case Diagram

The main user of the application is a **Student / User** who interacts with the program through the terminal.

```mermaid
flowchart LR
    User(("Student / User"))

    subgraph Personal_Expense_Tracker ["Personal Expense Tracker System"]
        UC1(["UC-1: Add New Expense"])
        UC2(["UC-2: View All Expenses in Table"])
        UC3(["UC-3: Search / Filter Transactions"])
        UC4(["UC-4: Update Existing Record"])
        UC5(["UC-5: Delete Transaction by ID"])
        UC6(["UC-6: Perform Expense Analytics"])
        UC7(["UC-7: Manage Monthly Budget"])
        UC8(["UC-8: Generate & Export Summary Report"])
        UC9(["UC-9: Save & Exit Application"])
    end

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    User --> UC7
    User --> UC8
    User --> UC9
```

---

## 3. Component & Module Breakdown

| Module | Responsibilities | Key Functions | Primary Data Structures |
| :--- | :--- | :--- | :--- |
| `main.py` | Command loop, user prompts, menu routing | `main()`, `print_main_menu()`, `prompt_add_expense()` | Strings, Ints, Booleans |
| `expense_manager.py` | In-memory CRUD, search, filter, set operations | `add_expense()`, `find_expense_by_id()`, `search_by_category()`, `delete_expense()` | List of Dictionaries, Sets |
| `analysis.py` | Spending algorithms written from first principles | `calculate_total_expense()`, `count_expenses()`, `find_highest_expense()`, `calculate_category_totals()`, `sort_expenses_by_amount()` | Lists, Dictionaries, Floats |
| `budget.py` | Budget comparison, threshold analysis, status messaging | `evaluate_budget()`, `filter_expenses_by_month()` | Floats, Dictionaries |
| `reports.py` | Aligned ASCII display, tables, progress indicators, export | `format_expense_table()`, `format_category_summary()`, `generate_full_report()`, `export_report_to_file()` | Strings, Lists, Dictionaries |
| `validation.py` | Data validation and input verification | `validate_amount()`, `validate_date()`, `validate_non_empty()`, `validate_menu_choice()` | Tuples, Strings, Floats |
| `data.py` | JSON serialization, file handling, presets | `load_expenses()`, `save_expenses()`, `load_budget()`, `save_budget()` | Lists of Dictionaries, Tuples |

---

## 4. Sequence Diagram: Adding an Expense

```mermaid
sequenceDiagram
    actor User as Student
    participant Main as main.py
    participant Val as validation.py
    participant Mgr as expense_manager.py
    participant Data as data.py
    participant File as expenses.json

    User->>Main: Select "1. Add Expense"
    Main->>User: Prompt for Date
    User->>Main: Enter "2026-09-28"
    Main->>Val: validate_date("2026-09-28")
    Val-->>Main: (True, "2026-09-28")

    Main->>User: Display Categories & Prompt
    User->>Main: Select Category "Food"
    
    Main->>User: Prompt for Amount
    User->>Main: Enter "350.00"
    Main->>Val: validate_amount("350.00")
    Val-->>Main: (True, 350.00)

    Main->>User: Prompt for Description
    User->>Main: Enter "Lunch at food court"
    Main->>Val: validate_non_empty(...)
    Val-->>Main: (True, "Lunch at food court")

    Main->>Mgr: add_expense(expenses, "2026-09-28", "Food", 350.00, ...)
    Mgr->>Mgr: Calculate unique ID = max(IDs) + 1
    Mgr->>Mgr: Append new dictionary record
    Mgr-->>Main: new_record dict

    Main->>Data: save_expenses(expenses)
    Data->>File: Write serialized JSON
    File-->>Data: OK
    Data-->>Main: True

    Main->>User: Display "Expense added successfully!"
```

---

## 5. Sequence Diagram: Spending Analysis

```mermaid
sequenceDiagram
    actor User as Student
    participant Main as main.py
    participant Ana as analysis.py
    participant Bud as budget.py
    participant Rep as reports.py

    User->>Main: Select "6. Expense Analysis"
    Main->>Ana: calculate_total_expense(expenses)
    Ana-->>Main: total_amount (Float)
    Main->>Ana: count_expenses(expenses)
    Ana-->>Main: count (Int)
    Main->>Ana: calculate_average_expense(expenses)
    Ana-->>Main: avg_amount (Float)
    Main->>Ana: find_highest_expense(expenses)
    Ana-->>Main: highest_record (Dict)
    Main->>Ana: find_lowest_expense(expenses)
    Ana-->>Main: lowest_record (Dict)
    Main->>Rep: format_category_summary(expenses)
    Rep->>Ana: calculate_category_totals(expenses)
    Ana-->>Rep: dict of category totals
    Rep->>Ana: calculate_category_percentages(...)
    Ana-->>Rep: dict of percentages
    Rep-->>Main: formatted summary string with progress bars
    Main->>User: Display analytics dashboard
```

---

## 6. Data & Storage Structure

### 6.1 Expense Record Structure (Dictionary)
Each expense is stored as a dictionary:
```python
{
    "id": 1,                               # Unique positive integer ID
    "date": "2026-09-28",                  # Calendar date string (YYYY-MM-DD)
    "category": "Food",                    # Category name string
    "amount": 350.00,                      # Numeric amount (INR, 2 decimal places)
    "description": "Lunch at food court"   # Brief note string
}
```

### 6.2 Predefined Categories (Tuple)
Standard categories are stored in an immutable tuple:
```python
DEFAULT_CATEGORIES = (
    "Food",
    "Travel",
    "Shopping",
    "Education",
    "Entertainment",
    "Bills",
    "Other",
)
```

### 6.3 Budget Storage (`budget.json`)
```json
{
    "monthly_budget": 5000.00
}
```

### 6.4 Storage Files
* **`expenses.json`**: List of all expense dictionaries formatted with indentation for readability.
* **`budget.json`**: JSON file holding the monthly budget limit.
* **`expense_report.txt`**: Text file export containing formatted ASCII tables, budget status, and category breakdowns.
