import Transaction
from datetime import date

class TransactionList:
    def __init__(self):
        self._income_transactions = []
        self._expense_transactions = []
        self._total_income = 0
        self._total_expenses = 0
        self._transaction_count = 0 #this is used to set transaction IDs
    
    def add_income_transaction(self, income: Transaction) -> None:
        self._transaction_count += 1  #increment our transaction count
        income.set_transaction_id(self._transaction_count)

        self._income_transactions.append(income)
        self._total_income += income._amount
    
    def add_expense_transaction(self, expense: Transaction) -> None:
        self._transaction_count += 1  #increment our transaction count
        expense.set_transaction_id(self._transaction_count)

        self._expense_transactions.append(expense)
        self._total_expenses += expense._amount

    def remove_income_transaction(self, transaction_id: int) -> bool:
        for income in self._income_transactions:
            if income._transaction_ID == transaction_id:
                print(f"From list: {income._transaction_ID}")
                print(f"From passed-in: {transaction_id}")
                self._income_transactions.remove(income)
                self._total_income -= income._amount
                return True
        return False
    
    def remove_expense_transaction(self, transaction_id: int) -> bool:
        for expense in self._expense_transactions:
            if expense.Transaction.get_transaction_id() == transaction_id:
                self._income_transactions.remove(expense)
                self.total_income -= expense._amount
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
        return self._total_income
    
    # Return the total expenses
    def get_total_expenses(self) -> float:
        return self._total_expenses
    
    def get_transaction_count(self) -> float:
        return self._transaction_count
    
    def print_expenses(self) -> None:
        print("\nExpense List:")
        for expense in self._expense_transactions:
            expense.print_transaction()
    
    def print_incomes(self) -> None:
        print("\nIncome List:")
        for income in self._income_transactions:
            income.print_transaction()
    
    def print_transactions(self) -> None:
        TransactionList.print_expenses(self)
        TransactionList.print_incomes(self)
        