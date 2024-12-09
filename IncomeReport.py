from datetime import date
from typing import List
import TransactionList
import Transaction
import MainUI

class IncomeReport:
    def __init__(self, transaction_list: TransactionList):
        super().__init__()
        self._total_income_last_month = 0.0
        self._income_entries_last_month = []  # List to store income amounts (floats)
        for income in transaction_list._income_transactions:
            if income.get_is_within_last_month():
                self._income_entries_last_month.append(income)
                self._total_income_last_month += income.get_amount()
        self._total_income = transaction_list.get_total_income()  # Default total income is 0.0

    # getters
    def get_income_entries_last_month(self):
        return self._income_entries_last_month

    def get_total_income(self):
        return self._total_income
    
    def get_total_income_last_month(self):
        return self._total_income_last_month

    # setters
    def set_income_entries_last_month(self, income_entries_last_month: List[float]):
        self._income_entries_last_month = income_entries_last_month
        self._total_income = sum(self.income_entries_last_month)

    def set_total_income(self, total_income: float):
        self._total_income = total_income

    def set_total_income_last_month(self, total_income_last_month: float):
        self._total_income_last_month = total_income_last_month

    def generate_report(self):
        income_report = f"Income Report\n---------------\nTotal lifetime income: ${self._total_income}\n\nTotal income from last month: ${self._total_income_last_month}\n\nEach income entry from last month:\n"
        for income in self._income_entries_last_month:
            income_report += f"{income.print_transaction()}\n"
        MainUI.MainUI.utility_print(income_report)

    def to_string(self) -> str:
        income_report = f"Income Report\nTotal lifetime income: ${self._total_income}\n\nTotal income from last month: ${self._total_income_last_month}\n\nEach income entry from last month:\n"
        for income in self._income_entries_last_month:
            income_report += f"{income.print_transaction()}\n"
        return income_report
