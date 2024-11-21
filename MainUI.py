import Validator
import Operations

import os

input_text = ""
#input_text = "Press enter to return to the main menu"

class MainUI:
    # class variables
    INCOME_MGMT_MENU_LOW = 0
    INCOME_MGMT_MENU_HIGH = 3
    SPENDING_MGMT_MENU_LOW = 0
    SPENDING_MGMT_MENU_HIGH = 7
    ASSET_MGMT_MENU_LOW = 0
    ASSET_MGMT_MENU_HIGH = 4

    def clear_screen():
        #pass
        # for Windows
        if os.name == "nt":
            os.system("cls")
        # for macOS and Linux
        else:
            os.system("clear")

    def get_transaction_amount():
        print("Enter transaction amount in dollars: ")
        return input("$")
    
    def get_date():
        print("Enter date in MM/DD/YY format:")
        return input()

    def get_desc():
        print("Enter a description: ")
        return input()
    
    def get_num_owned():
        print("Enter the number of entites you own\nWill default to 1 if left blank")
        return input()
    
    def get_entity_value():
        print("Enter the entity value")
        return input("$")
    
    def get_entity_name():
        print("Enter the entity name")
        return input()
    
    def get_stock_symbol():
        print("Enter the stock symbol that you want to link with the asset")
        return input()

    @staticmethod
    def draw_logo():
        print(r"    _      __                     ____  _____ ")
        print(r"   / \    |  \   \     /         |        |   ")
        print(r"  /---\   |   |   \   /    ===   |--      |   ")
        print(r" /     \  |__/     \_/           |      __|__ ")
        print("\n")
        return


    @staticmethod
    def show_net_worth():
        #calculate networth and display it
        net_worth = 20,000
        print("\nCurrent Net Worth: $20,000\n")
        return
        

    @staticmethod
    def home_screen():
        MainUI.clear_screen()
        print("\n\tWelcome to")
        MainUI.draw_logo()
        MainUI.show_net_worth()
        print("1: Income Management Menu")
        print("2: Spending and Expense Management Menu")
        print("3: Asset Management Menu")
        print("4: Liability and Debt Management Menu")
        print("5: Fiancial Reports Menu")
        print("6: Retrieve Transactions")
        print("7: Alert Center Menu")
        print("8: Program Settings Menu")
        print("9: Exit AdvFi")
        return input()

    @staticmethod
    def income_management_menu():
        MainUI.clear_screen()
        print("Income Management Menu\n----------------------------------")
        print("1: Add income")
        print("2: View income list")
        print("3: Delete income")
        print("0: Return to main menu")
        return input()
    
    @staticmethod
    def income_management_menu_add_income():
        MainUI.clear_screen()
        print("Adding New Income \n")
        return

    @staticmethod
    def income_management_menu_view_income_list():
        MainUI.clear_screen()

    @staticmethod
    def income_management_menu_remove_income():
        print("Enter the ID of the income you would like to remove\nEnter -1 to cancel the operation")
        return input()
    
    @staticmethod
    def spending_management_menu():
        MainUI.clear_screen()
        print("\nSpending and Expense Management Menu")
        print("1: Add expense")
        print("2: Import spending data from CSV")
        print("3: Create recurring expenses")
        print("4: Create new spending category")
        print("5: Set budgets for spending categories")
        print("6: Monitor budget adherence")
        print("7: Delete transaction")
        print("0: Return to main menu")
        
        # return the user's input and give it to the Controller class
        return input()
    
    @staticmethod
    def asset_management_menu():
        MainUI.clear_screen()
        print("\nAsset Management Menu")
        print("1: Add asset")
        print("2: View asset list")
        print("3: Remove asset")
        print("4: Calculate real time asset prices")
        print("5: Add category for assets/liabilities")
        print("0: Return to main menu")
        return input()
    
    @staticmethod
    def asset_management_menu_add_asset_is_stock():
        MainUI.clear_screen()
        print("Adding New Asset")
        print("Would you like to link this asset with a stock? (y/n)")
        return input()
    
    def asset_management_menu_delete_asset():
        Operations.asset_management_menu_view_asset_list_operations()
        print("Enter the ID of the income you would like to remove\nEnter -1 to cancel the operation")
        return input()
    


    @staticmethod
    def liability_management_menu():
        MainUI.clear_screen()
        print("\nLiability and Debt Managment Menu")
        print("1: Add Liability")
        print("2: Remove Liability")
        print("3: Track outstanding debt and payment debt") #will allow user to make a payment and reduce the debt recorded in AdvFi
        print("4: Add category for assets/liabilities")
        print("0: Return to main menu")

    @staticmethod
    def financial_reports_menu():
        MainUI.clear_screen()
        print("\nFinancial Reports Menu")
        print("1: Generate income report")              # when the user generates a report, they will be prompted to save to database, save to pdf, or both
        print("2: Generate spending report")
        print("3: Generate financial health report")
        print("4: Retrieve previously generated report from the database")  # goes to a sub-menu where all previously saved reports show up, maybe only display this option if user previously saved report to database
        print("0: Return to main menu")

    @staticmethod
    def retrieve_transactions():
        MainUI.clear_screen()
        print("\nTransactions")


    @staticmethod
    def alert_center_menu():
        MainUI.clear_screen()
        print("\nAlert Center Menu")
        print("1: Create alert")
        print("2: Delete alert")
        print("3: Edit alert")
        print("4: Retrieve current alerts")
        print("5: Dismiss alert")
        print("0: Return to main menu")


    @staticmethod
    def program_settings_menu():
        MainUI.clear_screen()
        print("\nProgram Settings Menu")
        print("1: change password")
        print("2: delete user account")
        print("0: Return to main menu")




    #other misc classes

    #this is used to make the program wait for the user to be ready for another action
    #typically used before going back to the home screen
    def wait_for_user_input():
        return input(input_text) #don't actually need to return anything

    def add_transaction_success():
        print("Transaction added successfully!")
        MainUI.wait_for_user_input()

    def remove_transaction_success():
        print("Transaction removed successfully!")
        MainUI.wait_for_user_input()

    
    def remove_transaction_failure(transaction_id):
        print(f"Transaction ID {transaction_id} was not found in the given list, nothing was removed")
        MainUI.wait_for_user_input()

    
    def action_cancelled():
        print("Action was cancelled")
        MainUI.wait_for_user_input()


    def empty_name():
        print("Error: cannot enter an empty name")

    def add_entity_success(entity_type): #should only ever be asset or liability
        print(f"{entity_type} added successfully") #asset/liability added successfully
        MainUI.wait_for_user_input()

    def stock_not_found(stock):
        print(f"{stock} was not found, please ensure correct spelling and that the stock is listed in yahoo finance")
        

    def remove_entity_success(entity_type):
        print(f"{entity_type} removed successfully")
        MainUI.wait_for_user_input()








