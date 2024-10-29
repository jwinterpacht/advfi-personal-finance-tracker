from datetime import date
from typing import List, Dict

class SpendingReport:
    def __init__(self):
        self.startDate = date.min 
        self.endDate = date.min   
        self.totalSpending = 0.0
        self.expenses = [] 

    # Getters
    def getTotalSpending(self):
        return self.totalSpending
    
    def getExpenses(self):
        return self.expenses


    # Setters
    def setTotalSpending(self, totalSpending: float):
        self.totalSpending = totalSpending
    
    def setExpenses(self, expenses: List[Dict]):
        self.expenses = expenses



    def addExpense(self, amount: float, expenseDate: date, category: str, isRecurring: bool = False):
        expense = {
            "amount": amount,
            "expenseDate": expenseDate,
            "category": category,
            "isRecurring": isRecurring
        }
        self.expenses.append(expense)
        self.totalSpending += amount
    


    def filterByDateRange(self, left: date, right: date):
      
        filteredExpenses = [i for i in self.expenses if left <= i["expenseDate"] <= right]
        filteredReport = SpendingReport()
        filteredReport.setExpenses(filteredExpenses)
        filteredReport.setTotalSpending(sum(i["amount"] for i in filteredExpenses))
      
        return filteredReport

    def filterByCategory(self, category: str):
      
        filteredExpenses = [i for i in self.expenses if i["category"] == category]
        filteredReport = SpendingReport()
        filteredReport.setExpenses(filteredExpenses)
        filteredReport.setTotalSpending(sum(i["amount"] for i in filteredExpenses))
      
        return filteredReport

    def filterByRecurring(self, isRecurring: bool = True):
      
        filteredExpenses = [i for i in self.expenses if i["isRecurring"] == isRecurring]
        filteredReport = SpendingReport()
        filteredReport.setExpenses(filteredExpenses)
        filteredReport.setTotalSpending(sum(i["amount"] for i in filteredExpenses))
      
        return filteredReport



    def generateReport(self):
        reportSummary = {
            "totalSpending": self.totalSpending,
            "expenseCount": len(self.expenses),
            "expensesByCategory": {}
        }
        for expense in self.expenses:
            category = expense["category"]
            if category in reportSummary["expensesByCategory"]:
                reportSummary["expensesByCategory"][category] += expense["amount"]
            else:
                reportSummary["expensesByCategory"][category] = expense["amount"]

        return reportSummary
