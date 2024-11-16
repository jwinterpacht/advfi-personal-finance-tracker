import Transaction
import Report
import UserAccount
#import Budget
from datetime import date
#import SavingsGoalList #DELETE if we remove SavingsGoals (11-5-2024)

#11-5: updated to be compatible with associated use cases && added params to __init__

''' #Commented out because now we have actual Transaction class
# Transaction Class (for testing) to store each transaction
class Transaction:
    def __init__(self, transaction_id, description, amount):
        self.transaction_id = transaction_id
        self.description = description
        self.amount = amount
'''

# TransactionList Class used for storing income and expenses
class TransactionList:
    def __init__(self, total_income = 0, total_expenses = 0):
        self.income_transactions = [] #not passed in as param. Should it?
        self.expense_transactions = [] #not passed in as param. Should it?
        self.total_income = total_income
        self.total_expenses = total_expenses
        #self.report = Report.Report(date(1,1,1)) # No actual report stored during initalization.

    # Adds a new income transaction and updates total income
    def add_income_transaction(self, transaction) -> None:
        self.income_transactions.append(transaction)
        self.total_income += transaction.amount

    # Removes an income transaction by its ID, returning true if succeeded and false is failed
    def remove_income_transaction(self, transaction_id: int) -> bool:
        for transaction in self.income_transactions:
            # If we find the ID update info
            if transaction.transaction_id == transaction_id:
                self.income_transactions.remove(transaction)
                self.total_income -= transaction.amount
                return True
        return False
    
    # Adds a new expense transaction and updates total expenses
    def add_expense_transaction(self, transaction: Transaction) -> None:
        self.expense_transactions.append(transaction)
        self.total_expenses += transaction.amount

    # Removes an expense by its ID, returns true if succeeded and false if failed
    def remove_expense_transaction(self, transaction_id: int) -> bool:
        for transaction in self.expense_transactions:
            # If we find the ID update info
            if transaction.transaction_id == transaction_id:
                self.expense_transactions.remove(transaction)
                self.total_expenses -= transaction.amount
                return True
        return False

    # Finds and returns transacton by its ID from income or expense transaction
    def get_transaction(self, transaction_id: int) -> Transaction:
        # Add the two lengths to find which ID they're in
        for transaction in self.income_transactions + self.expense_transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None
    
    # Return the total income
    def get_total_income(self) -> float:
        return self.total_income
    
    # Return the total expenses
    def get_total_expenses(self) -> float:
        return self.total_expenses
    
    def set_report(self, new_report: Report):
        self.report = new_report
    
# Testing
#transaction_list = TransactionList()
'''
# Add transactions (ID, Description, Value)
income1 = Transaction(1, "Salary", 5000)
expense1 = Transaction(2, "Rent", 1500)

transaction_list.add_income_transaction(income1)
transaction_list.add_expense_transaction(expense1)

# Display totals for income and expense
print(f"Total Income: {transaction_list.get_total_income()}")
print(f"Total Expenses: {transaction_list.get_total_expenses()}")

# Removing a transaction 
transaction_list.remove_income_transaction(1)

# Display totals after removal
print(f"Total Income after removal: {transaction_list.get_total_income()}")
print(f"Total Expenses after removal: {transaction_list.get_total_expenses()}")
'''