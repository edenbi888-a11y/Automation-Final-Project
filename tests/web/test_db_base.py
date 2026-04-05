
import allure
import pytest
from data.web.atid_expense_data import EXPECTED_SUM
from extensions.db_actions import DBActions
from extensions.db_verifications import DbVerifications


class TestDBAtidExpenses:

    @allure.title("Test 01 - DB Sanity Check")
    def test01_verify_db(self, db: DBActions):
        atidexpenses = db.get_atidexpenses()
        DbVerifications.verify_db_not_empty(atidexpenses)
            #test02_ means here just check if the tests have connection with the data base.
            #means the  preformance is santiy test.
        

    def test02_total_expenses_sum(self, db: DBActions):
        db.clear_table("atidexpenses") # Clear everything to start with a "clean slate"
        db.insert_expense("tutor", 400, "11/3/26", "Education") 
        db.insert_expense("fishes", 200, "10/3/26", "food") 
        db.insert_expense("bus ticket", 100, "13/3/26", "Transportation") 
        actual_sum = db.get_total_sum_from_table("atidexpenses")
        DbVerifications.verify_total_sum(actual_sum, EXPECTED_SUM)
            #End-to-end DB validation 
            # Clears the DB → clean start
            # Inserts known data
            # Calculates the total
            # Compares to the expected result — this is a very strong test

    def test03_non_existent_expense(self, db: DBActions):
        result = db.get_expense_by_name("NotReal")
        DbVerifications.verify_record_not_found(result)
            # What happens when searching for data that does not exist
            # Does not "invent" data
        
    def test04_table_schema(self, db: DBActions):
        actual_columns = db.get_table_columns("atidexpenses")
        expected_columns = ["expense name", "amount", "date", "category"]
      # 2. Assertion – a clean comparison in the verification
        DbVerifications.verify_schema(actual_columns, expected_columns)

        