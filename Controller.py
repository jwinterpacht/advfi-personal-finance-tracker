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
    
    def _get_name():
        name = MainUI.MainUI.get_entity_name()
        return name

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
            stop = Validator.validate_income_management_menu_entry(user_selection)
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

    
    def asset_management_menu():
        
        stop = False
        while not stop:
            user_selection = MainUI.MainUI.asset_management_menu()
            stop = Validator.validate_asset_management_menu_entry(user_selection)
        selection = int(user_selection)
        Operations.asset_management_menu_operations(selection)

        
    def asset_management_menu_add_asset():
        #need num owned, value per entity, name, desc, auto update & stock symbol
        stop = False
        while not stop:
            is_stock = MainUI.MainUI.asset_management_menu_add_asset_is_stock()
            stop = Validator.validate_yes_no(is_stock)
        
        num_owned = Controller._get_num_owned()
        name = Controller._get_name()
        desc = Controller._get_desc()

        if is_stock == "n":
            value = Controller._get_entity_value()
            auto_update = False
        elif is_stock == "y":
            pass


    
    

        

        


        
    def retrieve_transactions():
        MainUI.MainUI.retrieve_transactions()
        Operations.print_transactions()
        MainUI.MainUI.wait_for_user_input()
        Controller.home_screen()
        
        


        

    

def main():
    Controller.home_screen()


if __name__ == "__main__":
    main()