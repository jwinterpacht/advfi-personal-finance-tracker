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

class ReportFactory():
    def get_report(report_type: str):
        if report_type == "financial":
            return FinancialHealthReport()
        elif report_type == "income":
            return IncomeReport()
        elif report_type == "spending":
            return SpendingReport()
        else:
            print(f"Invalid report type: {report_type}")
            return None
