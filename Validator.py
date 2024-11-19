import Operations
import Transaction
from datetime import datetime



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
    


def validate_income_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 3

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    return True

def validate_asset_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 4

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
    return True



def validate_num_owned(num_owned: str):
    if not _validate_integer(num_owned):
        return False
    owned = int(num_owned)
    if owned < 0:
        print("Error: cannot own negative entities")
        return False
    return True


def validate_yes_no(user_input: str):
    if user_input[0].lower == "y":
        return True
    elif user_input[0].lower == "n":
        return True
    return False