import Operations
import Transaction
from datetime import datetime
import MainUI
import Entity
import EntityPortfolio


#-----------PRIVATE METHODS-------------------
# use to check if a given string can be converted to integer safely
def _validate_integer(entry: str) -> bool:
    try:
        int(entry)
        return True
    except:
        print("Please be sure to enter an integer")
        return False

#used to check if a given string can be converted to float safely
def _validate_float(entry: str) -> bool:
    try:
        float(entry)
        return True
    except:
        print("Please be sure to enter a number")
        return False

#another private method to check if the input integer is within a valid range
def _validate_selection_range(selection: int, low_end: int, high_end: int) -> bool:
    if selection > high_end or selection < low_end: 
        print("Please enter an integer between {} and {}".format(low_end, high_end))
        return False
    return True

def validate_home_screen_entry(entry: str) -> bool:
    #technically for speed this should be implemented below the validate integer
    #however this is more readable
    low_end = 1
    high_end = 9

    #if validate integer returns false
    if not _validate_integer(entry):
        return False #return false
    
    selection = int(entry)  #we can now safely cast entry to int
    if not _validate_selection_range(selection, low_end, high_end): #if selection range validation is false
        return False   #return false
    
    return True
    


def validate_menu_entry(entry: str, low_end: int, high_end: int) -> bool:
    # user's entry must be an integer
    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    return True


def validate_value(amount) -> bool:
    if not _validate_float(amount):
        return False
    amount = float(amount)
    if amount < 0:
        print("Error: amount cannot be negative")
        return False
    return True


def validate_transaction_date(date) -> bool:
    '''
    method to validate a transaction date
    '''
    try:
        datetime.strptime(date, '%m/%d/%y')

    except:
        print("Error: Please format date correctly.")
        return False
    
    return True

def are_transaction_details_valid(transaction_details: list, type: str) -> bool:
    if len(transaction_details) == 3:
        Operations.create_and_add_transaction(transaction_details, type)
        pass

def validate_transaction_id(transaction_id: str):
    if not _validate_integer(transaction_id):
        return False
    transaction_id = int(transaction_id)
    if transaction_id < -1:
        print("Error: smallest allowed value is -1")
        return False
    #Make sure that a transaction id that exists was entered
    if transaction_id > Operations.retrieve_transaction_count():
        MainUI.MainUI.remove_transaction_failure(transaction_id)
        return False
    return True



def validate_num_owned(num_owned: str):
    if num_owned == "": #allow for the case where the user enters nothing
        return True
    
    if not _validate_integer(num_owned):
        return False
    owned = int(num_owned)
    if owned < 0:
        print("Error: cannot own negative entities")
        return False
    return True


def validate_yes_no(user_input: str):
    if user_input == "":
        return False
    if user_input[0] == "y":
        return True
    elif user_input[0] == "n":
        return True
    return False

#used to ensure that the user did not leave the space blank
def validate_name(user_input: str):
    if user_input == "":
        MainUI.MainUI.empty_name()
        return False
    return True

def validate_stock_symbol(stock_symbol: str):
    if stock_symbol == "":
        return False
    stock_price = Entity.get_stock_value(stock_symbol)
    if stock_price == None:  #this means advfi couldn't find the corresponding stock
        MainUI.MainUI.stock_not_found()
        return False
    #if we make it here, then the user input stock symbol is valid
    return True

def validate_entity_id(type: str, entity_id: str):
    if not _validate_integer(entity_id):
        return False
    entity_id = int(entity_id)
    if entity_id < -1:
        print("Error: smallest allowed value is -1")
        return False
    if entity_id == -1: #action cancelled
        return True
    #Make sure that a transaction id that exists was entered
    if type == "asset":
        return Operations.entity_portfolio.find_asset_id(entity_id)