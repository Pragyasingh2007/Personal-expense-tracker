# Project Objectives: Personal Expense Tracker

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

---

## 1. What I Set Out to Build

The main aim of this project was to make a straightforward, offline console tool that helps students keep track of daily cash and UPI spending, stick to their monthly pocket money, and see where their money goes. At the same time, I wanted to put into practice the core concepts we studied in CSE1021, writing the logic from scratch without leaning on external libraries.

---

## 2. Practical Goals

When designing the application, I focused on three main practical areas:

### Handling Everyday Expenses
First and foremost, logging an expense needed to be quick and foolproof. The program asks for the date, category, amount, and note, giving each record an automatically incremented ID. I built defensive validation right into the input prompts so that typing letters instead of numbers or entering impossible calendar days won't crash the terminal. Beyond adding expenses, I wanted students to be able to view their ledger in a clean table, search by category name or date prefix, filter out small transactions to spot large purchases, and edit or delete previous entries whenever needed.

### Core Calculations and Math
Instead of calling pre-built statistical packages, I wanted to write all the computational routines by hand:
- Summing total expenditure and counting transactions with explicit loops.
- Calculating average spending per transaction with guard conditions against division by zero.
- Finding the highest and lowest single expense records by scanning through the list.
- Grouping expenses by category to calculate both monetary totals and percentage shares.
- Rendering simple text-based progress bars to show spending distributions visually in the console.
- Implementing the Bubble Sort algorithm to order records from most expensive to least expensive.

### Budgeting and Local Storage
Managing an allowance requires knowing how much you have left before the month ends. The program lets the user set a monthly spending limit and compares it against total spending to show whether you are still under budget, right at the limit, or over budget. It also allows exporting a formatted summary report to `expense_report.txt`. Everything saves automatically to local JSON files (`expenses.json` and `budget.json`) so transactions aren't lost when you close the terminal.

---

## 3. Academic Learning Outcomes

From a coursework perspective, this project helped me gain hands-on practice with several key topics:
- **Modular decomposition:** Organizing logic into 7 specialized files instead of dumping everything into one huge script.
- **Control structures:** Using `while` loops for menu navigation, `for` loops for iterating over transactions, and multi-way `if / elif / else` blocks for budget classification and user choices.
- **Data structures in practice:** 
  - Using lists to hold sequential expense dictionaries.
  - Using tuples for immutable category names and month lengths.
  - Using sets to extract distinct category names dynamically.
  - Using dictionaries to store structured record fields and accumulate category sums.
- **Error resilience:** Wrapping conversions in `try...except ValueError` blocks so invalid user inputs are handled gracefully.
