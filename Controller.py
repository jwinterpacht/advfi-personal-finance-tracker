'''
Mason Myre

My current mood: https://www.youtube.com/watch?v=9wtvXoXh0VU
'''

import MainUI
import Validator
import Operations


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
    

    def home_screen():
        #display main ui text
        #get user input and make sure user input is always valid
        stop = False
        while(not stop):
            user_selection = MainUI.MainUI.home_screen()
            stop = Validator.validate_home_screen_entry(user_selection)   
        Operations.home_screen_operations(user_selection)
    

    def income_management_menu():
        #display the main ui text
        #get user input and ensure validity
        stop = False
        while(not stop):
            user_selection = MainUI.MainUI.income_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.INCOME_MGMT_MENU_LOW, MainUI.MainUI.INCOME_MGMT_MENU_HIGH)
        selection = int(user_selection)
        Operations.income_management_menu_operations(selection)

    
    def income_management_menu_add_income():
        MainUI.MainUI.income_management_menu_add_income()
        amount = Controller._get_transaction_amount()
        date = Controller._get_date()
        desc = Controller._get_desc()

        Operations.create_and_add_transaction(amount, date, desc, "income")
        MainUI.MainUI.add_transaction_success()
        Controller.home_screen()

    def income_management_menu_view_income_list():
        MainUI.MainUI.income_management_menu_view_income_list()
        Operations.print_income_list()
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()

    
    def income_management_menu_remove_income():
        MainUI.MainUI.income_management_menu_view_income_list() #display the income list
        Operations.print_income_list()                          #so the user can find the relevant ID

        stop = False
        while not stop:
            income_id = MainUI.MainUI.income_management_menu_remove_income() 
            stop = Validator.validate_transaction_id(income_id)

        Operations.remove_transaction(income_id, "income")
        Controller.home_screen()

    def spending_management_menu():
        #display the main ui text
        #get user input and ensure validity
        stop = False
        while(not stop):
            user_selection = MainUI.MainUI.spending_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.SPENDING_MGMT_MENU_LOW, MainUI.MainUI.SPENDING_MGMT_MENU_HIGH)
        selection = int(user_selection)
        Operations.income_management_menu_operations(selection)

    
    def asset_management_menu():
        stop = False
        while not stop:
            user_selection = MainUI.MainUI.asset_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.ASSET_MGMT_MENU_LOW, MainUI.MainUI.ASSET_MGMT_MENU_HIGH)
        selection = int(user_selection)
        Operations.asset_management_menu_operations(selection)

        
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
        Operations.add_entity_to_portfolio("asset", name, desc, value, num_owned, auto_update, stock_symbol)


    def asset_management_menu_view_asset_list():
        Operations.asset_management_menu_view_asset_list_operations()
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()

    def asset_management_menu_delete_asset():
        #
        stop = False
        while not stop:
            id = MainUI.MainUI.asset_management_menu_delete_asset()
            stop = Validator.validate_entity_id("asset", id)
        #once the asset id is validated we need to actually remove the asset
        Operations.remove_entity_from_portfolio("asset", id)
        Controller.home_screen()

    def liability_management_menu():
        stop = False
        while not stop:
            user_selection = MainUI.MainUI.liability_management_menu()
            stop = Validator.validate_menu_entry(user_selection, MainUI.MainUI.LIABILITY_MGMG_MENU_LOW, MainUI.MainUI.LIABILITY_MGMG_MENU_HIGH)
        selection = int(user_selection)
        print(selection)
        Operations.liability_management_menu_operations(selection)

    def liability_management_menu_add_liability():
        print("test 3")
        #since we will have no liabilies that auto update, we will not include stocks
        #anyone who is smart enough to be shorting stocks is not really our taraget audience
        num_owned = 1  #for sake of simplicity, we only allow one copy of each liability
        name = Controller._get_name()
        desc = Controller._get_desc()
        value = Controller._get_entity_value()
        auto_update = False
        stock_symbol = "n/a"

        Operations.add_entity_to_portfolio("liability", name, desc, value, num_owned, auto_update, stock_symbol)



    def liability_management_menu_view_liability_list():
        Operations.liability_management_menu_view_liability_list_operations()
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()

        


        
    def retrieve_transactions():
        MainUI.MainUI.retrieve_transactions()
        Operations.print_transactions()
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()
        
        


        

    

def main():
    Controller.home_screen()


if __name__ == "__main__":
    main()