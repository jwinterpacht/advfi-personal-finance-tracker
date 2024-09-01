'''
Stock class
One notable thing is that although this stores the overall portfolio value for all the stocks the user owns, it does not store how much each individual stock is worth
This is important in cases where we sell stock, as the total portfolio value will not update unless update_portfolio_value() or print_stocks() are called
Technically add_stock_to_portfolio() has an edge case where it will only update the added stock values but this is VERY minor and will not be noticeable unless a stock price is HIGHLY volatile

Most of these methods have been fairly rigorously tested and this stuff is honestly somewhat ready to go
Only one small thing I'd like 
TODO: if a user tries to add a stock and the symbol is not found by the yfinance api, the exception is handled but the api prints out a 404 error
        I'd like it to be so that the user does not see this and only sees the error message coming from our program, but it's a small thing
        I'll look into it more later (obvious lie)

'''

#importing stocks works!
import yfinance as yf #yahoo finance api 

class Stocks():

    my_stocks = {}
    portfolio_value = 0

    #uses the api stuff to get the most recent stock prices, not fast enough for day trading but fast enough for our purposes
    def update_portfolio_value(self):
        portfolio_value = 0 #reset the portfolio value 
        for key in self.my_stocks.keys: #loop through each key in our stocks dictionary
            #and grab the value of each stock, multiply it by how many we own, and add that to our portfolio value
            stock = yf.Ticker(key) #turn the dictionary key into a ticker value 
            portfolio_value += (stock.info.get('currentPrice') * self.my_stocks[key]) #grab the current value of each stock, multiply, and increment
    

    #testing stuff
    #assign stocks and upate the portfolio value
    '''
    my_stocks = {"amzn": 3, "rivn": 1, "nvda":5}
    for key in my_stocks: #loop through each key in our stocks dictionary
        #and grab the value of each stock, multiply it by how many we own, and add that to our portfolio value
        stock = yf.Ticker(key)
        portfolio_value += (stock.info.get('currentPrice') * my_stocks[key])
    '''

    #grabs the currently set portfolio value
    def get_portfolio_value(self):
        return self.portfolio_value
    
    def print_portfolio_value(self):
        print("Current Total Portfolio Value: ${total}\n".format(total = self.portfolio_value))
    
    #grab the dictionary address for my_stocks
    def get_my_stocks(self):
        return self.my_stocks

    
    #useful if user is trying to remove a stock, also updates the total portfolio value
    def print_stocks(self):
        self.portfolio_value = 0 #reset portfolio value
        for key in self.my_stocks:
            stock = yf.Ticker(key)
            stock_price = stock.info.get('currentPrice')
            self.portfolio_value += stock_price * self.my_stocks[key] 
            print("Stock: {symbol}\tCurrent Stock Value: ${price}\tStocks Owned: {amount}".format(symbol = key, price = stock_price, amount = self.my_stocks[key])) #print out stock symbol, price, and amount owned
        print("Total Value of Portfolio: ${total}\n".format(total = self.portfolio_value))
    


    #symbol->stock symbol (think "msft") amount->how many stocks the user has purchased
    #3 possible cases: 
    #1. incorrect symbol and we cannot find the stock
    #2. already own the stock and just need to add to current amount 
    #3. correct symbol and don't already own the stock
    def add_stock_to_portfolio(self, symbol, amount):

        if amount < 1: #edge case handling
            return "Please enter a number greater than 0"

        #turn the string into a stock object
        stock = yf.Ticker(symbol)

        #print(stock)

        #this try/except currently prints out a 404 client error, I plan on fixing this to make it look nicer but not my current focus
        try:
            self.portfolio_value += stock.info.get('currentPrice') * amount
        except:
            return "Stock not found, please ensure correct spelling of the stock symbol\n"
    

        #if we already own some amount of this stock
        if symbol in self.my_stocks:
            self.my_stocks[symbol] += amount
        
        #if stock we do not already own
        else:
            self.my_stocks[symbol] = amount

        if amount == 1:        #making the output text look nice
            txt = "Successfully added 1 stock of {stock_symbol}\n".format(stock_symbol = symbol)
        else:
            txt = "Successfully added {stock_amount} stocks of {stock_symbol}\n".format(stock_amount = amount, stock_symbol = symbol)
        return txt
    
    #if the user inputs -1 into the amount, all shares of the stock will be sold
    #since we do not update the portfolio value here, I recommend calling print_stocks after every time we use this because not only can the user now see their updated portfolio with the removed stocks
    #   but the function will also update the overall portfolio value in the background
    def remove_stock_from_portfolio(self, symbol, amount):
        if amount < -1: #if user enters a number less than -1
            return "Please enter a positive number or -1 to sell all shares of the given stock"
        
        if symbol in self.my_stocks: #if given symbol was found in my_stocks
            if amount > self.my_stocks[symbol]: #if user attemps to sell more stocks than they currently own
                return "You own {amt_owned} share(s) of {sym} and cannot sell more stock than you currently own\nYou can enter -1 to sell all owned shares of a given stock\n".format(amt_owned = self.my_stocks[symbol], sym = symbol)
            
            if amount == -1: #if user wants to use the -1 to sell all functionality
                amount = self.my_stocks[symbol] #just set amount to number of stocks we have
            self.my_stocks[symbol] -= amount #subtract currently held number of shares by the amount we are selling
            if self.my_stocks[symbol] == 0: #if we currently hold zero shares of a stock
                del self.my_stocks[symbol] #no reason to keep that stock in our dictionary, so we delete it
                return "All shares of {sym} sold successfully\n".format(sym = symbol) #various returns so we can print out where the function was called
            return "{amt} share(s) of {sym} sold successfully\n".format(amt = amount, sym = symbol)
        return "Symbol {sym} not found, please check your spelling or ensure you currently own this shares of this stock\n".format(sym = symbol)
        

 





