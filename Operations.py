import MainUI
import Transaction
from datetime import datetime as dt
import TransactionList


transaction_list = TransactionList.TransactionList()


def home_screen_operations(selection):

    match selection:

        case 1:
            MainUI.MainUI.income_management_menu()

        case 2:
            MainUI.MainUI.spending_management_menu()
        
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
            print("Thank you for using AdvFi!")
            exit(0)


def income_management_menu_operations(selection):
    
    match selection:

        case 1:
            MainUI.MainUI.income_management_menu_add_income()
        

        case 0:
            MainUI.MainUI.home_screen()


def create_and_add_transaction(transaction_details: list, type: str):
    amount = float(transaction_details[0])
    date = dt.strptime(transaction_details[1], '%m/%d/%y')
    desc = transaction_details[2]
    transaction = Transaction.Transaction(amount, date, desc)

    if type == "income":
        transaction_list.add_income_transaction(transaction)
    
    elif type == "expense":
        transaction_list.add_expense_transaction(transaction)
    
    else:
        print("error")
        MainUI.MainUI.income_management_menu()
    
    print("Transaction Added Successfully!\n")
    MainUI.MainUI.home_screen()





def print_transactions():
    transaction_list.print_transactions()

