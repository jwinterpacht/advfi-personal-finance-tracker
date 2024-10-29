class UserAccount:
    def __init__(self, username, password, date_created, entities):
        self.username = username
        self.password = password
        self.date_created = date_created
        self.entites = entities #For EntityPortfolio
        self.net_worth = 0.0

    # Getter for asset total for an entity 
    def get_asset_total(self):
        return self.entites.get_asset_total()
    
    # Getter for liability total for an entity
    def get_liability_total(self):
        return self.entites.get_liability_total()
    
    #Used to calculate networth by using assets vs liabilities 
    def calculate_net_worth(self):
        self.net_worth = self.get_asset_total() - self.get_liability_total()
        return self.net_worth
    
    #Mock Entity Portfolio for testing simple
class EntityPortfolio:
    def __init__(self, assets, liabilities):
        self.assets = assets # List of asset values
        self.liabilites = liabilities # List of liabilities

    def get_asset_total(self):
        return sum(self.assets)
    
    def get_liability_total(self):
        return sum(self.liabilites)

portfolio = EntityPortfolio([10000, 5000, 2000], [3000, 1000])

user = UserAccount("Frank", "Admin", "2024-10-23", portfolio)

print("Asset Total: ", user.get_asset_total()) #Expected 17000
print("Liability Total: ", user.get_liability_total()) #Expected 4000
print("Net Worth: ", user.calculate_net_worth()) #Expected 13000
