# Project Statement: Personal Expense Tracker

**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Pragya Singh  
**Institution:** Vellore Institute of Technology (VIT), Vellore  

---

## 1. Problem Context

Living in a hostel or campus apartment at VIT, managing a monthly allowance is something almost every student struggles with. Between quick canteen lunches, Gazebo cold coffee and snacks, auto rides to Katpadi junction, printing lab observation sheets, buying textbooks, and mobile recharges, money slips away in small amounts every single day.

Because these payments are usually small UPI transfers or cash transactions (often ₹30 to ₹250), it is very easy to lose track. By the third or fourth week of the month, students frequently find their balances running dangerously low without knowing which purchases caused it.

Most existing expense tracking mobile apps have several annoying issues:
- They require creating accounts and remembering passwords.
- They demand intrusive permissions, such as reading SMS messages and notifications.
- They are full of advertisements and require an active internet connection.

For a student who just wants a fast, private, distraction-free way to log daily spending and stay within budget, these apps feel unnecessarily complicated. 

The **Personal Expense Tracker** addresses this problem by providing a lightweight, offline console application in Python. It lets students quickly log daily expenses, categorize them, check total and average spending, spot their biggest expenses, and see whether they are staying inside their monthly budget.

---

## 2. Project Scope

Developed as my project for **CSE1021 – Introduction to Problem Solving and Programming**, this application focuses on solving an everyday practical problem using standard Python concepts.

### Included in the Project
The application provides an interactive terminal menu that loops until the user chooses to exit. It includes built-in validation checks so that accidental mistakes—like entering letters for an amount or typing an invalid date—are caught cleanly without crashing the program.

Users can add, view, search, edit, and delete transactions. Searching can be done by category name, specific calendar date, month prefix, or a minimum rupee threshold. For analytics, the program calculates grand totals, transaction counts, averages, extremes, and category percentage shares with text progress bars. It also implements an optional Bubble Sort to rank expenses from highest to lowest.

For budgeting, the user can set a monthly allowance limit. The program compares actual spending against this limit and alerts the user whether they are safely under budget, right at the limit, or exceeding it. It can also export an overview report to a plain text file (`expense_report.txt`). All records persist across sessions via local JSON files (`expenses.json` and `budget.json`).

### Excluded from the Project
To keep the application lightweight, standalone, and easy to run during lab reviews, heavy database engines (like MySQL or MongoDB) were deliberately left out in favor of native JSON storage. Similarly, external data science packages (like Pandas or NumPy) were avoided so that all looping, summation, and sorting mechanics could be written and demonstrated from scratch. Cloud sync, external payment gateways, and network dependencies are also outside the scope of this project.

---

## 3. Intended Users

- **VIT Students:** Undergraduates looking for a fast, private way to track monthly allowances, canteen bills, and study materials without using bloated mobile apps.
- **First-Year Programming Students:** Learners who want to see how lists, dictionaries, tuples, sets, and control loops come together in a practical application.
- **Minimalist Users:** Anyone who prefers an offline terminal tool over commercial mobile apps.

---

## 4. Key Highlights

The application was designed to be simple, crash-resistant, and completely self-contained. It requires zero external installations beyond Python itself. Every algorithm is written by hand so that the logic is completely transparent and easy to explain during academic reviews.
