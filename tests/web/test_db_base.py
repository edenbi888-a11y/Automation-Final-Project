
import allure
import pytest
from data.web.atid_expense_data import EXPECTED_SUM
from extensions.db_actions import DBActions
from extensions.db_verifications import DbVerifications


class TestDBAtidExpenses:

    @allure.title("Test 01 - DB Sanity Check")
    def test01_verify_db(self, db: DBActions):
        # Action - שליפת כל הנתונים דרך ה-Action שכבר בנית
        atidexpenses = db.get_atidexpenses()
        # Assertion - שימוש במחלקת הווריפיקציות
        DbVerifications.verify_db_not_empty(atidexpenses)
            #test02_ means here just check if the tests have connection with the data base.
        #means the  preformance is santiy test.
        #כל שאר הטסטים לא רלוונטיים


    def test02_total_expenses_sum(self, db: DBActions):
        # --- שלב ה-Setup: הכנת הנתונים ---
        db.clear_table("atidexpenses") # מנקים הכל כדי להתחיל "דף חלק"
        db.insert_expense("tutor", 400, "11/3/26", "Education") 
        db.insert_expense("fishes", 200, "10/3/26", "food") 
        db.insert_expense("bus ticket", 100, "13/3/26", "Transportation") 
        actual_sum = db.get_total_sum_from_table("atidexpenses")
        DbVerifications.verify_total_sum(actual_sum, EXPECTED_SUM)
        #End-to-end DB validation 
        #מנקה DB → התחלה נקייה
        #מכניס נתונים ידועים
        #מחשב סכום
        #משווה לתוצאה צפויה,זה טסט חזק מאוד
    def test03_non_existent_expense(self, db: DBActions):
        result = db.get_expense_by_name("NotReal")
        DbVerifications.verify_record_not_found(result)
        #מה קורה כשמחפשים נתון שלא קיים
        #לא "ממציאה" נתונים
        
    def test04_table_schema(self, db: DBActions):
    # 1. Action - מקבלים רשימת שמות נקייה מה-Action
        actual_columns = db.get_table_columns("atidexpenses")
        expected_columns = ["expense name", "amount", "date", "category"]

        # 2. Assertion - השוואה נקייה ב-Verification
        DbVerifications.verify_schema(actual_columns, expected_columns)

        