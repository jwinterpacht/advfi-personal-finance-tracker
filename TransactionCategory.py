'''
this file defines the class TransactionCategory
by Jaden Winterpacht
'''

class TransactionCategory:
    # instance variables category_name and description
    def __init__(self, category_name: str, description: str):
        self._category_name = category_name
        self._description = description

    # returns the name of the category
    def get_name(self) -> str:
        return self._category_name

    # returns the description of the category
    def get_description(self) -> str:
        return self._description

    # sets the name of the category
    def set_name(self, name: str) -> None:
        self._category_name = name

    # sets the description of the category
    def set_description(self, description: str) -> None:
        self._description = description
