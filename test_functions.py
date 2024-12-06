import unittest
from datetime import datetime
from TransactionList import TransactionList
import Transaction
import Operations

# Frank's Use Cases (Import file from CSV, Retrieve Transaction, and Remove Transaction)

class TestSpendingManagement(unittest.TestCase):

    def setUp(self):
        # Initialize the transaction list and other prerequisites
        self.transaction_list = TransactionList()
        self.file_name = "CSVTest.csv"

    def test_create_and_add_transaction(self):
        # Test adding a transaction directly
        Operations.Operations.create_and_add_transaction(
            transaction_list=self.transaction_list,
            amount=-500,
            date="05/23/24",  # Correct format
            desc="Tow",
            type="expense"
        )
        self.assertEqual(len(self.transaction_list._expense_transactions), 1)
        self.assertEqual(self.transaction_list._total_expenses, -500)

    def test_spending_management_menu_import_spending_CSV_operations(self):
        # Test importing transactions from a CSV file
        result = Operations.Operations.spending_management_menu_import_spending_CSV_operations(
            fileName=self.file_name,
            transaction_list=self.transaction_list
        )
        self.assertTrue(result)  # Ensure the function returns True on success
        self.assertGreater(len(self.transaction_list._income_transactions) + len(self.transaction_list._expense_transactions), 0)

class TestTransactionCount(unittest.TestCase):

    def setUp(self):
        # Create a TransactionList instance before each test
        self.transaction_list = TransactionList()

    def test_transaction_count_empty(self):
        # Test that the transaction count is 0 when no transactions have been added
        count = Operations.Operations.retrieve_transaction_count(self.transaction_list)
        self.assertEqual(count, 0)

    def test_transaction_count_after_adding_transactions(self):
        # Test that the transaction count increases after adding transactions
        Operations.Operations.create_and_add_transaction(
            transaction_list=self.transaction_list,
            amount=100,
            date="05/23/24",
            desc="Deposit",
            type="income"
        )  # Add an income transaction
        Operations.Operations.create_and_add_transaction(
            transaction_list=self.transaction_list,
            amount=-50,
            date="05/24/24",
            desc="Withdrawal",
            type="expense"
        )  # Add an expense transaction

        count = Operations.Operations.retrieve_transaction_count(self.transaction_list)
        self.assertEqual(count, 2)

    def test_transaction_count_after_removing_transactions(self):
        # Test that the transaction count decreases after removing a transaction
        Operations.Operations.create_and_add_transaction(
            transaction_list=self.transaction_list,
            amount=100,
            date="05/23/24",
            desc="Deposit",
            type="income"
        )
        Operations.Operations.create_and_add_transaction(
            transaction_list=self.transaction_list,
            amount=-50,
            date="05/24/24",
            desc="Withdrawal",
            type="expense"
        )

        # Remove the income transaction by its transaction ID
        self.transaction_list.remove_income_transaction(1)  # Pass the ID directly

        # Verify the transaction count is updated
        count = len(self.transaction_list._income_transactions) + len(self.transaction_list._expense_transactions)
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
