from datetime import date
from typing import List, Dict

class SpendingReport:
    def __init__(self):  
        self._total_spending = 0.0
        self._expenses = []

    # Getters
    def get_total_spending(self):
        return self._total_spending
    
    def getExpenses(self):
        return self._expenses


    # Setters
    def set_total_spending(self, total_spending: float):
        self._total_spending = total_spending
    
    def set_expenses(self, expenses):
        self._expenses = expenses
