'''
this file defines a class FinancialHealthReport, which is used to assess the financial health of the user
by Jaden Winterpacht
'''

import EntityPortfolio
from datetime import date

class FinancialHealthReport:
    def __init__(self, net_worth: float, total_assets: EntityPortfolio, total_liabilities: EntityPortfolio,
                 income: float, expenses: float, savings_rate: float, debt_to_income_ratio: float,
                 liquidity_ratio: float, investment_return: float, report_date: date):
        self._net_worth = net_worth
        self._total_assets = total_assets
        self._total_liabilities = total_liabilities
        self._income = income
        self._expenses = expenses
        self._savings_rate = savings_rate
        self._debt_to_income_ratio = debt_to_income_ratio
        self._investment_return = investment_return

    def calculate_savings_rate(self, income: float, expenses: float) -> float:
        '''
        calculates the percent of income that the user is saving

        :return: the savings rate
        '''
        self._savings_rate = 1 - (expenses / income)
        return self._savings_rate

    def calculate_debt_to_income_ratio(self):
        '''
        calculates the percentage of gross income dedicated to paying debts

        :return: the debt-to-income ratio
        '''
        total_debt = self._total_liabilities.get_liabilities_value()
        if self._income > 0:
            self._debt_to_income_ratio = total_debt / self._income
        else:
            self._debt_to_income_ratio = 0  # Handle case where income is zero to avoid division by zero
        return self._debt_to_income_ratio
