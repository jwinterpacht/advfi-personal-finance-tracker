from datetime import date

class Transaction:
    
    _transaction_ID = -1

    def __init__(self, amount: float, transaction_date: date, description: str = ""):
        self._amount = amount
        self._transaction_date = transaction_date
        self._description = description
    
    # return the transaction ID
    def get_transaction_id(self) -> str:
        return self._transaction_id
    
    def set_transaction_id(self, new_ID: str) -> bool:
        if self._transaction_ID == -1:
            self._transaction_ID = new_ID
            return True
        else:
            print("Error: can only update a transaction ID once")
            return False


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
    
    def get_description(self) -> str:
        return self._description
    
    def set_description(self, description: str) -> None:
        self._description = description

    def print_transaction(self) -> None:
        print("ID: {}\tAmount: {}\tDate: {}\tDescription: {}".format(self._transaction_ID, self._amount, self._transaction_date.date(), self._description))
