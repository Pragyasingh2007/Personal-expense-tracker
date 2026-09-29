# Problem Statement: Personal Expense Tracker

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

---

## 1. Background & Context

For most students joining VIT, living in a hostel or campus accommodation is the first time managing personal expenses independently. At the beginning of the month, we receive an allowance or pocket money intended to last the next thirty days.

From that allowance, money goes out in small amounts almost every single day. There are canteen lunches, cold coffee and samosas at Gazebo, fresh juice after class, printed lab records, project manuals, scientific calculators, notebooks, auto rides to and from Katpadi railway station, shared autos, and monthly mobile data recharges.

Because these payments are usually small UPI transfers or cash transactions (often ₹40 to ₹250), we rarely stop to write them down or think about them.

---

## 2. The Problem

When you don't track small expenses, you run into three main issues:
- **Unexplained cash shortages:** By the third or fourth week of the month, the balance is almost empty and there is no clear record of where the money went.
- **Distorted spending assumptions:** Without categorizing spending, it is easy to assume money went towards textbooks when a large portion was actually spent on evening snacks and food deliveries.
- **Budget surprises:** Without a tracking tool, you only realize you have exceeded your budget when a UPI payment fails or your bank balance reaches zero.

While mobile apps for expense tracking exist, they are often frustrating for students. They require creating accounts and remembering passwords. They request invasive permissions to read SMS messages and banking alerts. Many are cluttered with advertisements, subscription upsells, and popups. Worst of all, they usually refuse to work without active internet.

Students need a simple, private tool: open the terminal, enter the expense in a few seconds, check the remaining balance, and get back to studying.

---

## 3. The Proposed Solution

The **Personal Expense Tracker** is a lightweight, offline console application in Python created to solve this problem.

It lets a student:
- Quickly log expenses with date, category, amount, and description.
- View previous spending in an aligned table format.
- Search expenses by category or date/month.
- Filter for larger purchases above a certain threshold (e.g., above ₹500).
- Edit previously entered details or delete unwanted entries.
- View instant spending summaries: total expenditure, transaction count, average expense, highest and lowest expenses, and category breakdowns with ASCII progress bars.
- Set a monthly budget and receive clear status feedback showing remaining balance or overspent amount.
- Export an overview report to a text file (`expense_report.txt`).

---

## 4. Academic Relevance for CSE1021

In **CSE1021 – Introduction to Problem Solving and Programming**, the focus is on algorithmic problem solving:
- Splitting the system into focused modules (`main`, `expense_manager`, `analysis`, `budget`, `reports`, `validation`, `data`) rather than writing a single huge file.
- Choosing appropriate data structures: lists for ordered sequences of records, tuples for immutable categories, sets for distinct category lookups, and dictionaries for key-value fields.
- Writing core algorithms from scratch: manually implementing summation, counting, min/max finding, linear search, and bubble sort without relying on third-party packages.
