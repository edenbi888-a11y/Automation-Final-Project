


import allure

class DBActions:
    def __init__(self, connection):
        # כאן אנחנו שומרים רק את החיבור למסד הנתונים
        self.data_base = connection
    
    def close_db(self):
        self.data_base.close()

    def get_atidexpenses(self):
        """שליפת כל הרשומות מהטבלה"""
        query = "SELECT * FROM atidexpenses"
        my_cursor = self.data_base.cursor()
        my_cursor.execute(query)
        # תיקון: מחזירים את כל הרשימה (fetchall) ולא רק אינדקס ספציפי
        return my_cursor.fetchall()

    def get_total_sum_from_table(self, table_name):
        """מתודה חדשה: מחשבת סכום של עמודת amount מטבלה מסוימת"""
        query = f"SELECT SUM(CAST(amount AS REAL)) FROM {table_name}"
        cursor = self.data_base.cursor()
        cursor.execute(query)
        # שליפת הערך הראשון מהרשומה הראשונה
        result = cursor.fetchone()
        return result[0] if result else 0

    def get_table_columns(self, table_name):
        """שליפת שמות העמודות של טבלה"""
        cursor = self.data_base.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        # עיבוד הנתונים (הלולאה) קורה כאן כדי שהטסט יישאר נקי
        return [row[1] for row in cursor.fetchall()]
    
    def get_expense_by_name(self, name):
        """שליפת הוצאה לפי שם"""
        query = "SELECT * FROM atidexpenses WHERE \"expense name\" = ?"
        cursor = self.data_base.cursor()
        cursor.execute(query, (name,))
        return cursor.fetchone()
        
    def insert_expense(self, name, amount, date, category):
        """הוספת הוצאה חדשה לטבלה"""
        query = "INSERT INTO atidexpenses ('expense name', amount, date, category) VALUES (?, ?, ?, ?)"
        cursor = self.data_base.cursor()
        with allure.step(f"Inserting record: {name}, {amount}"):
            cursor.execute(query, (name, amount, date, category))
            self.data_base.commit() # חובה כדי שהנתונים יישמרו בקובץ atid.db

    def clear_table(self, table_name):
        """ניקוי כל הנתונים מהטבלה (מחיקת כל השורות)"""
        query = f"DELETE FROM {table_name}"
        cursor = self.data_base.cursor()
        with allure.step(f"Clearing all data from table: {table_name}"):
            cursor.execute(query)
            self.data_base.commit()