"""
Idea for this class:
When you are in MainUI getting user input, you will always be able to just call the corresponding validator by doing
Validator.validate_class_name_entry(entry)
and it will return true if input is valid and false if not
High Cohesion
Low Coupling


"""

import Operations
from datetime import datetime
import Transaction

'''MENU VALIDATION'''
#used to check if a string is an integer
#internal private method to help prevent code reuse
def _validate_integer(entry: str) -> bool:
    try:
        int(entry)
        return True
    except:
        print("Please be sure to enter an integer")
        return False

# validates user input that is supposed to be floating point number
def _validate_float(entry: str) -> bool:
    try:
        float(entry)
        return True
    except:
        print("Please be sure to enter a number")
        return False

#another private method to check if the input integer is a valid selection
def _validate_selection_range(selection: int, low_end: int, high_end: int) -> bool:
    if selection > high_end or selection < low_end:
        print("Please enter an integer between {} and {}".format(low_end, high_end))
        return False
    return True



def validate_home_screen_entry(entry: str) -> bool:
    low_end = 1
    high_end = 9
    
    if(not _validate_integer(entry)):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    
    Operations.home_screen_operations(selection)
    


def validate_income_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 3

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    
    return True
   # Operations.income_management_operations(entry, transaction)

    
def are_transaction_details_valid(input_list: list, is_income: bool) -> bool:
    if len(input_list) == 3:
        transaction = Operations.create_transaction(input_list)
        if(is_income):
            print(transaction.get_description())
            Operations.add_income(transaction)
        return True
    else:
        return False

def validate_transaction_amt(amount) -> bool:
    # make sure amount is a number
    if(not _validate_float(amount)):
        return False
    amount = float(amount)
    # amount cannot be negative
    if amount < 0:
        print("Error: Amount cannot be negative")
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

def validate_spending_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 7

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False

def validate_asset_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 4

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    
def validate_liability_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 4

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    
def validate_financial_reports_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 4

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    
def validate_retrieve_transactions(entry: str) -> bool:
    low_end = 0
    high_end = 0

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False

'''  
def validate_alert_center_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 5

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
'''
    
def validate_program_settings_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 2

    if not _validate_integer(entry):
        return False
    
    selection = int(entry)
    if not _validate_selection_range(selection, low_end, high_end):
        return False
    

'''Operation VALIDATION'''