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
        self._liquidity_ratio = liquidity_ratio
        self._investment_return = investment_return
        self._report_date = report_date

    @classmethod
    def generate_report(cls, net_worth: float, total_assets: EntityPortfolio, total_liabilities: EntityPortfolio,
                        income: float, expenses: float, savings_rate: float, debt_to_income_ratio: float,
                        liquidity_ratio: float, investment_return: float, report_date: date):
        '''
        class method that creates a FinancialHealthReport object

        :param net_worth: the net worth of the user (assets - liabilities)
        :param total_assets: the total amount of assets the user has
        :param total_liabilities: the total amount of liabilities the user has
        :param income: total gross income
        :param expenses: total expenses
        :param savings_rate: percent of income that is saved
        :param debt_to_income_ratio: the percentage of gross income dedicated to paying debts
        :param liquidity_ratio: determines user's ability to pay short-term debts
        :param investment_return: how much the user has gained or lost on investments, represented by a percentage
        :param report_date: the date when the report was generated
        :return: a FinancialHealthReport object
        '''
        return cls(net_worth, total_assets, total_liabilities,
                        income, expenses, savings_rate, debt_to_income_ratio, liquidity_ratio, investment_return,
                   report_date)

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
