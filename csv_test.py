import csv
from typing import List
from transaction_list import Transaction, TransactionList

objects = []
transaction_list_object: TransactionList
with open ('IT_326_CSV_File.csv', 'r') as file:
    next(file) #Skipping header row (With all naming conventions)
    for row in file:
        income_or_expense = row[0]
        if(row[0] == "Expense"):
            TransactionList.add_expense_transaction(row)
        else:
            TransactionList.add_income_transaction(row)

    print(transaction_list_object.get_total_income)
    print(transaction_list_object.get_total_expense)



        

# expenses and incomes tranactionsList 
# Read line by line and for expense or income call method addincome or addexpense to transactionList based on first attribute "Expense" or "Income"

# with open ('IT_326_CSV_File.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     dataList = list(csv.reader(file))

# print(dataList)