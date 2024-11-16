import MainUI
import Transaction
import TransactionList
import UserAccount
import EntityPortfolio
from datetime import datetime

transaction_list = TransactionList.TransactionList()
entity_portfolio = EntityPortfolio.EntityPortfolio()
user_account = UserAccount.UserAccount("rishi", "326", entity_portfolio, transaction_list)

def home_screen_operations(entry):
    selection = int(entry)  # can safely cast this because we already validated

    match selection:
        case 1:
            MainUI.MainUI.income_management_menu()
        
        case 2:
            MainUI.MainUI.spending_managment_menu()
        
        case 3:
            MainUI.MainUI.asset_management_menu()
        
        case 4:
            MainUI.MainUI.liability_management_menu()
        
        case 5:
            MainUI.MainUI.financial_reports_menu()
        
        case 6:
            MainUI.MainUI.retrieve_transactions()
        
        case 7:
            MainUI.MainUI.alert_center_menu()
        
        case 8:
            MainUI.MainUI.program_settings_menu()
        case 9:
            exit(0)


'''Income Operations'''
def create_transaction(input_list: list) -> Transaction:
    '''
    adds a transaction (income)
    '''
    transaction_amt = float(input_list[0])
    transaction_date = datetime.strptime(input_list[1], '%m/%d/%y')
    transaction_desc = input_list[2]
    new_transaction = Transaction.Transaction(transaction_amt, transaction_date, transaction_desc)

    return new_transaction

def add_income(transaction):
    TransactionList.TransactionList.add_income_transaction(transaction)


'''
def income_management_operations(entry, transaction):
    selection = int(entry)

    match selection:
        case 1:
            add_income(input_list)
'''




'''[some other] Operations'''