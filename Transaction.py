'''
this file defines the class Transaction
by Jaden Winterpacht
'''

from datetime import date
import Category

class Transaction:

    #static bc defined outside of __init__
    transaction_ID = -1
    

    def __init__(self, amount: float, transaction_date: date, description: str = ""):
        self._amount = amount
        self._transaction_date = transaction_date
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
    def get_category(self) -> Category:
        return self._category

    # set the category of the transaction
    def set_category(self, category: Category) -> None:
        self._category = category

    # get the description of the transaction
    def get_description(self) -> str:
        return self._description

    # set the description of the transaction
    def set_description(self, description: str) -> None:
        self._description = description

    