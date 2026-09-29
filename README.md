# Personal Expense Tracker

A lightweight, offline Python console application to track daily spending, monitor category habits, and manage a monthly student allowance.

Developed by **Pragya Singh** for **CSE1021 – Introduction to Problem Solving and Programming** at **Vellore Institute of Technology (VIT)**.

---

## Why I Built This

Managing a monthly allowance as a college student in a hostel is surprisingly tricky. Between food court meals, cold coffees at Gazebo, auto rides to Katpadi railway station, printing lab observation sheets, buying notebooks, and phone recharges, small payments happen almost every day. 

Because most transactions are quick UPI payments or cash under ₹200, it's very easy to lose track. By the end of the month, money seems to just vanish without any obvious big purchase.

Most existing expense tracker apps on mobile app stores are bloated:
- They require online logins and accounts.
- They ask for intrusive SMS and banking permissions.
- They show distracting ads and require active internet.

I built this **Personal Expense Tracker** as a simple, distraction-free terminal tool. It runs offline, saves your data locally in plain JSON files (`expenses.json` and `budget.json`), never touches your bank details, and is built from scratch using the problem-solving concepts taught in **CSE1021**.

---

## What It Can Do

- **Log daily expenses:** Enter the date, category, amount, and note. Each record gets an auto-incremented ID.
- **Smart error handling:** Checks that amounts are positive numbers, validates dates (including leap years and calendar day limits), and handles typos without crashing.
- **Tabular display:** Formats all transactions in an aligned ASCII table with running totals.
- **Search and filter:** Search transactions by category name, look up specific dates or month prefixes (e.g. `2026-09`), or filter for large purchases above a certain threshold (e.g. >= ₹500).
- **Edit and delete records:** Fix mistakes in previous records or delete an entry after answering a confirmation check.
- **Spending analysis:** Computes grand total spent, transaction count, average per expense, highest and lowest purchases, and category breakdowns with ASCII progress bars. Also includes an optional Bubble Sort to rank spending from highest to lowest.
- **Budget tracking:** Set a monthly spending limit and see immediately whether you are under budget, exactly at the limit, or over budget.
- **Export reports:** Generate a monthly overview in the terminal and save it to a clean text file (`expense_report.txt`).
- **No extra installations:** Built entirely with Python's standard library modules.

---

## Project Layout

```
project/
├── main.py                     # Console menu loop and user prompts
├── expense_manager.py          # CRUD operations, searching, and filtering
├── analysis.py                 # Math calculations (totals, averages, extremes, bubble sort)
├── budget.py                   # Budget comparison and monthly evaluation
├── reports.py                  # ASCII table generator and report exporter
├── validation.py               # Input validation for dates, amounts, and choices
├── data.py                     # Local JSON storage and starter sample data
├── requirements.txt            # Zero-dependency note and optional pytest
├── statement.md                # Project statement and scope
├── README.md                   # Project overview and setup instructions
│
├── docs/                       # Project documentation
│   ├── problem_statement.md    # Real-world student context and problem definition
│   ├── objectives.md           # Project goals and learning outcomes
│   ├── pseudocode.md           # Step-by-step pseudocode for core operations
│   ├── flowchart.md            # Mermaid flowcharts for major application flows
│   ├── architecture.md         # Modular system design and component diagrams
│   ├── testing.md              # Test plan and 30-case validation matrix
│   └── project_report.md       # Full academic project report
│
└── tests/
    └── test_expense_tracker.py # 30 automated unit tests using Python's unittest
```

---

## Getting Started

### Prerequisites
- Python 3.10 or higher.
- No external packages needed (uses only `json`, `os`, `sys`, `unittest`).

### Running the Application
Open a terminal in the project directory and run:
```powershell
python main.py
```

> **Starter Data:** On initial launch, the program automatically loads 8 realistic sample student expenses so you can try out search, analytics, and reports right away.

### Running the Unit Tests
All features come with automated unit tests using Python's built-in `unittest` module:
```powershell
python -m unittest tests/test_expense_tracker.py
```
For verbose output:
```powershell
python -m unittest -v tests/test_expense_tracker.py
```

---

## Sample Console Output

### Main Menu
```text
========================================================
   Personal Expense Tracker (VIT - CSE1021 Project)
                   by Pragya Singh
========================================================
Loaded 8 expense records. Current budget: INR 5000.00.

================================================
        PERSONAL EXPENSE TRACKER
================================================
  1. Add Expense
  2. View All Expenses
  3. Search / Filter Expenses
  4. Update Expense
  5. Delete Expense
  6. Expense Analysis
  7. Set / View Monthly Budget
  8. Monthly Summary Report
  9. Save and Exit
================================================
Enter your choice (1-9): 
```

### Viewing All Expenses in Tabular View
```text
+-----------------------------------------------------------------------------------------+
|                                   ALL EXPENSE RECORDS                                   |
+------+------------+-----------------+--------------+------------------------------------+
|  ID  |    Date    |    Category     | Amount (INR) |            Description             |
+------+------------+-----------------+--------------+------------------------------------+
|    1 | 2026-09-02 | Education       |      1200.00 | Semester reference textbooks an... |
|    2 | 2026-09-05 | Food            |       350.00 | VIT food court lunch with hoste... |
|    3 | 2026-09-08 | Travel          |       220.00 | Auto fare to Katpadi railway st... |
|    4 | 2026-09-12 | Bills           |       499.00 | Monthly high-speed mobile data ... |
|    5 | 2026-09-15 | Entertainment   |       300.00 | Weekend movie ticket               |
|    6 | 2026-09-18 | Shopping        |       850.00 | Replacement scientific calculat... |
|    7 | 2026-09-22 | Food            |       180.00 | Evening snacks and juice at Gazebo |
|    8 | 2026-09-25 | Education       |       450.00 | Lab record notebook and project... |
+------+------------+-----------------+--------------+------------------------------------+
| TOTAL (8 items)                     |      4049.00 |                                    |
+-----------------------------------------------------------------------------------------+
```

### Spending Analytics
```text
====================================================================
                   EXPENSE ANALYTICS
====================================================================
  * Total Transactions Recorded : 8
  * Total Expenditure           : INR 4049.00
  * Average Expense Amount      : INR 506.12
  * Unique Expense Categories   : 6 (Bills, Education, Entertainment, Food, Shopping, Travel)
  * Highest Single Transaction  : INR 1200.00 (ID #1 - Education)
  * Lowest Single Transaction   : INR 180.00 (ID #7 - Food)

====================================================================
               CATEGORY-WISE SPENDING BREAKDOWN
====================================================================
Category         |  Total (INR) | Share of Total                
--------------------------------------------------------------------
Bills            |       499.00 | [==--------------]  12.3%
Education        |      1650.00 | [=======---------]  40.8%
Entertainment    |       300.00 | [=---------------]   7.4%
Food             |       530.00 | [==--------------]  13.1%
Shopping         |       850.00 | [===-------------]  21.0%
Travel           |       220.00 | [=---------------]   5.4%
--------------------------------------------------------------------
Grand Total      |      4049.00 | 100.0%
====================================================================
```

### Budget Management
```text
==================================================
               BUDGET MANAGEMENT
==================================================
  Current Monthly Budget : INR 5000.00
  Total Spending to Date : INR 4049.00
  Budget Status          : UNDER_BUDGET
  Utilization Rate       : 81.0%
  Details                : Within budget: you have spent INR 4049.00 of INR 5000.00. Remaining balance: INR 951.00 (19.0% remaining).
```

---

## Programming Concepts Used

I designed this project to put core CSE1021 topics into practice:
- **Modular decomposition:** Splitting responsibilities into 7 separate files instead of one huge script.
- **Data structures:**
  - Lists of dictionaries for sequential records.
  - Tuples for immutable category choices and date verification arrays.
  - Sets for extracting unique categories dynamically without duplicates.
- **Control flow:** `while` loops for menu navigation and defensive inputs, `for` loops for traversals, and `if / elif / else` for budget evaluations.
- **Handwritten algorithms:** Accumulators for sums and counts, iterative comparisons for min/max, linear search, and Bubble Sort.
- **Defensive input parsing:** Wrapping data entry in `try...except ValueError` blocks to prevent unexpected terminal crashes.
- **File persistence:** Loading and writing formatted JSON data directly to local disk.

---

## Author & Academic Information

* **Student Name:** Pragya Singh
* **Course:** CSE1021 – Introduction to Problem Solving and Programming
* **School:** School of Computer Science and Engineering (SCOPE)
* **Institution:** Vellore Institute of Technology (VIT), Vellore
