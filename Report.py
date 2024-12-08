'''
Report class
By Jonah Raef
10-24-2024

Report is an abstract class that allows ReportFactory to create a report of any type (FinancialHealth, Income, Spending)
'''

from datetime import date
from datetime import datetime
from abc import ABC, abstractmethod #for abstract classes

#ABC denotes the class as 'abstract'
class Report(ABC):
    # = datetime.now() # year/month/day (i.e. 2024/10/17)

    def __init__(self, report_date):
        self.reportDate = report_date

    @abstractmethod
    def generate_report(self) -> bool:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass
