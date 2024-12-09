import mysql.connector
import Transaction
import TransactionList
import Entity
import EntityPortfolio
import CategoryList
import Category
import MainUI #need for util print
#import time #for debugging


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
                transaction_list.add_income_transaction(trans, True)



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
                transaction_list.add_expense_transaction(trans, True)

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



    '''ENTITY STUFF'''
    def add_entity_to_db(type: str, name, desc, value, num_owned, auto_update, stock_symbol, id):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            add_asset_query = ("INSERT INTO asset (entity_value, entity_amount, entity_name, entity_desc, entity_auto_update, entity_stock_symbol, id) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            
            add_liability_query = ("INSERT INTO liability (entity_value, entity_amount, entity_name, entity_desc, entity_auto_update, entity_stock_symbol, id) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            
            new_entity_data = (value, num_owned, name, desc, auto_update, stock_symbol, id)

            if type == "asset":
                #add the data to database using the above query
                db_cursor.execute(add_asset_query, new_entity_data) #execute() sends query to the SQL database server for execution
            else: #type == "liability"
                db_cursor.execute(add_liability_query, new_entity_data)

            db.commit() #commit() saves changes, made by cursor(), into the database

            #close database connection; avoid any possible trouble because we good programmer
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not store income to database. Error: {e}")
            return False #added bools for testing
        return True
    
    def pull_entities_from_database(entity_portfolio: EntityPortfolio):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor()
            db_cursor.execute("SELECT * FROM asset")
            assets = db_cursor.fetchall()
            for row in assets:
                value = row[0]
                amount = row[1]
                name = row[2]
                desc = row[3]
                auto_update = row[4]
                stock_symbol = row[5]
                the_id = row[6]

                #add transaction to the transaction_list
                asset = Entity.Entity(value, amount, name, desc, auto_update, stock_symbol)
                asset.set_entity_id(the_id)
                entity_portfolio.add_asset(asset, True)
                

            '''Liabilities'''
            db_cursor.execute("SELECT * FROM liability")
            liabilities = db_cursor.fetchall()
            for row in liabilities:
                value = row[0]
                amount = row[1]
                name = row[2]
                desc = row[3]
                auto_update = row[4]
                stock_symbol = row[5]
                the_id = row[6]

                #add transaction to the transaction_list
                liability = Entity.Entity(value, amount, name, desc, auto_update, stock_symbol) #this line is where it fails
                liability.set_entity_id(the_id)
                entity_portfolio.add_liability(liability, True)
            
            #close database connection
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not grab income to database Please exit AdvFi and fix to save your data. Error: {e}")
            return False #added bools for testing
        return True
    

    def delete_entity_from_db(entity_portfolio: EntityPortfolio, type: str, id):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            del_asset_query = ("DELETE FROM asset WHERE id = %s")
            del_liability_query = ("DELETE FROM liability WHERE id = %s")

            if type == "asset":
                #add the data to database using the above query
                db_cursor.execute(del_asset_query, (id,)) #execute() sends query to the SQL database server for execution
            else: #type == "liability"
                db_cursor.execute(del_liability_query, (id,)) #passing 'id' as a 'tuple' to make .execute() func happy

            db.commit() #commit() saves changes, made by cursor(), into the database

            #close database connection; avoid any possible trouble because we good programmer
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not remove entity from database. Error: {e}")
            return False #added bools for testing
        return True



    '''Category stuff!'''
    def add_category(cat_name: str, cat_desc: str):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            add_cat_query = ("INSERT INTO category (cat_name, cat_desc) " "VALUES (%s, %s)")
            
            new_entity_data = (cat_name, cat_desc)
            db_cursor.execute(add_cat_query, new_entity_data)
            db.commit()
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not add category to the database. Error: {e}")
            return False #added bools for testing
        return True
    

    def set_transaction_category(transaction_list: TransactionList, id: str, type: str, category_name: str):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            update_income_query = ("UPDATE income SET category_name = %s WHERE id = %s")
            
            update_expense_query = ("UPDATE expense SET category_name = %s WHERE id = %s")
            
            new_trans_data = (category_name, id)
            if type == "income":
                db_cursor.execute(update_income_query, new_trans_data)
            else:
                db_cursor.execute(update_expense_query, new_trans_data)
            db.commit()
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not set transaction category to the database. Error: {e}")
            return False #added bools for testing
        return True

    def set_entity_category(entity_portfolio: EntityPortfolio, id: str, type: str, category_name: str):
        MainUI.MainUI.utility_print(f"Type: {type}, ID: {id}, Category: {category_name}")
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            update_asset_query = ("UPDATE asset SET cat_name = %s WHERE id = %s")
            update_liability_query = ("UPDATE liability SET cat_name = %s WHERE id = %s")

            MainUI.MainUI.utility_print(f"Type: {type}, ID: {id}, Category: {category_name}")
            
            new_trans_data = (category_name, id)
            if type == "asset":
                db_cursor.execute(update_asset_query, new_trans_data)
            else:
                db_cursor.execute(update_liability_query, new_trans_data)
            db.commit()
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not set transaction category to the database. Error: {e}")
            return False #added bools for testing
        return True

    def pull_categories_from_db(cat_list: CategoryList):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            db_cursor.execute("SELECT * FROM category")
            categories = db_cursor.fetchall()
            for row in categories:
                name = row[0]
                desc = row[1]
                income_count = row[2]
                expense_count = row[3]
                asset_count = row[4]
                liability_count = row[5]
                temp_cat = Category.Category(name, desc)
                temp_cat.set_income(income_count)
                temp_cat.set_expense(expense_count)
                temp_cat.set_asset(asset_count)
                temp_cat.set_liability(liability_count)
                cat_list.add_category(temp_cat)

            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not add category to the database. Error: {e}")
            return False #added bools for testing
        return True
    
    def update_category_counts(cat_name: str, income_count: int, type: str):
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor() #cursor() acts as an interace between AdvFi and the database
            update_income_query = ("UPDATE category SET income_count = %s WHERE cat_name = %s")
            update_expense_query = ("UPDATE category SET expense_count = %s WHERE cat_name = %s")
            update_asset_query = ("UPDATE category SET asset_count = %s WHERE cat_name = %s")
            update_liability_query = ("UPDATE category SET liability_count = %s WHERE cat_name = %s")
            
            new_trans_data = (income_count, cat_name)
            if type == "income":
                db_cursor.execute(update_income_query, new_trans_data)
            elif type == "expense":
                db_cursor.execute(update_expense_query, new_trans_data)
            elif type == "asset":
                db_cursor.execute(update_asset_query, new_trans_data)
            else: #type == "liability"
                db_cursor.execute(update_liability_query, new_trans_data)
            db.commit()
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not set transaction category to the database. Error: {e}")
            return False #added bools for testing
        return True
    




    #REPORT METHODS!!!!
    def add_report(report_date: str, total_income: float, total_income_last_month: float, income_entries: list):
        """
        Adds a new income report and its entries to the database.

        :param report_date: Date of the report (format: 'YYYY-MM-DD').
        :param total_income: Total lifetime income.
        :param total_income_last_month: Total income for the last month.
        :param income_entries: A list of dictionaries, each containing:
                            - income_date (str): Date of the income transaction.
                            - amount (float): Income amount.
                            - description (str): Description of the income entry.
        :return: True if the operation is successful, False otherwise.
        """
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor()

            # Add report to income_report table
            add_report_query = ("INSERT INTO income_report (report_date, total_income, total_income_last_month) "
                                "VALUES (%s, %s, %s)")
            report_data = (report_date, total_income, total_income_last_month)
            db_cursor.execute(add_report_query, report_data)

            # Get the last inserted report ID
            report_id = db_cursor.lastrowid

            # Add income entries to income_entry table
            add_entry_query = ("INSERT INTO income_entry (report_id, income_date, amount, description) "
                            "VALUES (%s, %s, %s, %s)")
            for entry in income_entries:
                entry_data = (report_id, entry['income_date'], entry['amount'], entry['description'])
                db_cursor.execute(add_entry_query, entry_data)

            # Commit changes
            db.commit()
            db_cursor.close()
            db.close()
        except Exception as e:
            print(f"Could not add report to the database. Error: {e}")
            return False
        return True

    def get_report(report_id: int):
        """
        Retrieves a report and its associated entries from the database.

        :param report_id: The ID of the report to retrieve.
        :return: A dictionary containing the report details and its entries, or None if the operation fails.
        """
        try:
            db = mysql.connector.connect(user='advfi_user', password='advfi_password', host='localhost', database='advfi_database')
            db_cursor = db.cursor(dictionary=True)  # Use dictionary cursor for better readability

            # Fetch report details
            get_report_query = "SELECT * FROM income_report WHERE report_id = %s"
            db_cursor.execute(get_report_query, (report_id,))
            report = db_cursor.fetchone()

            if not report:
                print(f"Report with ID {report_id} not found.")
                return None

            # Fetch associated income entries
            get_entries_query = "SELECT * FROM income_entry WHERE report_id = %s"
            db_cursor.execute(get_entries_query, (report_id,))
            entries = db_cursor.fetchall()

            db_cursor.close()
            db.close()

            # Combine report and entries into a single dictionary
            report['income_entries'] = entries
            return report
        except Exception as e:
            print(f"Could not retrieve report from the database. Error: {e}")
            return None
