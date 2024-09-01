#what a wonderful long conga line we have here
from Stocks import Stocks

class NetWorth():
    liquid_net_worth = 0
    stock_portfolio_value = 0
    total_net_worth = 0
    stock_portfolio = Stocks()

    #testing stuff, give us a starting point
    liquid_net_worth = 7800

    stock_portfolio.add_stock_to_portfolio("nvda", 6)
    stock_portfolio.add_stock_to_portfolio("msft", 9)

    stock_portfolio_value = stock_portfolio.get_portfolio_value()

    total_net_worth = liquid_net_worth + stock_portfolio_value

    
    def get_net_worth(self):
        return self.total_net_worth
    
    def print_net_worth(self):
        return self.total_net_worth
    
    def get_liquid_net_worth(self):
        pass




        
    
