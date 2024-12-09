import Transaction
import TransactionList
import Category
import CategoryList
import Operations
from datetime import datetime as dt
transaction_list = TransactionList.TransactionList()
def test_add_income():
    amount = 100
    date = "12/07/24"
    desc = "test desc"
    type = "income"
    Operations.Operations.create_and_add_transaction(transaction_list, amount, date, desc, type)
    new_income = transaction_list.get_transaction(1)
    assert new_income.get_amount() == amount
    assert new_income.get_transaction_date() == dt.strptime(date, '%m/%d/%y')
    assert new_income.get_description() == desc

category_list = CategoryList.CategoryList()
new_cat = Category.Category("test", "category used for testing")

def test_add_budget():
    category_list.add_category(new_cat)
    new_cat.set_budget(600.0)
    assert new_cat.get_budget() == 600.0

def test_remove_budget():
    new_cat.set_budget(-1.0)
    assert new_cat.get_budget() == -1.0




    