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
    def get_report(self, report_type: str, transaction_list: TransactionList, entity_portfolio=None):
        if report_type == "financial health":
            return FinancialHealthReport.FinancialHealthReport(date.today(), transaction_list, entity_portfolio)
        elif report_type == "income":
            return IncomeReport.IncomeReport(date.today(), transaction_list)
        elif report_type == "spending":
            return SpendingReport.SpendingReport(date.today(), transaction_list)
        else:
            print(f"Invalid report type: {report_type}")
            return None
