import allure

class DbVerifications:
    
    @staticmethod
    @allure.step("Verify database is not empty")
    def verify_db_not_empty(data_list):
        assert len(data_list) > 0, "Database is empty! No records found."
        print(f"[INFO] Sanity passed: Found {len(data_list)} records.")

    @staticmethod
    @allure.step("Verify total expenses sum is {expected_sum}")
    def verify_total_sum(actual_sum, expected_sum):
        
        print(f"\n[CHECK] Expected Sum: {expected_sum}")
        
        assert float(actual_sum) == expected_sum, \
            f"Assertion Failed! Expected: {expected_sum}, but found: {actual_sum}"
        
      
        print(f"SUCCESS: The sums match!")
            

    @staticmethod
    @allure.step("Verify record is None (Not Found)")
    def verify_record_not_found(result):
        assert result is None, f"Error: Found unexpected data in DB: {result}"



    @staticmethod
    @allure.step("Verify table schema matches expected columns")
    def verify_schema(actual_columns, expected_columns):
        assert actual_columns == expected_columns, \
            f"Schema mismatch! Expected: {expected_columns}, Actual: {actual_columns}"