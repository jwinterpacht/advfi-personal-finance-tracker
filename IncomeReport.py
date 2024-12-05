from datetime import date
from typing import List

class IncomeReport:
    def __init__(self):
        self._totalIncome = 0.0  # Default total income is 0.0
        self._incomeEntries = []  # List to store income amounts (floats)

    # getters
    def getIncomeEntries(self):
        return self._incomeEntries

    def getTotalIncome(self):
        return self._totalIncome

    # setters
    def setIncomeEntries(self, incomeEntries: List[float]):
        self._incomeEntries = incomeEntries
        self._totalIncome = sum(self.incomeEntries)

    def setTotalIncome(self, totalIncome: float):
        self._totalIncome = totalIncome
