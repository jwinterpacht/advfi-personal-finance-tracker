import MainUI
import Transaction
from datetime import datetime as dt
import TransactionList
import Controller
import Entity
import EntityPortfolio





def create_and_add_transaction(transaction_list, amount, date, desc, type: str):
    amount = float(amount)
    date = dt.strptime(date, '%m/%d/%y')

    transaction = Transaction.Transaction(amount, date, desc)

    if type == "income":
        transaction_list.add_income_transaction(transaction)
    
    elif type == "expense":
        transaction_list.add_expense_transaction(transaction)
    
    else:
        print("error")
    
def remove_transaction(transaction_list, transaction_id, type: str):
    transaction_id = int(transaction_id)
    #allow for the user to cancel the action
    if transaction_id == -1:
        MainUI.MainUI.action_cancelled()
        return

    found_id = False
    if type == "income":
        found_id = transaction_list.remove_income_transaction(transaction_id)
    elif type == "expense":
        found_id = transaction_list.remove_expense_transaction(transaction_id)
    
    if found_id:
        MainUI.MainUI.remove_transaction_success()
    else:
        MainUI.MainUI.remove_transaction_failure(transaction_id)

def retrieve_transaction_count(transaction_list):
    return transaction_list.get_transaction_count()


def asset_management_menu_view_asset_list_operations(entity_portfolio):
    MainUI.MainUI.clear_screen()
    entity_portfolio.print_assets()

def liability_management_menu_view_liability_list_operations(entity_portfolio):
    MainUI.MainUI.clear_screen()
    entity_portfolio.print_liabilities()


'''
type: string used to determine if entity is asset or liability

'''
def add_entity_to_portfolio(entity_portfolio, type, name, desc, value, num_owned, auto_update, stock_symbol):
    #first we need to create the entity
    new_entity = Entity.Entity(value, num_owned, name, desc, auto_update, stock_symbol)

    #now we need to add it to the respective list
    if type == "asset":
        EntityPortfolio.EntityPortfolio.add_asset(entity_portfolio, new_entity)
    elif type == "liability":
        EntityPortfolio.EntityPortfolio.add_liability(entity_portfolio, new_entity)
    
    MainUI.MainUI.add_entity_success(type)

    Controller.Controller.home_screen()


def remove_entity_from_portfolio(entity_portfolio, type, entity_id):
    #since we have already checked to make sure that the entity id is in the respective list,
    #we do not need to worry about that
    entity_id = int(entity_id)

    if entity_id == -1:
        MainUI.MainUI.action_cancelled()
        return

    if type == "asset":
        entity_portfolio.remove_asset(entity_id)

    elif type == "liability":
        entity_portfolio.remove_liability(entity_id)
    
    MainUI.MainUI.remove_entity_success(type)
    



def print_transactions(transaction_list):
    transaction_list.print_transactions()


def print_income_list(transaction_list):
    transaction_list.print_incomes()

def print_expense_list(transaction_list):
    transaction_list.print_expenses()

