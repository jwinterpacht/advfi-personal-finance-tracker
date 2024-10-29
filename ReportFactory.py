'''
ReportFactory class
By Jonah Raef
10-24-2024
'''

from datetime import date
from datetime import datetime

import Report
#imports will work when classes are made
import FinancialHealthReport
import IncomeReport
import SpendingReport

class ReportFactory(Report):
    def __init__(self, reportDate: date = date(1,1,1)):
        super().__init__(reportDate)
        self.fin_health_report = None #Will be an instance of FinancialHealthReport
        self.income_report = None #Will be an instance of IncomeReport
        self.spending_report = None #Will be an isntance of SpendingReport

    #Date will either be based off system time or the user will manually input i
    reportDate = datetime.now() # year/month/day (i.e. 2024/10/17)

    fin_health_report = FinancialHealthReport()
    income_report = IncomeReport()
    spending_report = SpendingReport()

    def getReportDate(self):
        return self.reportDate
    
    def printReportDate(self):
        print(self.reportDate.year,'/',self.reportDate.month,'/',self.reportDate.day)


    '''Implementing abstract methods'''
    def generateAllReports(self):
        #Generate individual reports and store them in attributes
        self.fin_health_report = self.getFinancialHealth().generate_report() #generate_report is based off the function in FinancialHealthReport, the only funciton class as of now.
        self.income_report = self.getIncomeReport().generate_report()
        self.spending_report = self.getSpendingReport().generate_report()
        
        
    def generateCombinedReport(self):
        self.generateAllReports()
        combined_report_data = {
            "Financial Health": self.fin_health_report,
            "Income": self.income_report,
            "Spending": self.spending_report
        }
        return combined_report_data



    def getFinancialHealth(self):
        #If a report doesn't exist, make an empty one so something is return and the program doesn't crash.
        if self.fin_health_report is None:
            self.fin_health_report = FinancialHealthReport()
        return self.fin_health_report
    
    def getIncomeReport(self):
        #If a report doesn't exist, make an empty one so something is return and the program doesn't crash.
        if self.income_report is None:
            self.income_report = IncomeReport()
        return self.income_report
    

    def getSpendingReport(self):
        #If a report doesn't exist, make an empty one so something is return and the program doesn't crash.
        if self.spending_report is None:
            self.spending_report = SpendingReport()
        return self.spending_report




print("ReportFactory.py")
factory = ReportFactory()
factory.printReportDate()
