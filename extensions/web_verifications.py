from playwright.sync_api import Locator, expect
from smart_assertions import soft_assert, verify_expectations
import allure

class WebVerify:
  
    @staticmethod    
    @allure.step("Verify that the element has text")
    def text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element matches the expected text.
        """
        expect(element).to_have_text(expected_text)

    @staticmethod
    @allure.step("Verify String")
    def strings_are_equal(actual:str,expected:str,message=None):
        assert actual == expected,message


    @staticmethod
    @allure.step("Verify that the element is visible")
    def visible(element: Locator):
        """
        Verifies that the element is visible.
        """
        expect(element).to_be_visible()
    
    @staticmethod
    @allure.step("Verify that the element is not visible")
    def not_visible(element: Locator):
        """
        Verifies that the element is not visible.
        """
        expect(element).not_to_be_visible()
    
    @staticmethod
    @allure.step("Verifies that the number of elements matching the locator is equal to the expected count")
    def count(element: Locator, count: int):
        """
        Verifies that the number of elements matching the locator is equal to the expected count.
        """
        expect(element).to_have_count(count)

    @staticmethod
    @allure.step("Verify that the element contains the expected text")
    def contain_text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element contains the expected text.
        """
        expect(element).to_contain_text(expected_text)
    
    @staticmethod
    @allure.step("Verify that the element has the expected value")
    def value(element: Locator, expected_value: str):
        """
        Verifies that the value of the element matches the expected value.
        """
        expect(element).to_have_value(expected_value)


    # Soft Assertions    
    @staticmethod
    @allure.step("Soft assertion to check if the element has the expected text")
    def soft_text(element: Locator, expected_text: str, message: str):
        """
        Soft assertion to check if the element has the expected text.
        Test execution will continue even if this assertion fails.
        """
        actual_text = element.inner_text()
        soft_assert(actual_text == expected_text, message)

    @staticmethod
    @allure.step("Soft assertion to check if the element is visible")
    def soft_is_visible(element: Locator, message: str):
        """
        Soft assertion to check if the element is visible.
        Test execution will continue even if this assertion fails.
        """
        soft_assert(element.is_visible(), message)

    @staticmethod
    @allure.step("Raises all collected assertion errors at once")
    def soft_all():
        """Raises all collected assertion errors at once."""
        verify_expectations()



    @staticmethod
    @allure.step("{description}")
    def verify_alert_text(actual_text: str, expected_text: str, description: str = None):
        """
        Verify that the actual text matches (or contains) the expected text
        actual_text: הטקסט שנלקח מה-alert/dialog
        expected_text: הטקסט הצפוי
        description: תיאור בדיקה ל-Allure, ברירת מחדל = הטקסט הצפוי
        """
        if description is None:
            description = f"Verify alert text contains: '{expected_text}'"

        if expected_text not in actual_text:
            raise AssertionError(f"{description} failed: expected '{expected_text}', got '{actual_text}'")
        #invalid category web verification:
    @staticmethod
    @allure.step("Verify element has text '{expected_text}'")
    def text(element: Locator, expected_text: str):
        expect(element).to_have_text(expected_text)

    @staticmethod
    @allure.step("Verify number of elements equals {count}")
    def count(element: Locator, count: int):
        expect(element).to_have_count(count)

    @staticmethod
    @allure.step("Verify alert text contains '{expected_text}'")
    def verify_alert_text(actual_text: str, expected_text: str):
        if expected_text not in actual_text:
            raise AssertionError(f"Expected alert text to contain '{expected_text}', got '{actual_text}'")
            

          
          #test3 - expense name with spaces only verification  
    @staticmethod
    @allure.step("Verify expense was not added and optional alert message")
    def verify_expense_not_added(result: dict, expected_message: str = None):
    
        assert result["final_count"] == result["initial_count"], \
            f"BUG: Expense was added! Before: {result['initial_count']}, After: {result['final_count']}"

        if expected_message and "alert_text" in result:
            actual_alert = result["alert_text"]
            assert expected_message in actual_alert, \
                f"Wrong alert message! Expected: {expected_message}, Got: {actual_alert}"


        
    #test04 _nemric amount verification
    @staticmethod
    def verify_invalid_amount(result: dict, expected_msg: str):
        assert expected_msg in result["alert_text"], "Wrong alert message"
        assert result["final_count"] == result["initial_count"], "Row was added unexpectedly"  

        

      #test05 - invalid category verification
   
    @staticmethod
    def verify_invalid_category_result(result: dict, expected_message: str):
        assert expected_message in result["alert_text"], "Wrong alert message"
        assert result["final_count"] == result["initial_count"], \
            "BUG: Expense was added with invalid category!"




    #TEST06 - Negative Amount Verification
    @staticmethod
    @allure.step("Verify that no expense was added (Negative Test)")
    def verify_no_expense_added(actual_count, expected_count):
        assert actual_count == expected_count, f"BUG: Expense was added! Started with {expected_count}, now have {actual_count}"    
        

        
    #test07delete expense verification
    @staticmethod
    @allure.step("Verify expense name is deleted from the list")
    def expense_deleted(page, name: str):
        
        # זה מייצג את האלמנט שאנחנו מצפים שייעלם
        expense_row = page.locator(f"//li[contains(., '{name}')]")
        
        # עכשיו זה קריא יותר: "צפה ששורת ההוצאה תהיה בספירה 0"
        expect(expense_row).to_have_count(0)
        #to_have_count(0). זה הרבה יותר יציב מלחפש את האלמנט ולבדוק אם הוא קיים, כי Playwright

    @staticmethod
    def verify_expense_ddt_result(result: dict, data: dict):

        expected_status = data['expected_status']

        was_added = result["final_count"] > result["initial_count"]
        alert_text = result["alert_text"]
        alert_exists = "Please enter all details" in alert_text

        errors = []

        if expected_status == "failure":

            if was_added:
                errors.append("Row was added improperly")

            if not alert_exists:
                errors.append(f"Alert missing (Got: '{alert_text}')")


        else:
            if not was_added:
                errors.append("Expense was not added")
        if errors:
            error_message = "BUG FOUND:\n" + "\n".join(f"- {e}" for e in errors)

            allure.attach(
                body=error_message,
                name="Failure Details",
                attachment_type=allure.attachment_type.TEXT
            )

            assert False, error_message  

           #test08 - AI Vision verification
    @staticmethod
    def verify_no_expense_added(actual_message, expected_message):
        # actual_message is now the string returned by the flow
        # expected_message is your constant 'Please enter all details...'
        assert actual_message == expected_message, \
            f"Validation Failed! Expected: '{expected_message}', but got: '{actual_message}'"


       