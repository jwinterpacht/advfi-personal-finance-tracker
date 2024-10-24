'''
Budget class
By Jonah Raef
10-17-2024

This also manages the Alerts.
STILL NEED TO MAKE ALERTS ACTUALLY TRIGGER IN THE APP. I THINK ADDING THIS IS FATHOMABLE AFTER WE HAVE SOME FUNCTIONALITY IN 'MAIN'

This class requires Python 3.12 for the 'match' functionality.
'''
from datetime import date
import Alert

print("Running: Budget.py")

#Temp class while Jaden makes the actual 'Transaction' class.
class Transaction:
    amount = 0
    description = ""
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description


''' Budget Class
If a date is the default value of (1, 1, 1) then it means the user
    did not (or did not want to) define a date for their Budget.
'''
class Budget:
    budgetTotal = 0.0
    remainingBudget = 0.0 #Calculation: budgetTotal + income[] - expenses[]
    category = ""
    startDate = date(1, 1, 1) #Uses imported 'Date' class from Python library
    endDate = date(1, 1, 1) # year/month/day (i.e. 2024/10/17)
    income = []
    expenses = []
    alertList = [] #A list of Alert objects

    #For AdvFi System: Find an efficient way to automatically [delete or archive] a Budget on endDate, UNLESS the endDate is (1, 1, 1)

    '''
    budgetTotal is required for a Budget object.
    category, startDate, endDate are all optional parameters.
    '''
    def __init__(self, budgetTotal, categorty="", startDate=date(1,1,1), endDate=date(1,1,1)):
        self.budgetTotal = budgetTotal
        self.category = categorty
        self.startDate = startDate
        self.endDate = endDate

    def calculateRemainingBudget(self):
        incomeTotal = 0
        expenseTotal = 0
        for item in self.income:
            incomeTotal = incomeTotal + item.amount
        
        for item in self.expenses:
            expenseTotal = expenseTotal - item.amount

        self.remainingBudget = self.budgetTotal + incomeTotal + expenseTotal #adding expenseTotal because it's negative
        if(self.remainingBudget < 0):
            print("Warning: you have exceeded your budget!")

    '''description is optional'''
    def addIncome(self, amt, desc=""):
        tempTrans = Transaction(amt, desc)
        self.income.append(tempTrans)
        self.calculateRemainingBudget() #update the remaining budget

    '''description is optional'''
    def addExpense(self, amt, desc=""):
        tempTrans = Transaction(amt, desc)
        self.expenses.append(tempTrans)
        self.calculateRemainingBudget() #update the remaining budget

    '''Add an Alert that is triggered by an event happening within this budget'''
    def addAlert(self, type, description, time, frequency, recur):
        self.alertType = type
        self.alertDescription = description
        self.alertTime = time
        self.alertFrequency = frequency
        self.alertsList.append(Alert(type, description, time, frequency, recur))

    '''Remove an alert from the list'''
    def removeAlert(self, alert):
        self.alertsList.remove(alert)

    '''Modify the parameters of an alert for this budget
    '''
    def modifyAlert(self, alert):
        print('What aspect of this alert would you like to modify?')
        #print('1. Type\n2. Description\n3. Time\n4. Frequency\n5. Recurrance')
        user_input = input("1. Type\n2. Description\n3. Time\n4. Frequency\n5. Recurrance")

        match user_input:
            case "1":
                new_type = input("Enter the new type: ")
                alert.alert_type = new_type
            case "2":
                new_description = input("Enter the new description: ")
                alert.alert_description = new_description
            case "3":
                try:
                    new_time = float(input("Enter the new time (e.g., 15.5 for 3:30 PM): "))
                    alert.alert_time = new_time
                except ValueError:
                    print("Invalid time format. Please enter a number.")
            case "4":
                new_frequency = input("Enter the new frequency [hourly, daily, weekly, monthly]: ")
                alert.alert_frequency = new_frequency
            case "5":
                # Assuming recurrence is toggled on/off
                if alert.isRecurring():
                    alert.alert_frequency = None
                    print("Recurrence turned off.")
                else:
                    new_frequency = input("Enter the recurrence frequency (e.g., daily, weekly): ")
                    alert.alert_frequency = new_frequency
                    print("Recurrence turned on.")
            case _:
                print("Invalid input.")


    #GETTERS
    def getStartDate(self):
        return self.startDate
    
    def getEndDate(self):
        return self.endDate
    
    def getBudget(self):
        return self.budgetTotal
    
    def getCategory(self):
        return self.category
    
    def getRemainingBudget(self):
        return self.remainingBudget #updated every time addIncome or addExpense is called

    def printIncomeList(self):
        for item in self.income:
            if(item.description != ""):
                print('+' + str(item.amount) + ": " + item.description)
            else:
                print('+' + str(item.amount))

    def printExpenseList(self):
        for item in self.expense:
            if(item.description != ""):
                print('-' + str(item.amount) + ": " + item.description)
            else:
                print('-' + str(item.amount))

    #SETTERS
    '''startDate is a 'date' class object 
        unfortunately, can't override in Python, so can't allow user to
        pass in (year, month, day) with the same func name'''
    def setStartDate(self, startDate):
        self.startDate = startDate
    
    def setEndDate(self, endDate):
        self.endDate = endDate

    #amt is a float or int
    def setBudget(self, amt):
        self.budgetTotal = amt

    #categorty is a string
    def setCategory(self, category):
        self.category = category


'''
#TESTING ENVIRONMENT!!
test_budget = Budget(1500, "bi-weekly entertainment and expenses budget.")
test_budget.setStartDate(date(2024, 10, 17))
test_budget.setEndDate(date(2026, 10, 17))
test_budget.addExpense(512, "car repair")

test_budget.addIncome(145, "sold Nvidia stocks")
test_budget.addIncome(175, "traded in phone")
test_budget.addIncome(50, "birthday money")
test_budget.addIncome(200, "fur cut for dogs + tip")
print("\nPrinting income list: ")
test_budget.printIncomeList()
print("Budget remaining: " + str(test_budget.getRemainingBudget()))

print("\nPrinting expense list: ")



print('Entire program successfully ran :D')
'''