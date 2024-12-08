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
import TransactionList
import EntityPortfolio


class ReportFactory():
    def get_report(self, report_type: str, transaction_list: TransactionList):
        if report_type == "financial":
            return FinancialHealthReport.FinancialHealthReport()
        elif report_type == "income":
            return IncomeReport.IncomeReport(transaction_list)
        elif report_type == "spending":
            return SpendingReport.SpendingReport(transaction_list)
        else:
            print(f"Invalid report type: {report_type}")
            return None
