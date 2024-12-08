import mysql.connector
import Transaction
import TransactionList



class MySQLOperations:
    '''
    WARNING: This function will CRASH the program if you're not on at least: mysql-connector version 2.2.9
    Run in bash: pip install --upgrade mysql-connector-python
    'type' determines what Transaction type (income or expense) we are handling
    '''
    def add_transaction_to_database(the_transaction: Transaction, type: str):
        #Validator.validate_database_connection() proves that db connection is established. But, keep try-catch in case of unforseen failure?
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            add_income_query = ("INSERT INTO income (amount, transaction_date, trans_desc, category_name, id) "
                            "VALUES (%s, %s, %s, %s, %s)") # '%s' is a SQL.connector placeholder for ANY datatype...so we WIN!
            
            add_expense_query = ("INSERT INTO expense (amount, transaction_date, trans_desc, category_name, id) "
                                "VALUES (%s, %s, %s, %s, %s)")
            
            new_transaction_data = (the_transaction.get_amount(), the_transaction.get_transaction_date(),
                            the_transaction.get_description(), the_transaction.get_category_name(), the_transaction.get_transaction_id() )

            if type == "income":
                #add the data to database using the above query
                db_cursor.execute(add_income_query, new_transaction_data) #execute() sends query to the SQL database server for execution
            else: #type == "expense"
                db_cursor.execute(add_expense_query, new_transaction_data)

            db.commit() #commit() saves changes, made by cursor(), into the database

            #close database connection; avoid any possible trouble because we good programmer
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not store income to database. Error: {e}")
            return False #added bools for testing
        return True


    def pull_trans_from_database(transaction_list: TransactionList):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor()

            db_cursor.execute("SELECT * FROM income")
            incomes = db_cursor.fetchall()

            #go through each attribute, income-by-income
            for row in incomes:
                amount = row[0]
                trans_date = row[1]
                desc = row[2]
                category_name = row[3]
                trans_id = row[4]

                #add transaction to the transaction_list
                trans = Transaction.Transaction(amount, trans_date, desc) #limits of Transaction.__init__
                trans.set_category_name(category_name)
                trans.set_transaction_id(trans_id)
                transaction_list.add_income_transaction(trans)



            '''EXPENSES'''
            db_cursor.execute("SELECT * FROM expense")
            incomes = db_cursor.fetchall()
            #go through each attribute, income-by-income
            for row in incomes:
                amount = row[0]
                trans_date = row[1]
                desc = row[2]
                category_name = row[3]
                trans_id = row[4]

                #add transaction to the transaction_list
                trans = Transaction.Transaction(amount, trans_date, desc) #limits of Transaction.__init__
                trans.set_category_name(category_name)
                trans.set_transaction_id(trans_id)
                transaction_list.add_expense_transaction(trans)

            #close database connection
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not grab income to database Please exit AdvFi and fix to save your data. Error: {e}")
            return False #added bools for testing
        return True

    def delete_transaction_from_db(transaction_list: TransactionList, id: str, type: str):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            del_income_query = ("DELETE FROM income WHERE id = %s")
            del_expense_query = ("DELETE FROM expense WHERE id = %s")

            if type == "income":
                #add the data to database using the above query
                db_cursor.execute(del_income_query, (id,)) #execute() sends query to the SQL database server for execution
            else: #type == "expense"
                db_cursor.execute(del_expense_query, (id,)) #passing 'id' as a 'tuple' to make .execute() func happy

            db.commit() #commit() saves changes, made by cursor(), into the database

            #close database connection; avoid any possible trouble because we good programmer
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not remove transaction from database. Error: {e}")
            return False #added bools for testing
        return True
