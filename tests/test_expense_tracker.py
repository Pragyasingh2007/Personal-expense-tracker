"""
test_expense_tracker.py
Unit tests for Personal Expense Tracker.
Tests validation, expense operations, calculations, budgeting, and file saving.
Author: Pragya Singh
"""

import os
import unittest

import analysis
import budget
import data
import expense_manager
import validation


class TestValidationModule(unittest.TestCase):
    """Test suite for validation functions."""

    def test_validate_amount_valid(self):
        valid, val = validation.validate_amount("150.50")
        self.assertTrue(valid)
        self.assertEqual(val, 150.50)

    def test_validate_amount_invalid_text(self):
        valid, msg = validation.validate_amount("abc")
        self.assertFalse(valid)
        self.assertIn("valid number", msg)

    def test_validate_amount_negative(self):
        valid, msg = validation.validate_amount("-50")
        self.assertFalse(valid)
        self.assertIn("greater than zero", msg)

    def test_validate_amount_zero(self):
        valid, msg = validation.validate_amount("0")
        self.assertFalse(valid)
        self.assertIn("greater than zero", msg)

    def test_validate_date_valid(self):
        valid, dt = validation.validate_date("2026-09-28")
        self.assertTrue(valid)
        self.assertEqual(dt, "2026-09-28")

    def test_validate_date_leap_year(self):
        # 2024 is a leap year (Feb 29 is valid)
        valid, dt = validation.validate_date("2024-02-29")
        self.assertTrue(valid)
        self.assertEqual(dt, "2024-02-29")

        # 2026 is not a leap year (Feb 29 is invalid)
        valid, msg = validation.validate_date("2026-02-29")
        self.assertFalse(valid)
        self.assertIn("Day must be between 01 and 28", msg)

    def test_validate_date_invalid_format(self):
        valid, msg = validation.validate_date("28-09-2026")
        self.assertFalse(valid)

    def test_validate_date_invalid_month(self):
        valid, msg = validation.validate_date("2026-13-10")
        self.assertFalse(valid)
        self.assertIn("Month must be between 01 and 12", msg)

    def test_validate_non_empty(self):
        valid, txt = validation.validate_non_empty("  Snacks  ", "Description")
        self.assertTrue(valid)
        self.assertEqual(txt, "Snacks")

        valid, msg = validation.validate_non_empty("   ", "Description")
        self.assertFalse(valid)
        self.assertIn("cannot be empty", msg)

    def test_validate_menu_choice(self):
        valid, choice = validation.validate_menu_choice("5", 1, 9)
        self.assertTrue(valid)
        self.assertEqual(choice, 5)

        valid, msg = validation.validate_menu_choice("12", 1, 9)
        self.assertFalse(valid)


class TestExpenseManagerModule(unittest.TestCase):
    """Test suite for expense CRUD and search operations."""

    def setUp(self):
        self.sample_expenses = [
            {"id": 1, "date": "2026-09-01", "category": "Food", "amount": 100.0, "description": "Breakfast"},
            {"id": 2, "date": "2026-09-05", "category": "Travel", "amount": 250.0, "description": "Cab"},
            {"id": 3, "date": "2026-09-10", "category": "Food", "amount": 500.0, "description": "Dinner"},
        ]

    def test_add_expense(self):
        new_rec = expense_manager.add_expense(
            self.sample_expenses, "2026-09-12", "Books", 350.0, "Python Book"
        )
        self.assertEqual(new_rec["id"], 4)
        self.assertEqual(len(self.sample_expenses), 4)
        self.assertEqual(self.sample_expenses[-1]["description"], "Python Book")

    def test_find_expense_by_id(self):
        rec, idx = expense_manager.find_expense_by_id(self.sample_expenses, 2)
        self.assertIsNotNone(rec)
        self.assertEqual(rec["category"], "Travel")
        self.assertEqual(idx, 1)

        rec_none, idx_none = expense_manager.find_expense_by_id(self.sample_expenses, 999)
        self.assertIsNone(rec_none)
        self.assertEqual(idx_none, -1)

    def test_search_by_category(self):
        results = expense_manager.search_by_category(self.sample_expenses, "food")
        self.assertEqual(len(results), 2)
        for r in results:
            self.assertEqual(r["category"], "Food")

    def test_search_by_date(self):
        results = expense_manager.search_by_date(self.sample_expenses, "2026-09-05")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], 2)

        results_month = expense_manager.search_by_date(self.sample_expenses, "2026-09")
        self.assertEqual(len(results_month), 3)

    def test_filter_by_min_amount(self):
        filtered = expense_manager.filter_by_min_amount(self.sample_expenses, 250.0)
        self.assertEqual(len(filtered), 2)
        self.assertTrue(all(e["amount"] >= 250.0 for e in filtered))

    def test_update_expense(self):
        updated = expense_manager.update_expense(
            self.sample_expenses, expense_id=1, new_amount=150.0, new_description="Brunch"
        )
        self.assertTrue(updated)
        rec, _ = expense_manager.find_expense_by_id(self.sample_expenses, 1)
        self.assertEqual(rec["amount"], 150.0)
        self.assertEqual(rec["description"], "Brunch")

    def test_delete_expense(self):
        deleted = expense_manager.delete_expense(self.sample_expenses, 2)
        self.assertTrue(deleted)
        self.assertEqual(len(self.sample_expenses), 2)
        rec, _ = expense_manager.find_expense_by_id(self.sample_expenses, 2)
        self.assertIsNone(rec)

    def test_get_unique_categories(self):
        cats = expense_manager.get_unique_categories(self.sample_expenses)
        self.assertIsInstance(cats, set)
        self.assertEqual(cats, {"Food", "Travel"})


class TestAnalysisModule(unittest.TestCase):
    """Test suite for analytics, summation, min/max, and sorting."""

    def setUp(self):
        self.sample_expenses = [
            {"id": 1, "date": "2026-09-01", "category": "Food", "amount": 100.0, "description": "Tea"},
            {"id": 2, "date": "2026-09-05", "category": "Travel", "amount": 400.0, "description": "Bus"},
            {"id": 3, "date": "2026-09-10", "category": "Food", "amount": 300.0, "description": "Lunch"},
        ]

    def test_count_expenses(self):
        self.assertEqual(analysis.count_expenses(self.sample_expenses), 3)
        self.assertEqual(analysis.count_expenses([]), 0)

    def test_calculate_total_expense(self):
        self.assertEqual(analysis.calculate_total_expense(self.sample_expenses), 800.0)
        self.assertEqual(analysis.calculate_total_expense([]), 0.0)

    def test_calculate_average_expense(self):
        self.assertAlmostEqual(analysis.calculate_average_expense(self.sample_expenses), 266.67, places=2)
        self.assertEqual(analysis.calculate_average_expense([]), 0.0)

    def test_find_highest_expense(self):
        highest = analysis.find_highest_expense(self.sample_expenses)
        self.assertIsNotNone(highest)
        self.assertEqual(highest["id"], 2)
        self.assertEqual(highest["amount"], 400.0)
        self.assertIsNone(analysis.find_highest_expense([]))

    def test_find_lowest_expense(self):
        lowest = analysis.find_lowest_expense(self.sample_expenses)
        self.assertIsNotNone(lowest)
        self.assertEqual(lowest["id"], 1)
        self.assertEqual(lowest["amount"], 100.0)
        self.assertIsNone(analysis.find_lowest_expense([]))

    def test_category_totals(self):
        totals = analysis.calculate_category_totals(self.sample_expenses)
        self.assertEqual(totals["Food"], 400.0)
        self.assertEqual(totals["Travel"], 400.0)

    def test_category_percentages(self):
        totals = {"Food": 400.0, "Travel": 400.0}
        pcts = analysis.calculate_category_percentages(totals, 800.0)
        self.assertEqual(pcts["Food"], 50.0)
        self.assertEqual(pcts["Travel"], 50.0)

    def test_sort_expenses_by_amount(self):
        desc = analysis.sort_expenses_by_amount(self.sample_expenses, descending=True)
        self.assertEqual(desc[0]["amount"], 400.0)
        self.assertEqual(desc[1]["amount"], 300.0)
        self.assertEqual(desc[2]["amount"], 100.0)

        asc = analysis.sort_expenses_by_amount(self.sample_expenses, descending=False)
        self.assertEqual(asc[0]["amount"], 100.0)
        self.assertEqual(asc[2]["amount"], 400.0)


class TestBudgetModule(unittest.TestCase):
    """Test suite for budget evaluation under various spending conditions."""

    def test_budget_under_limit(self):
        res = budget.evaluate_budget(5000.0, 3200.0)
        self.assertEqual(res["status"], "UNDER_BUDGET")
        self.assertEqual(res["difference"], 1800.0)
        self.assertEqual(res["percentage_used"], 64.0)

    def test_budget_exact_reached(self):
        res = budget.evaluate_budget(5000.0, 5000.0)
        self.assertEqual(res["status"], "EXACT_BUDGET")
        self.assertEqual(res["difference"], 0.0)
        self.assertEqual(res["percentage_used"], 100.0)

    def test_budget_exceeded(self):
        res = budget.evaluate_budget(5000.0, 5500.0)
        self.assertEqual(res["status"], "OVER_BUDGET")
        self.assertEqual(res["difference"], -500.0)
        self.assertEqual(res["percentage_used"], 110.0)


class TestDataPersistence(unittest.TestCase):
    """Test suite for file persistence logic."""

    def test_save_and_load_roundtrip(self):
        test_file = "test_temp_expenses.json"
        data_to_save = [
            {"id": 1, "date": "2026-09-01", "category": "Food", "amount": 120.0, "description": "Test"}
        ]
        try:
            save_ok = data.save_expenses(data_to_save, filepath=test_file)
            self.assertTrue(save_ok)
            loaded = data.load_expenses(filepath=test_file)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0]["amount"], 120.0)
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
