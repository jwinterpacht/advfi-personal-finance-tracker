from datetime import date
from typing import List

class IncomeReport:
    def __init__(self):
        self._report_date: date = date.min  # Default date: 00/00/0000
        self._total_income: float = 0.0     # Default total income is 0.0
        self._income_entries: List[float] = []  # List to store income amounts (floats)

  
    #Getters
    def get_report_date(self):
        return self._report_date
    
    def get_income_entries(self):
        return self._income_entries

    def get_total_income(self):
        return self._total_income

  
    #Setters
    def set_report_date(self, report_date: date):
        self._report_date = report_date

    def set_income_entries(self, income_entries: List[float]):
        self._income_entries = income_entries
        self._total_income = sum(self._income_entries)

    def set_total_income(self, total_income: float):
        self._total_income = total_income

  
    #Generates Report
    def generate_report(self):
       
        return self
