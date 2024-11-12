# Transaction Class to store each transaction
class Transaction:
    def __init__(self, transaction_id, description, amount):
        self.transaction_id = transaction_id
        self.description = description
        self.amount = amount

# CSV File
# 1: Open file 2: read from file 3: while reading store the variables into an transactionObject 4: create a list of transactionObjects  5: Populate add income and add expense based on the objects 
    # Handling Empty values in the rows only two ,'s are accepted? transaction_id, description, amount
    # 
# Transaction removal must keep the next highest ID no replacing old removed IDs (remove id 5, add new transaction must be the next highest id available not id 5)

# TransactionList Class used for storing income and expenses
class TransactionList:
    def __init__(self):
        self.income_transactions = []
        self.expense_transactions = []
        self.total_income = 0.0
        self.total_expenses = 0.0

    # Adds a new income transaction and updates total income
    def add_income_transaction(self, transaction: Transaction) -> None:
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

# Testing
transaction_list = TransactionList()

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