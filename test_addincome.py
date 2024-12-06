import unittest
import Transaction
import Operations
from datetime import datetime as dt

#https://www.youtube.com/watch?v=6tNS--WetLI

#assertion test funcs: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class TestIncome(unittest.TestCase):
    date = "10/23/24"
    date = dt.strptime(date, '%m/%d/%y')
    income_obj = Transaction.Transaction(500, date, "Paycheck")


    #test_ naming convention required
    #testing transaction
    def test_add(self):
        result = self.income_obj.get_amount()


#testing adding to database
    def test_db_add(self):
        #first, give a category name
        result = Operations.Operations.add_income_to_database(self.income_obj)
        self.assertEqual(True, result) #if result is True, then income successfully added to db

    def test_db_get(self):
        result = Operations.Operations.pull_incomes_from_database(self.income_obj)
        self.assertEqual(True, result) #if result is True, then income(s) successfully grabbed from db