import TransactionList
import EntityPortfolio

class userAccount:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._entity_portfolio = []
        self._transaction_list = []
        self._net_worth = 0.0
        