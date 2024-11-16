'''
Author: Mason Myre
Purpose: to hold all of the entities for a user, and to allow the user to calculate the total value of their liabilities and assets
11-5: updated to be compatible with associated use cases
'''

import Entity  # python is lying, entity class is certainly used, dynamic typing is just clueless
import UserAccount #idk if we need this one
import Category

class EntityPortfolio:

    assets = []
    liabilities = []
    total_assets_value = 0.00
    total_liabilities_value = 0.00
    total_value = 0.00
    next_entity_ID = 0  # will use this to ensure unique entity IDs, will increment every time we add a new entity, will not decrement when entity is deleted
    category_list = []

    def __init__(self):
        self.name = "Default Category"  #create a default category for entites that do not get assigned a category
        self.description = ""
        self.cat = Category.Category(self.name, self.description)
        self.category_list.append(self.cat)
        
    
    
    #  add a category with a name and description to the category list
    def add_category(self, name, description):
        for category in self.category_list:
            if category.get_name() == name:
                return False    # do not allow two categories with the same name
            
        # allow adding a category if the name is unique
        cat = Category(name, description)
        self.category_list.append(cat)

    def remove_category(self, name):
        if name == "Default Category":  #do not allow user to delete the default category - this ensures we never have zero categories and always have a generic category for entities
            return False                
        for i in range(len(self.category_list)):
            if self.category.get_name() == name:
                self.category_list.pop(i)
                return True #return true now to represent that we found the category we were searching for as well as prevent looping through the rest of the list
        
        #could not find the correspoinding category name
        return False
    
    def get_category_list(self):
        return self.category_list
    
    #get a category at a specific index
    def get_category(self, index):
        if index < len(self.category_list):  #handle error: given index is larger than the length of the category list
            return self.category_list[index] 
        else:
            return self.category_list[0]  #solution: just return the default category, this implementation prevents the deletion of the default category and always ensures it is stored at the 0 index
    
    #add given entity as an asset
    def add_asset(self, entity: Entity):
        self.entityCount += 1  # increment next_entity_ID 
        entity.set_type("asset") #set entity type as asset
        entity.set_entity_ID(self.next_entity_ID)
        self.assets.append(entity)
        self.update_values()  # do this every time we add or remove an entity to ensure that we always give the user up-to-date information
        return True
        
    #will need to thoroughly test remove functions because I do not trust them to work first try
    def remove_asset(self, entity_ID):
        for asset in self.assets:
            if asset.get_entity_ID() == entity_ID:
                self.assets.remove(asset)
                self.update_values()
                return True
        print("Error: could not find the corresponding asset ID, please ensure you provide a valid entity ID")
        return False
    
    def add_liability(self, entity: Entity):
        self.next_entity_ID += 1
        entity.set_type("liability")
        entity.set_entity_ID(self.next_entity_ID)
        self.liabilities.append(entity)
        self.update_values()
        return True
    
    def remove_liability(self, entity_ID):
        for liability in self.liabilities:
            if liability.get_entity_ID() == entity_ID:
                self.liabilities.remove(liability)
                self.update_values()
                return True
        print("Error: could not find the corresponding liability ID, please ensure you provide a valid entity ID")
        return False    


    #function to update total asset value, total liability value, and total portfolio value to ensure accuracy
    def update_values(self):
        updated_asset_value = 0
        updated_liability_value = 0

        for entity in self.assets:
            updated_asset_value += entity.get_total_value()
        
        for entity in self.liabilities:
            updated_liability_value += entity.get_total_value()
        
        self.total_assets_value = updated_asset_value
        self.total_liabilities_value = updated_liability_value
        self.total_value = updated_asset_value - updated_liability_value


    #getters
    def get_asset_list(self):
        return self.assets
    
    def get_liability_list(self):
        return self.liabilities
    
    def get_assets_value(self):
        self.update_values()
        return self.total_assets_value
    
    def get_liabilities_value(self):
        self.update_values()
        return self.total_liabilities_value
    
    def get_portfolio_value(self):
        self.update_values()
        return self.total_value
        
            
    
    
    

    