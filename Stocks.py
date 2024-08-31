#importing stocks works!
import yfinance as yf

class Stocks():

    my_stocks = {}
    portfolio_value = 0

    #uses the api stuff to get the most recent stock prices, not fast enough for day trading but fast enough for our purposes
    def update_portfolio_value(self):
        portfolio_value = 0 #reset the portfolio value (almost forgot to do this whoops)
        for key in self.my_stocks.keys: #loop through each key in our stocks dictionary
            #and grab the value of each stock, multiply it by how many we own, and add that to our portfolio value
            stock = yf.Ticker(key) #turn the dictionary key into a ticker value (something like that idk I'm not a stock person)
            portfolio_value += (stock.info.get('currentPrice') * self.my_stocks[key]) #grab the current value of each stock, multiply, and increment
    
    #testing stuff
    my_stocks = {"amzn": 3, "rivn": 1, "nvda":5}
    for key in my_stocks: #loop through each key in our stocks dictionary
        #and grab the value of each stock, multiply it by how many we own, and add that to our portfolio value
        stock = yf.Ticker(key)
        portfolio_value += (stock.info.get('currentPrice') * my_stocks[key])


    #
    def get_portfolio_value(self):
        return self.portfolio_value


    #symbol->stock symbol (think "msft") amount->how many stocks the user has purchased
    #3 possible cases: 
    #1. incorrect symbol and we cannot find the stock
    #2. already own the stock and just need to add to current amount 
    #3. correct symbol and don't already own the stock
    def add_stock_to_portfolio(self, symbol, amount):

        #turn the string into a stock object
        stock = yf.Ticker(symbol)

        print(stock)

        #this try/except currently prints out a 404 client error, I plan on fixing this to make it look nicer but not my current focus
        try:
            self.portfolio_value += stock.info.get('currentPrice') * amount
        except:
            return "Stock not found, please ensure correct spelling of the stock symbol"
    

        #if we already own some amount of this stock
        if symbol in self.my_stocks:
            self.my_stocks[symbol] += amount
        
        #if stock we do not already own
        else:
            self.my_stocks[symbol] = amount
        

        return "Stock added successfully!"
    
    #if the user inputs -1 into the amount, all shares of the stock will be sold
    #TODO: if user inputs more than they have or a negative number that is not -1, throw an error
    def remove_stock_from_portfolio(self, symbol, amount):
        if symbol in self.my_stocks: #if given symbol was found in my_stocks
            if amount == -1: #if user wants to use the -1 to sell all functionality
                amount = self.my_stocks[symbol] #just set amount to number of stocks we have
            self.my_stocks[symbol] -= amount #subtract currently held number of shares by the amount we are selling
            if self.my_stocks[symbol] == 0: #if we currently hold zero shares of a stock
                del self.my_stocks[symbol] #no reason to keep that stock in our dictionary, so we delete it
                return "All shares sold successfully"
            return amount + " shares sold successfully"
        return "Symbol not found, please check your spelling or ensure you currently own this shares of this stock"
        

 





