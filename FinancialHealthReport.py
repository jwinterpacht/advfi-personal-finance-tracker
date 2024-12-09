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
<<<<<<< Updated upstream
            self._debt_to_income_ratio = 0  # Handle case where income is zero to avoid division by zero
        return self._debt_to_income_ratio
=======
            investment_return = f"Investment return: N/A\n\n"
        advfi_score = f"AdvFi Score: {self._advfi_score}\n"
        financial_health_report = header + net_worth + items + savings_rate + investment_return + advfi_score
        MainUI.MainUI.utility_print(financial_health_report)

    def to_string(self) -> str:
        header = f"Financial Health Report\n{self._report_date}\n---------------------------\n"
        net_worth = f"Net worth: ${self._net_worth}\n\n"
        items = f"Total asset value: ${self._total_assets}\nTotal debt value: ${self._total_liabilities}\nTotal income: ${self._total_income}\nTotal spending: ${self._total_expenses}\n\n"
        savings_rate = f"Savings rate: {self._savings_rate:.2f}%\n"
        inv_return = self._investment_return
        if inv_return != -1:
            investment_return = f"Investment return: {self._investment_return}%\n\n"
        else:
            investment_return = f"Investment return: N/A\n\n"
        advfi_score = f"AdvFi Score: {self._advfi_score}\n"
        financial_health_report = header + net_worth + items + savings_rate + investment_return + advfi_score
        return financial_health_report
>>>>>>> Stashed changes
