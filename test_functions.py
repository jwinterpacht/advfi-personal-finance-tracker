import unittest
from datetime import datetime
from TransactionList import TransactionList
import Transaction
import Operations

# Frank's Use Cases (Import file from CSV, Retrieve Transaction, and Remove Transaction)

class TestSpendingManagement(unittest.TestCase):

    def setUp(self):
        # Set up the environment for testing
        self.transaction_list = TransactionList()
        self.file_name = "CSVTest.csv"  # Ensure this file is in the same directory

    def test_spending_management_menu_import_spending_CSV_operations(self):
        # Test the CSV import function
        result = Operations.Operations.spending_management_menu_import_spending_CSV_operations(
            fileName=self.file_name,
            transaction_list=self.transaction_list
        )

        # Validate transactions are imported correctly
        total_transactions = (
            len(self.transaction_list._income_transactions) +
            len(self.transaction_list._expense_transactions)
        )
        self.assertGreater(total_transactions, 0, "No transactions were imported.")
        
        # Optional: Print a summary for debugging
        print("Income Transactions:", self.transaction_list.get_total_income())
        print("Expense Transactions:", self.transaction_list.get_total_expenses())

if __name__ == "__main__":
    unittest.main()

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
