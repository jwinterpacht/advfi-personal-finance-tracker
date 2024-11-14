'''
this file defines the class Transaction
by Jaden Winterpacht
'''

from datetime import date
import TransactionCategory

class Transaction:

    transaction_ID = -1
    

    def __init__(self, amount: float, transaction_date: date, recurring_rate: int = 0, description: str = ""):
        self.amount = amount
        self.transaction_date = transaction_date
        self.recurring_rate = recurring_rate
        self.description = description



    # instance variables transaction_id, amount, transaction_date, category, recurring_rate, and description
    def __init__(self, transaction_id: str, amount: float, transaction_date: date, category: TransactionCategory,
                 recurring_rate: int, description: str):
        self._transaction_id = transaction_id
        self._amount = amount
        self._transaction_date = transaction_date
        self._category = category
        self._recurring_rate = recurring_rate
        self._description = description

    # return the transaction ID
    def get_transaction_id(self) -> str:
        return self._transaction_id

    # return the transaction amount
    def get_amount(self) -> float:
        return self._amount

    # set the transaction amount
    def set_amount(self, amount: float) -> None:
        self._amount = amount

    # get the date of the transaction
    def get_transaction_date(self) -> date:
        return self._transaction_date

    # set the date of the transaction
    def set_transaction_date(self, transaction_date: date) -> None:
        self._transaction_date = transaction_date

    # get the category of the transaction
    def get_category(self) -> TransactionCategory:
        return self._category

    # set the category of the transaction
    def set_category(self, category: TransactionCategory) -> None:
        self._category = category

    # get the recurring rate of the transaction
    def get_recurring_rate(self) -> int:
        return self._recurring_rate

    # set the recurring rate of the transaction
    def set_recurring_rate(self, recurring_rate: int) -> None:
        self._recurring_rate = recurring_rate

    # get the description of the transaction
    def get_description(self) -> str:
        return self._description

    # set the description of the transaction
    def set_description(self, description: str) -> None:
        self._description = description
