'''
Author: Mason Myre
Purpose: to be used by entity and transaction to keep track of different spending/income/asset/liability categories
Time to work on the part of this program that has given me the most headaches
(aside from the factory reporting stuff but I'm just pretending that doesn't exist for now)

Here's how this will work: we're gonna have a parent called CategoryList.py that will hold a list of the categories
    This will also have all of the methods/functions we want
    Each instance of a category will have 4 lists the assets, liabilities, incomes, and expenses associated with that category
    Each asset/liability/income/expense will also have a string varaible for the category name that can be displayed when printing out the information


'''

#11-5: updated to be compatible with associated use cases && added params to __init__

import Transaction
import Entity

class Category:

    def __init__(self, name, description = ""): 
        self._category_name = name
        self._category_description = description

        self._asset_list = []
        self._liability_list = []
        self._income_list = []
        self._expense_list = []

        self._asset_count = 0
        self._liability_count = 0
        self._income_count = 0
        self._expense_count = 0

        self._budget = -1.0  #a budget of -1 will be used to signify that this category does not have a given budget

        
    
    def get_name(self):
        return self._category_name
    
    def get_description(self):
        return self._category_description
    
    def set_name(self, new_name):
        self._category_name = new_name
    
    def set_description(self, new_description):
        self._category_description = new_description
    
    def add_asset(self, asset: Entity):
        self._asset_count += 1
        self._asset_list.append(asset)
    
    def add_liability(self, liability: Entity):
        self._liability_count += 1
        self._liability_list.append(liability)
    
    def add_income(self, income: Transaction):
        self._income_count += 1
        self._income_list.append(income)
    
    def add_expense(self, expense: Transaction):
        self._expense_count += 1
        self._expense_list.append(expense)
    
    #remove items
    def remove_asset(self, asset: Entity):
        self._asset_count -= 1
        self._asset_list.remove(asset)
    
    def remove_liability(self, liability: Entity):
        self._liability_count -= 1
        self._liability_list.remove(liability)
    
    def remove_income(self, income: Transaction):
        self._income_count -= 1
        self._income_list.remove(income)
    
    def remove_expense(self, expense: Transaction):
        self._expense_count -= 1
        self._expense_list.remove(expense)
    
    #wasn't sure what the best name for this one was but the idea is that when you delete a category from the category list
    #you also need to makes sure that the items which were previously associated with that category get the category_name field reset
    def reset_item_category_names(self):
        for income in self._income_list:
            income.set_category_name("")
        for expense in self._expense_list:
            expense.set_category_name("")
        for asset in self._asset_list:
            asset.set_category_name("")
        for liability in self._liability_list:
            liability.set_category_name("")
    
    #used to help print out all of the items associated with a given category
    def get_category_items_str(self) -> str:
        items_str = f"All items associated with the category '{self.category_name}'\n\n"
        if self._income_count > 0:
            items_str += "Income List:\n"
            for income in self._income_list:
                items_str += f"{income.print_transaction()}\n"
            items_str += "\n"
        if self._expense_count > 0:
            items_str += "Expense List:\n"
            for expense in self._expense_list:
                items_str += f"{expense.print_transaction()}\n"
            items_str += "\n"
        if self._asset_count > 0:
            items_str += "Asset List:\n"
            for asset in self._asset_list:
                items_str += f"{asset.print_entity()}"
            items_str += "\n"
        if self._liability_count > 0:
            items_str += "Liability List:\n"
            for liability in self._liability_list:
                items_str += f"{liability.print_entity()}"
        return items_str

    def set_budget(self, budget: str) -> None:
        budget = float(budget)
        self._budget = budget
    
    def get_budget(self) -> float:
        return self.budget
    
    def get_budget_adherence(self):
        #grab the total of all the expenses that have happened within the last month
        monthly_expenses = 0.0 #set as a float
        for expense in self._expense_list:
            if expense.get_is_within_last_month():
                monthly_expenses += expense.get_amount()
        percent_spent = (monthly_expenses/self._budget) * 100
        return f"{self._category_name}\tAmount spent this month: ${monthly_expenses:.2f}\tTotal budget: ${self._budget}\tPercentage spent: {percent_spent:.2f}%"
    

    



































