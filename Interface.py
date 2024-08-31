#importing the classes from the other files
#import User #imported NetWorth here, probably don't need to import it again
from Stocks import Stocks






def draw_UI():
    
    pass



s1 = Stocks()
print(s1.get_portfolio_value())


print(s1.add_stock_to_portfolio("rvin",2))


print(s1.get_portfolio_value())



'''
#main driver code
print("Welcome to AdvFi, your personal finance tracker!")

#get user authentication
user_ID = input("Please enter your User ID: ") #this is just placeholder stuff for now but should eventually go to the database and lookup if there is a user matching the id and password
password = input("Please enter your Password: ")

if False: #will use this if no matching database entry
    print("Incorrect User ID or password") #remember not to tell the user which was wrong between the ID and password (causes security problems)
    #repeat this process until matching id and password
    user_ID = input("Please enter your User ID: ") #this is just placeholder stuff for now but should eventually go to the database and lookup if there is a user matching the id and password
    password = input("Please enter your Password: ")





'''




