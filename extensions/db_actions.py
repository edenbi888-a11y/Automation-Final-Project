


import allure

class DBActions:
    def __init__(self, connection):
       
        self.data_base = connection
    
    def close_db(self):
        self.data_base.close()

    def get_atidexpenses(self):
       
        query = "SELECT * FROM atidexpenses"
        my_cursor = self.data_base.cursor()
        my_cursor.execute(query)
        
        return my_cursor.fetchall()

    def get_total_sum_from_table(self, table_name):
        
        query = f"SELECT SUM(CAST(amount AS REAL)) FROM {table_name}"
        cursor = self.data_base.cursor()
        cursor.execute(query)
        
        result = cursor.fetchone()
        return result[0] if result else 0

    def get_table_columns(self, table_name):
      
        cursor = self.data_base.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
      
        return [row[1] for row in cursor.fetchall()]
    
    def get_expense_by_name(self, name):
     
        query = "SELECT * FROM atidexpenses WHERE \"expense name\" = ?"
        cursor = self.data_base.cursor()
        cursor.execute(query, (name,))
        return cursor.fetchone()
        
    def insert_expense(self, name, amount, date, category):
        
        query = "INSERT INTO atidexpenses ('expense name', amount, date, category) VALUES (?, ?, ?, ?)"
        cursor = self.data_base.cursor()
        with allure.step(f"Inserting record: {name}, {amount}"):
            cursor.execute(query, (name, amount, date, category))
            self.data_base.commit() 

    def clear_table(self, table_name):
        
        query = f"DELETE FROM {table_name}"
        cursor = self.data_base.cursor()
        with allure.step(f"Clearing all data from table: {table_name}"):
            cursor.execute(query)
            self.data_base.commit()