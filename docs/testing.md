# Testing Documentation & Test Cases

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

---

## 1. How I Tested the Project

While building the application, I wanted to make sure it wouldn't crash when someone enters unexpected data. I used Python's built-in `unittest` module to write automated tests for all core functions across `validation.py`, `expense_manager.py`, `analysis.py`, `budget.py`, and `data.py`.

My testing focused on practical edge cases:
- Entering letters or symbols where a number is expected (like typing 'two hundred' or blank spaces for an amount).
- Boundary conditions for dates, such as checking that February 29th works in 2024 (a leap year) but is rejected in 2026.
- Out-of-bounds menu numbers and negative amounts.
- Making sure calculations (like average spending) don't trigger a `ZeroDivisionError` when the expense list is empty.
- Verifying that saved records reload accurately from the JSON files.

---

## 2. Test Execution Summary

* **Framework:** Python Standard Library `unittest`
* **Test File:** `tests/test_expense_tracker.py`
* **Total Unit Tests:** 30
* **Tests Passed:** 30
* **Tests Failed:** 0
* **Execution Time:** ~0.005 seconds
* **Pass Rate:** 100%

---

## 3. Test Cases Matrix

| Test ID | Module / Feature | Description | Input Data | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Validation | Valid positive expense amount | `amount_str = "150.50"` | `(True, 150.50)` | **PASS** |
| **TC-02** | Validation | Non-numeric string amount | `amount_str = "abc"` | `(False, ...valid number...)` | **PASS** |
| **TC-03** | Validation | Negative expense amount | `amount_str = "-50.00"` | `(False, ...greater than zero...)` | **PASS** |
| **TC-04** | Validation | Zero expense amount | `amount_str = "0"` | `(False, ...greater than zero...)` | **PASS** |
| **TC-05** | Validation | Empty whitespace amount | `amount_str = "   "` | `(False, ...cannot be empty...)` | **PASS** |
| **TC-06** | Validation | Valid calendar date | `date_str = "2026-09-28"` | `(True, "2026-09-28")` | **PASS** |
| **TC-07** | Validation | Leap year date validation | `date_str = "2024-02-29"` | `(True, "2024-02-29")` | **PASS** |
| **TC-08** | Validation | Non-leap year Feb 29 date | `date_str = "2026-02-29"` | `(False, ...Day must be between 01 and 28...)` | **PASS** |
| **TC-09** | Validation | Invalid month number | `date_str = "2026-13-10"` | `(False, ...Month must be between 01 and 12...)` | **PASS** |
| **TC-10** | Validation | Empty text description | `text = "   "` | `(False, ...cannot be empty...)` | **PASS** |
| **TC-11** | Validation | Valid menu choice | `choice = "5", min=1, max=9` | `(True, 5)` | **PASS** |
| **TC-12** | Validation | Out-of-bounds menu choice | `choice = "12", min=1, max=9` | `(False, ...)` | **PASS** |
| **TC-13** | Expense Manager | Add new expense record | Date: 2026-09-12, Cat: Books, Amt: 350.0 | New record with ID 4 added | **PASS** |
| **TC-14** | Expense Manager | Search expense by category | Query: `"food"` | All matching "Food" records returned | **PASS** |
| **TC-15** | Expense Manager | Search expense by date | Query: `"2026-09-05"` | Record with matching date returned | **PASS** |
| **TC-16** | Expense Manager | Filter by minimum amount | `min_amount = 250.0` | Records with amount >= 250.0 returned | **PASS** |
| **TC-17** | Expense Manager | Update expense fields | ID: 1, new_amt: 150.0, new_desc: "Brunch" | Record updated in-place | **PASS** |
| **TC-18** | Expense Manager | Delete expense record | ID: 2 | Record removed from list | **PASS** |
| **TC-19** | Expense Manager | Extract unique categories | Records with categories Food, Travel | Set containing `{"Food", "Travel"}` | **PASS** |
| **TC-20** | Analysis | Count expenses algorithm | List of 3 records | Count = 3 | **PASS** |
| **TC-21** | Analysis | Total summation algorithm | Amounts: 100.0, 400.0, 300.0 | Sum = 800.0 | **PASS** |
| **TC-22** | Analysis | Average calculation | Total: 800.0, Count: 3 | Average = 266.67 | **PASS** |
| **TC-23** | Analysis | Maximum finding algorithm | Amounts: 100.0, 400.0, 300.0 | Highest record: ID 2 (400.0) | **PASS** |
| **TC-24** | Analysis | Minimum finding algorithm | Amounts: 100.0, 400.0, 300.0 | Lowest record: ID 1 (100.0) | **PASS** |
| **TC-25** | Analysis | Bubble sort by amount | Amounts: 100.0, 400.0, 300.0 | Sorted: [400.0, 300.0, 100.0] | **PASS** |
| **TC-26** | Budget | Spending under budget | Budget: 5000.0, Spent: 3200.0 | Status: `UNDER_BUDGET`, Diff: 1800.0 | **PASS** |
| **TC-27** | Budget | Spending equal to budget | Budget: 5000.0, Spent: 5000.0 | Status: `EXACT_BUDGET`, Diff: 0.0 | **PASS** |
| **TC-28** | Budget | Spending over budget | Budget: 5000.0, Spent: 5500.0 | Status: `OVER_BUDGET`, Diff: -500.0 | **PASS** |
| **TC-29** | Persistence | Save & load roundtrip | Save list with 1 item to file | Loaded item matches saved data | **PASS** |
| **TC-30** | Persistence | Missing file fallback | Load from non-existent file | Initializes default sample data | **PASS** |

---

## 4. Running the Tests

To run the unit test suite:
```powershell
python -m unittest tests/test_expense_tracker.py
```

To see each individual test name as it executes:
```powershell
python -m unittest -v tests/test_expense_tracker.py
```
