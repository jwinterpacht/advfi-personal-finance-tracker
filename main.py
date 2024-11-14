'''
Main functionality of AdvFi, will be the user interface
'''
import UserAccount
from datetime import datetime
import Category
import Entity
import EntityPortfolio


#draw the AdvFi logo for the user
def draw_logo():
    print(r"    _      __                     ____  _____ ")
    print(r"   / \    |  \   \     /         |        |   ")
    print(r"  /---\   |   |   \   /    ===   |--      |   ")
    print(r" /     \  |__/     \_/           |      __|__ ")
    print("\n")


#the main user interface menu for the user
def home_screen(entity_portfolio):
    print("\n\t\tWelcome to")
    draw_logo()
    show_net_worth()
    print("1: Income Management Menu")
    print("2: Spending and Expense Management Menu")
    print("3: Asset Management Menu")
    print("4: Liability and Debt Management Menu")
    print("5: Fiancial Reports Menu")
    print("6: Retrieve Transactions")
    print("7: Alert Center Menu")
    print("8: Program Settings Menu")
    print("9: Exit AdvFi")

    user_selection = input()
    
    match user_selection:
        case "1":
            income_management_menu()
        case "2":
            spending_managment_menu()
        case "3":
            asset_management_menu(entity_portfolio)
        case "4": 
            liability_management_menu(entity_portfolio)
        case "5":
            financial_reports_menu()
        case "6": 
            retrieve_transactions()
        case "7":
            alert_center_menu()
        case "8":
            program_settings_menu()
        case "9":
            print("Thank you for using AdvFi")
            exit()
            

def show_net_worth():
    #calculate networth and display it
    net_worth = 20,000
    print("\nCurrent Net Worth: $20,000\n")


def income_management_menu():
    print("Income Management Menu")
    print("1: Add income")
    print("2: View income list")
    print("3: Delete income")
    print("0: Return to main menu")
    user_selection = input()

    match user_selection:
        case "1":
            #add income
            #amount
            print("Amount: ")
            amount = input()
            #date
            print("Enter date in MM/DD/YYYY:")
            date = input()
            date_format = "%m/%d/%Y"
            date_obj = datetime.strptime(date, date_format).date()
            print(date_obj)
            #category (not rn)  


def spending_managment_menu():
    print("Spending and Expense Management Menu")
    print("1: Add expense")
    print("2: Import spending data from CSV")
    print("3: Create recurring expenses")
    print("4: Create new spending category")
    print("5: Set budgets for spending categories")
    print("6: Monitor budget adherence")
    print("7: Delete transaction")
    print("0: Return to main menu")



def asset_management_menu(entity_portfolio):
    print("Asset Management Menu")
    print("1: Add asset")
    print("2: Remove asset")
    print("3: Calculate real time asset prices")
    print("4: Add category for assets/liabilities")
    print("0: Return to main menu")


def liability_management_menu(entity_portfolio):
    print("Liability and Debt Managment Menu")
    print("1: Add Liability")
    print("2: Remove Liability")
    print("3: Track outstanding debt and payment debt") #will allow user to make a payment and reduce the debt recorded in AdvFi
    print("4: Add category for assets/liabilities")
    print("0: Return to main menu")

    user_selection = input()

    match user_selection:
        case "1":
            print("Adding a liability:")
            print("Enter the liability name, the value in dollars, and a description(optional).")
            print("Please separate the name, value, and description with commas (do not worry about commas for the value)")
            print("Press -1 to cancel") #needs functionality

            user_in = input()
            if user_in == "-1":  #return to the menu
                liability_management_menu()
                return      #I think this is right
            
            user_in = user_in.split(",")
            name = user_in[0]
            value = float(user_in[1])
            if len(user_in) == 3:
                desc = user_in[2]
            else:
                desc = ""

            if len(entity_portfolio.get_category_list()) == 1:
                category = entity_portfolio.get_category(0)
            else:
                #add logic here to print all the categories and let the user select one of them
                pass
            new_liability = Entity.Entity(category, "liability", value, 1, name, desc, False, "n/a")
            entity_portfolio.add_liability(new_liability)
            print("New liability added successfully")
            liability_management_menu()
            return

            




            

            



def financial_reports_menu():
    print("Financial Reports Menu")
    print("1: Generate income report")              # when the user generates a report, they will be prompted to save to database, save to pdf, or both
    print("2: Generate spending report")
    print("3: Generate financial health report")
    print("4: Retrieve previously generated report from the database")  # goes to a sub-menu where all previously saved reports show up, maybe only display this option if user previously saved report to database
    print("0: Return to main menu")



def retrieve_transactions():
    print("Transactions")
    print("Placeholder")
    print("0: Return to main menu")



def alert_center_menu():
    print("Alert Center Menu")
    print("1: Create alert")
    print("2: Delete alert")
    print("3: Edit alert")
    print("4: Retrieve current alerts")
    print("5: Dismiss alert")
    print("0: Return to main menu")



def program_settings_menu():
    print("Program Settings Menu")
    print("1: change password")
    print("2: delete user account")
    print("0: Return to main menu")










#will need to add functionality to create account/login
if __name__ == "__main__":
    entity_portfolio = EntityPortfolio.EntityPortfolio()
    liability_management_menu(entity_portfolio)
    
