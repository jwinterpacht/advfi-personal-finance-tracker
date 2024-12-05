import csv
from datetime import datetime
from TransactionList import TransactionList
from Transaction import Transaction

transaction_list_object = TransactionList()

with open('transactions.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        if len(row) < 5:  # Ensure there are enough columns
            continue

        # Parse transaction date
        try:
            transaction_date = datetime.strptime(row[0], '%m/%d/%Y').date()
        except ValueError:
            print(f"Invalid date format in row: {row}")
            continue

        # Determine amount and description
        withdrawal_amount = row[3].strip()
        deposit_amount = row[4].strip()
        description = row[2].strip() if row[2] else "No description"

        # Determine income or expense and parse amount
        if withdrawal_amount:
            amount = float(withdrawal_amount)
            income_or_expense = "Expense"
        elif deposit_amount:
            amount = float(deposit_amount)
            income_or_expense = "Income"
        else:
            print(f"Invalid transaction data in row: {row}")
            continue

        # Create Transaction object
        transaction = Transaction(amount=amount, transaction_date=transaction_date, description=description)

        # Add transaction to the correct list
        if income_or_expense == "Expense":
            transaction_list_object.add_expense_transaction(transaction)
        else:
            transaction_list_object.add_income_transaction(transaction)

# Print total income and expenses
print(f"Total Income: {transaction_list_object.get_total_income()}")
print(f"Total Expense: {transaction_list_object.get_total_expenses()}")