from datetime import date
from typing import List, Dict
import TransactionList
import MainUI

class SpendingReport:
    def __init__(self, transaction_list: TransactionList):
        super().__init__()
        self._total_spending_last_month = 0.0
        self._expense_entries_last_month = []
        for expense in transaction_list._expense_transactions:
            if expense.get_is_within_last_month():
                self._expense_entries_last_month.append(expense)
                self._total_spending_last_month += expense.get_amount()
        self._total_spending = transaction_list.get_total_expenses()

    # Getters
    def get_expense_entries_last_month(self):
        return self._expense_entries_last_month

    def get_total_spending(self):
        return self._total_spending
    
    def get_total_spending_last_month(self):
        return self._total_spending_last_month


    # Setters
    def set_expense_entries_last_month(self, expense_entries_last_month: List[float]):
        self._expense_entries_last_month = expense_entries_last_month
        self._total_spending = sum(self.income_entries_last_month)

    def set_total_spending(self, total_spending: float):
        self._total_spending = total_spending
    
    def set_total_spending_last_month(self, total_spending_last_month: float):
        self._total_spending_last_month = total_spending_last_month

    def generate_report(self):
        spending_report = f"Spending Report\n-----------------\nTotal lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"
        for expense in self._expense_entries_last_month:
            spending_report += f"{expense.print_transaction()}\n"
        MainUI.MainUI.utility_print(spending_report)

    def to_string(self) -> str:
        spending_report = f"Spending Report\nTotal lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"
        for expense in self._expense_entries_last_month:
            spending_report += f"{expense.print_transaction()}\n"
        return spending_report
