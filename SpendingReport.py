from datetime import date
from typing import List
import TransactionList
import Transaction
import MainUI
from Report import Report

class SpendingReport(Report):
    def __init__(self, report_date: date, transaction_list: TransactionList):
        super().__init__(report_date)
        self._total_spending_last_month = 0.0
        self._spending_entries_last_month = []  # List to store spending amounts (floats)
        for spending in transaction_list._expense_transactions:
            if spending.get_is_within_last_month():
                self._spending_entries_last_month.append(spending)
                self._total_spending_last_month += spending.get_amount()
        self._total_spending = transaction_list.get_total_expenses()  # Default total spending is 0.0

    # getters
    def get_spending_entries_last_month(self):
        return self._spending_entries_last_month

    def get_total_spending(self):
        return self._total_spending
    
    def get_total_spending_last_month(self):
        return self._total_spending_last_month

    # setters
    def set_spending_entries_last_month(self, spending_entries_last_month: List[float]):
        self._spending_entries_last_month = spending_entries_last_month
        self._total_spending = sum(self.spending_entries_last_month)

    def set_total_spending(self, total_spending: float):
        self._total_spending = total_spending

    def set_total_spending_last_month(self, total_spending_last_month: float):
        self._total_spending_last_month = total_spending_last_month

    def generate_report(self):
        spending_report = f"spending Report\n{self._report_date}\n---------------\nTotal lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"
        for spending in self._spending_entries_last_month:
            spending_report += f"{spending.print_transaction()}\n"
        MainUI.MainUI.utility_print(spending_report)

    def to_string(self) -> str:
        spending_report = f"spending Report\n{self._report_date}\n---------------\nTotal lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"
        for spending in self._spending_entries_last_month:
            spending_report += f"{spending.print_transaction()}\n"
        return spending_report

    def get_header(self) -> str:
        header = f"spending Report\n{self._report_date}"
        return header
    
    def get_body(self) -> str:
        body = f"Total lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"        
        for spending in self._spending_entries_last_month:
            body += f"{spending.print_transaction()}\n"
        return body
