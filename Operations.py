import MainUI
import Transaction
from datetime import datetime as dt
import TransactionList
import Controller
import Entity
import EntityPortfolio

transaction_list = TransactionList.TransactionList()
entity_portfolio = EntityPortfolio.EntityPortfolio()


def home_screen_operations(selection):

    selection = int(selection) #can safely cast here because this code cannot run otherwise

    match selection:

        case 1:
            Controller.Controller.income_management_menu()

        case 2:
            MainUI.MainUI.spending_management_menu()
        
        case 3: 
            Controller.Controller.asset_management_menu()
        
        case 4: 
            MainUI.MainUI.liability_management_menu()
        
        case 5:
            MainUI.MainUI.financial_reports_menu()
        
        case 6:
            Controller.Controller.retrieve_transactions()
        
        case 7: 
            MainUI.MainUI.alert_center_menu()
        
        case 8:
            MainUI.MainUI.program_settings_menu()
        
        case 9:
            print("Thank you for using AdvFi!")
            exit(0)


def income_management_menu_operations(selection):
    match selection:
        case 1:
            Controller.Controller.income_management_menu_add_income()
        case 2:
            Controller.Controller.income_management_menu_view_income_list()
        case 3:
            Controller.Controller.income_management_menu_remove_income()
        case 0:
            Controller.Controller.home_screen()


def create_and_add_transaction(amount, date, desc, type: str):
    amount = float(amount)
    date = dt.strptime(date, '%m/%d/%y')

    transaction = Transaction.Transaction(amount, date, desc)

    if type == "income":
        transaction_list.add_income_transaction(transaction)
    
    elif type == "expense":
        transaction_list.add_expense_transaction(transaction)
    
    else:
        print("error")
    
def remove_transaction(transaction_id, type: str):
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
        MainUI.MainUI.remove_transaction_failure()

def retrieve_transaction_count():
    return transaction_list.get_transaction_count()


def asset_management_menu_operations(selection):
    match selection:
        case 1:
            Controller.Controller.asset_management_menu_add_asset()
        case 2:
            Controller.Controller.asset_management_menu_view_asset_list()
        case 3:
            Controller.Controller.asset_management_menu_delete_asset()

        case 0:
            Controller.Controller.home_screen()

def asset_management_menu_view_asset_list_operations():
    MainUI.MainUI.clear_screen()
    entity_portfolio.print_assets()



'''
type: string used to determine if entity is asset or liability

'''
def add_entity_to_portfolio(type, name, desc, value, num_owned, auto_update, stock_symbol):
    #first we need to create the entity
    new_entity = Entity.Entity(value, num_owned, name, desc, auto_update, stock_symbol)

    #now we need to add it to the respective list
    if type == "asset":
        EntityPortfolio.EntityPortfolio.add_asset(entity_portfolio, new_entity)
    elif type == "liability":
        EntityPortfolio.EntityPortfolio.add_liability(entity_portfolio, new_entity)
    
    MainUI.MainUI.add_entity_success(type)

    Controller.Controller.home_screen()


def remove_entity_from_portfolio(type, entity_id):
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
    




def print_transactions():
    transaction_list.print_transactions()


def print_income_list():
    transaction_list.print_incomes()

def print_expense_list():
    transaction_list.print_expenses()

