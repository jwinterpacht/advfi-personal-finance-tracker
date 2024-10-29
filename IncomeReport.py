from datetime import date
from typing import List

class IncomeReport:
    def __init__(self):
        self.reportDate = date.min  # Default date: 00/00/0000
        self.totalIncome = 0.0  # Default total income is 0.0
        self.incomeEntries = []  # List to store income amounts (floats)

    # Getters
    def getReportDate(self):
        return self.reportDate

    def getIncomeEntries(self):
        return self.incomeEntries

    def getTotalIncome(self):
        return self.totalIncome

    # Setters
    def setReportDate(self, reportDate: date):
        self.reportDate = reportDate

    def setIncomeEntries(self, incomeEntries: List[float]):
        self.incomeEntries = incomeEntries
        self.totalIncome = sum(self.incomeEntries)

    def setTotalIncome(self, totalIncome: float):
        self.totalIncome = totalIncome

    # Generates Report
    def generateReport(self):
        reportSummary = {
            "reportDate": self.reportDate,
            "totalIncome": self.totalIncome,
            "incomeEntryCount": len(self.incomeEntries),
            "incomeEntries": self.incomeEntries
        }

        return reportSummary
