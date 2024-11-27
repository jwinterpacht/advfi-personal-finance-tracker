'''
Mason Myre

My current mood: https://www.youtube.com/watch?v=9wtvXoXh0VU
'''

import MainUI
import Validator
import Operations
import EntityPortfolio
import Entity
import Transaction
import TransactionList


entity_portfolio = EntityPortfolio.EntityPortfolio()
transaction_list = TransactionList.TransactionList()




class Controller:

    #internal functions
    def _get_transaction_amount():
        stop = False
        while not stop:
            amount = MainUI.MainUI.get_transaction_amount() #single use principle
            stop = Validator.validate_value(amount)
        return amount
    
    def _get_date():
        stop = False
        while not stop:
            date = MainUI.MainUI.get_date()
            stop = Validator.validate_transaction_date(date)
        return date
    
    def _get_desc():
        desc = MainUI.MainUI.get_desc()
        return desc

    def _get_num_owned():
        stop = False
        while not stop:
            num_owned = MainUI.MainUI.get_num_owned()
            stop = Validator.validate_num_owned(num_owned)
        return num_owned

    def _get_entity_value():
        stop = False
        while not stop:
            value = MainUI.MainUI.get_entity_value()
            stop = Validator.validate_value(value)
        return float(value)
    
    def _get_name():
        stop = False
        while not stop:
            name = MainUI.MainUI.get_entity_name()
            stop = Validator.validate_name(name)
        return name
    
    def _get_stock_symbol():
        stop = False
        while not stop:
            stock = MainUI.MainUI.get_stock_symbol()
            stop = Validator.validate_stock_symbol(stock)
        return stock
    
    def _calculate_current_net_worth():
        entity_portfolio.update_values()
        net_worth = 0 #reset net worth value
        net_worth += transaction_list.get_total_income()  #add total income
        net_worth -= transaction_list.get_total_expenses() #add total expense
        net_worth += entity_portfolio.total_value
        return net_worth #now we have a complete picture of the net worth so we can just return that
    

    def home_screen():
        #display main ui text
        #get user input and make sure user input is always valid
        stop = False
        net_worth = Controller._calculate_current_net_worth()
        while(not stop):
            user_selection = MainUI.MainUI.home_screen(net_worth)
            stop = Validator.validate_home_screen_entry(user_selection)   
        selection = int(user_selection)
        match selection:
            case 1:
                Controller.income_management_menu()
            case 2:
                Controller.spending_management_menu()
            case 3: 
                Controller.asset_management_menu()
            case 4: 
                Controller.liability_management_menu()
            case 5:
                #Controller.financial_reports_menu()
                pass
            case 6:
                Controller.retrieve_transactions()
            case 7: 
                #Controller.alert_center_menu()
                pass
            case 8:
                #Controller.program_settings_menu()
                pass
            case 9:
                MainUI.MainUI.exit_adv_fi()
                exit(0)     

    def income_management_menu():
        #display the main ui text
        #get user input and ensure validity
        stop = False
        while(not stop):
            user_selection = MainUI.MainUI.income_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.INCOME_MGMT_MENU_LOW, MainUI.MainUI.INCOME_MGMT_MENU_HIGH)
        selection = int(user_selection)
        match selection:
            case 1:
                Controller.income_management_menu_add_income()
            case 2:
                Controller.income_management_menu_view_income_list()
            case 3:
                Controller.income_management_menu_remove_income()
            case 0:
                Controller.home_screen()

    
    def income_management_menu_add_income():
        MainUI.MainUI.income_management_menu_add_income()
        amount = Controller._get_transaction_amount()
        date = Controller._get_date()
        desc = Controller._get_desc()

        Operations.create_and_add_transaction(transaction_list, amount, date, desc, "income")
        MainUI.MainUI.add_transaction_success()
        Controller.home_screen()

    def income_management_menu_view_income_list():
        MainUI.MainUI.income_management_menu_view_income_list()
        Operations.print_income_list(transaction_list)
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()

    
    def income_management_menu_remove_income():
        MainUI.MainUI.income_management_menu_view_income_list() #display the income list
        Operations.print_income_list(transaction_list)                          #so the user can find the relevant ID

        stop = False
        while not stop:
            income_id = MainUI.MainUI.remove_transaction() 
            stop = Validator.validate_transaction_id(transaction_list, income_id, "income")

        Operations.remove_transaction(transaction_list, income_id, "income")
        Controller.home_screen()

    def spending_management_menu():
        #display the main ui text
        #get user input and ensure validity
        stop = False
        while(not stop):
            user_selection = MainUI.MainUI.spending_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.SPENDING_MGMT_MENU_LOW, MainUI.MainUI.SPENDING_MGMT_MENU_HIGH)
        selection = int(user_selection)
        print(selection)
        match selection:
            case 0:
                Controller.home_screen()
            case 1: 
                Controller.spending_management_menu_add_expense()
            case 2:
                Controller.spending_management_menu_view_expense_list()
            case 3:
                Controller.spending_management_menu_delete_expense()
            case 4:
                #Controller.spending_management_menu_import_spending_CSV()
                pass

    def spending_management_menu_add_expense():
        MainUI.MainUI.spending_management_menu_add_expense()
        amount = Controller._get_transaction_amount()
        date = Controller._get_date()
        desc = Controller._get_desc()

        Operations.create_and_add_transaction(transaction_list, amount, date, desc, "expense")
        MainUI.MainUI.add_transaction_success()
        Controller.home_screen()
    
    def spending_management_menu_view_expense_list():
        MainUI.MainUI.clear_screen()
        Operations.print_expense_list(transaction_list)
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()
    
    def spending_management_menu_delete_expense():
        MainUI.MainUI.clear_screen() #
        Operations.print_expense_list(transaction_list)

        stop = False
        while not stop:
            expense_id = MainUI.MainUI.remove_transaction() 
            stop = Validator.validate_transaction_id(transaction_list, expense_id, "expense")
        Operations.remove_transaction(transaction_list, expense_id, "expense")
        Controller.home_screen()    

    def asset_management_menu():
        assets_value = entity_portfolio.total_assets_value
        stop = False
        while not stop:
            user_selection = MainUI.MainUI.asset_management_menu(assets_value)
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.ASSET_MGMT_MENU_LOW, MainUI.MainUI.ASSET_MGMT_MENU_HIGH)
        selection = int(user_selection)
        match selection:
            case 1:
                Controller.asset_management_menu_add_asset()
            case 2:
                Controller.asset_management_menu_view_asset_list()
            case 3:
                Controller.asset_management_menu_delete_asset()
            case 4:
                Controller.asset_management_menu_update_assets()
            case 0:
                Controller.home_screen()

        
    def asset_management_menu_add_asset():
        #need num owned, value per entity, name, desc, auto update & stock symbol
        stop = False
        while not stop:
            is_stock = MainUI.MainUI.asset_management_menu_add_asset_is_stock()
            stop = Validator.validate_yes_no(is_stock)
        
        num_owned = Controller._get_num_owned()
        if num_owned == "":
            num_owned = 1
        name = Controller._get_name()
        desc = Controller._get_desc()

        if is_stock[0] == "n":
            value = Controller._get_entity_value()
            auto_update = False
            stock_symbol = "n/a"
        elif is_stock[0] == "y":
            #can pass in value as 0 because we will automatically update it anyway
            value = 0
            auto_update = True #tell entity.py that this is a stock and that the symbol matters
            stock_symbol = Controller._get_stock_symbol()        
        #now that we have all the data we need to create a non stock asset, we will
        #call a method in operations to do exactly that
        Operations.add_entity_to_portfolio(entity_portfolio, "asset", name, desc, value, num_owned, auto_update, stock_symbol)
        Controller.home_screen()


    def asset_management_menu_view_asset_list():
        Operations.asset_management_menu_view_asset_list_operations(entity_portfolio)
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()

    def asset_management_menu_delete_asset():
        #3
        Operations.asset_management_menu_view_asset_list_operations(entity_portfolio)
        stop = False
        while not stop:
            id = MainUI.MainUI.asset_management_menu_delete_asset()
            stop = Validator.validate_entity_id(entity_portfolio, "asset", id)
        #once the asset id is validated we need to actually remove the asset
        Operations.remove_entity_from_portfolio(entity_portfolio, "asset", id)
        Controller.home_screen()
    
    def asset_management_menu_update_assets():
        EntityPortfolio.EntityPortfolio.update_values(entity_portfolio)
        MainUI.MainUI.update_asset_values_success()
        Controller.home_screen()

    def liability_management_menu():
        stop = False
        while not stop:
            user_selection = MainUI.MainUI.liability_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.LIABILITY_MGMG_MENU_LOW, MainUI.MainUI.LIABILITY_MGMG_MENU_HIGH)
        selection = int(user_selection)
        match selection:
                case 0:
                    Controller.home_screen()
                case 1:
                    Controller.liability_management_menu_add_liability()
                case 2:
                    Controller.liability_management_menu_view_liability_list()
                case 3:
                    Controller.liability_management_menu_make_liability_payment()
                case 4:
                    Controller.liability_management_menu_delete_liability()
                case 5:
                    Controller.liability_management_menu_track_debt()

    def liability_management_menu_add_liability():
        MainUI.MainUI.liability_management_menu_add_liability()
        #since we will have no liabilies that auto update, we will not include stocks
        #anyone who is smart enough to be shorting stocks is not really our taraget audience
        num_owned = 1  #for sake of simplicity, we only allow one copy of each liability
        name = Controller._get_name()
        desc = Controller._get_desc()
        value = Controller._get_entity_value()
        auto_update = False
        stock_symbol = "n/a"

        Operations.add_entity_to_portfolio(entity_portfolio, "liability", name, desc, value, num_owned, auto_update, stock_symbol)

        Controller.home_screen()


    def liability_management_menu_view_liability_list():
        Operations.liability_management_menu_view_liability_list_operations(entity_portfolio)
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()

    def liability_management_menu_make_liability_payment():
        Operations.liability_management_menu_view_liability_list_operations(entity_portfolio)
        stop = False
        while not stop:
            id = MainUI.MainUI.liability_management_menu_get_liability_id()
            stop = Validator.validate_entity_id(entity_portfolio, "liability", id)
        #once we have found the corresponding liability ID
        #we get the amount that that the user has just paid into the liability
        stop = False
        while not stop:
            payment = MainUI.MainUI.get_payment_value()
            stop = Validator.validate_payment_debt(payment, entity_portfolio, id)
        #now that the payment is validated, we have to apply it to the debt
        Operations.make_liability_payment_operations(entity_portfolio, id, payment)
        Controller.home_screen()
    
    def liability_management_menu_delete_liability():
        Operations.liability_management_menu_view_liability_list_operations(entity_portfolio)
        stop = False
        while not stop:
            id = MainUI.MainUI.liability_management_menu_get_liability_id()
            stop = Validator.validate_entity_id(entity_portfolio, "liability", id)
        Operations.remove_entity_from_portfolio(entity_portfolio, "liability", id)
        Controller.home_screen()

    def liability_management_menu_track_debt():
        #print out each debt and how much is left to be paid
        debt_status = Operations.liability_management_menu_track_debt_operations(entity_portfolio)
        MainUI.MainUI.liability_track_debt(debt_status)
        Controller.home_screen()



        


        
    def retrieve_transactions():
        MainUI.MainUI.retrieve_transactions()
        Operations.print_transactions(transaction_list)
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()
        
        


        

    

def main():
    test_debt = Entity.Entity(100, 1, "Student Debt", "", False, "n/a")
    entity_portfolio.add_liability(test_debt)
    Controller.home_screen()


if __name__ == "__main__":
    main()