'''
Mason Myre

My current mood: https://www.youtube.com/watch?v=9wtvXoXh0VU
'''

import MainUI
import Validator
import Operations


class Controller:

    #private functions
    def _get_amount():
        MainUI.MainUI.get_amount() #single use principle4
        amount = input("$")
        stop = Validator.validate_transaction_amount(amount)
        while not stop:
            amount = input("$")
            stop = Validator.validate_transaction_amount(amount)
        return amount
    
    def _get_date():
        MainUI.MainUI.get_date()
        stop = False
        while not stop:
            date = input()
            stop = Validator.validate_transaction_date(date)
        return date
    
    def _get_desc():
        MainUI.MainUI.get_desc()
        desc = input()
        return desc

    

    def home_screen():
        #display main ui text
        MainUI.MainUI.home_screen()

        #get user input and make sure user input is always valid
        user_selection = input()
        stop = Validator.validate_home_screen_entry(user_selection)
        while(not stop):
            user_selection = input()
            stop = Validator.validate_home_screen_entry(user_selection)   
        
        Operations.home_screen_operations(user_selection)
    
    def income_management_menu():
        #display the main ui text
        MainUI.MainUI.income_management_menu()

        #get user input and ensure validity
        user_selection = input()
        stop = Validator.validate_income_management_menu_entry(user_selection)
        while(not stop):
            user_selection = input()
            stop = Validator.validate_income_management_menu_entry(user_selection)
        
    
    def income_management_menu_add_income():
        
        MainUI.MainUI.income_management_menu_add_income()
        amount = Controller._get_amount()
        date = Controller._get_date()
        desc = Controller._get_desc()

        

        



        


        

    

def main():
    Controller.home_screen()


if __name__ == "__main__":
    main()