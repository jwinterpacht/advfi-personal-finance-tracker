import TransactionList
import EntityPortfolio

class UserAccount:
    def __init__(self):
        #self._username = username
        self.new_user = True  #only hardcode this to False in testing
        self._password = "admin"
        self._pin = "1515"

    def set_password(self, new_password):
        self._password = new_password
    
    def set_pin(self, new_pin):
        self._pin = new_pin
    
    #pass in the password to the user account instead of bringing the actual password from the user account
    #increases overall program security
    def check_password(self, input_password):
        if self._password == input_password:
            return True
        return False
    
    def check_pin(self, input_pin):
        if self._pin == input_pin:
            return True
        return False
