
class APIVerify:
    @staticmethod
    def status_code(response, expected_status_code: int):
        """
        Verifies that the API response status code matches the expected status code.
        """
        if isinstance(response, dict):  # If it's already JSON, we can't check status
            raise ValueError("Expected a Playwright response object, but got a dictionary. Ensure status code is checked before calling .json()")
        assert response.status == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {response.status}"
        

    @staticmethod
    def json_key_exists(response_data, key: str):
        """
        Verifies that a specific key exists in the JSON response.
        """
        assert key in response_data, f"Key '{key}' not found in the response JSON"

    
    @staticmethod
    def json_value_equals(response_data, key: str, expected_value):
        """
        Verifies that a specific key in the JSON response has the expected value.
        """
        assert response_data[key] == expected_value, (
            f"Expected value for key '{key}' is '{expected_value}', but got '{response_data[key]}'"
        )

    @staticmethod
    def verify_equals(response_data, expected_value):
        """
        Verifies that a specific key in the JSON response has the expected value.
        """
        assert response_data == expected_value, (
            f"Expected value is '{expected_value}', but got '{response_data}'"
        )
    
    @staticmethod
    def json_contains(response_data, expected_data: dict):
        """
        Verifies that the JSON response contains the expected data.
        """
        for key, value in expected_data.items():
            assert key in response_data, f"Key '{key}' not found in the response JSON"
            assert response_data[key] == value, (
                f"Expected value for key '{key}' is '{value}', but got '{response_data[key]}'"
            )

    # Soft Assertions
    @staticmethod
    def soft_assert_status_code(response, expected_status_code: int):
        """
        Soft asserts that the API response status code matches the expected status code.
        """
        if isinstance(response, dict):  
            APIVerify.errors.append("Expected a Playwright response object, got a dictionary.")

        elif response.status != expected_status_code:
            APIVerify.errors.append(
                f"Expected status code {expected_status_code}, but got {response.status}."
            )

    @staticmethod
    def assert_all():
        """
        Raises all collected assertion errors at once.
        """
        if APIVerify.errors:
            error_message = "\n".join(APIVerify.errors)
            APIVerify.errors.clear()  # Clear errors after raising
            raise AssertionError(f"Soft assertion failures:\n{error_message}")
        
    @staticmethod
    def list_contains_all(actual_list: list, expected_list: list):
        """ וולידציה שכל האיברים ברשימה המצופה קיימים ברשימה שחזרה """
        for item in expected_list:
            assert item in actual_list, f"Item '{item}' was expected but not found in the response list."
      #test 07 the url have to strings e.g "https:"
    @staticmethod
    def string_contains(actual_string: str, expected_substring: str):
        """ וולידציה שסטרינג מכיל תת-סטרינג (מתאים ל-Headers ו-URLs) """
        assert expected_substring in actual_string, \
            f"Expected '{expected_substring}' to be in '{actual_string}'"

    @staticmethod
    def instance_of(value, expected_type):
        """ וולידציה שסוג הנתון תקין (למשל שה-ID הוא מחרוזת) """
        assert isinstance(value, expected_type), \
            f"Expected type {expected_type}, but got {type(value)}"
        
        #for test 09 performance
    @staticmethod
    def is_less_than(actual_value: float, threshold: float, unit: str = "s"):
        """ וולידציה שהערך קטן מסף מסוים (מתאים לזמן תגובה) """
        assert actual_value < threshold, \
            f"Value too high: {actual_value}{unit} (Limit: {threshold}{unit})"   
        #test 11
    @staticmethod
    def verify_error_status(response, expected_error_code: int):
        """
        מוודא שהשרת אכן מחזיר שגיאה כשמנסים לבצע פעולה אסורה
        """
        assert response.status == expected_error_code, \
            f"Expected error {expected_error_code}, but got {response.status}. Server might be vulnerable!"   
    


   #test3
    @staticmethod
    def verify_search_results(data, query, should_have_results):
        assert "total" in data, f"'total' field missing in response for {query}"
        assert isinstance(data["total"], int), f"'total' is not int for {query}"

        if should_have_results:
            assert data["total"] > 0, f"{query} should return results but got 0"
        else:
            assert data["total"] == 0, f"{query} should return 0 results but got {data['total']}"