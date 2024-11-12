'''
Main functionality of AdvFi, will be the user interface
'''
#import UserAccount


#draw the AdvFi logo for the user
def draw_logo():
    print(r"    _      __                     ____  _____ ")
    print(r"   / \    |  \   \     /         |        |   ")
    print(r"  /---\   |   |   \   /    ===   |--      |   ")
    print(r" /     \  |__/     \_/           |      __|__ ")
    print("\n")


#the main user interface menu for the user
def home_screen():
    print("\n\t\tWelcome to")
    draw_logo()
    show_alerts()
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
            asset_management_menu()
        case "4": 
            liability_management_menu()
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
            


def show_alerts():
    #go to the budget class and get any alerts that should be displayed to the user
    #for now, display no alerts
    alert_str = "No current alerts"
    print(alert_str)


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



def asset_management_menu():
    print("Asset Management Menu")
    print("1: Add asset")
    print("2: Remove asset")
    print("3: Calculate real time asset prices")
    print("0: Return to main menu")


def liability_management_menu():
    print("Liability and Debt Managment Menu")
    print("1: Add Liability")
    print("2: Remove Liability")
    print("3: Track outstanding debt and payment debt") #will allow user to make a payment and reduce the debt recorded in AdvFi
    print("0: Return to main menu")


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
    home_screen()
    
