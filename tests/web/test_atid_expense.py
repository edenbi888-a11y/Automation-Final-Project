
from unittest import result

import pytest
import allure
from playwright.sync_api import Playwright
from data.web.atid_expense_data import *
from extensions.web_verifications import WebVerify
from tests.web.test_atid_expense_ddt import EXPENSE_DATA_PATH
from utils.common_ops import read_data_from_csv
from workflows.web.atid_expense_flows import AtidExpenseFlows
from extensions.web_verifications import WebVerify 
from google import genai
from google.genai import types
from PIL import Image
import io
from unittest.mock import patch





class TestAtidExpenseWeb:

    @allure.title("Test - Add Expense")
    @allure.description("This test verify adding an expense is successful")
    def test01_verifiy_add_expenses(self,atid_expense_flows:AtidExpenseFlows):
        atid_expense_flows.add_expense(EXPENSE_NAME,AMOUNT_DINNER, DATE, CATEGORY_FOOD )
        atid_expense_flows.select_option_date(DATE)
        atid_expense_flows.click_add_expense_btn()
        WebVerify.count(atid_expense_flows.expense_page.expense_list,1)
     
     #Verify that adding an expense works successfully
     #expected Expense is added successfully,Table contains 1 new record



    @allure.title("Test - Mandatory fields validation")
    @allure.description("This test verify that the mandatory fields validation is working properly")
    def test02_mandatory_validation(self, atid_expense_flows: AtidExpenseFlows):
        alert_message = atid_expense_flows.mandatory_validation_empty_fields()
        WebVerify.verify_alert_text(alert_message, EXPECTED_ERROR_MESSAGE)
      #Submit the form with empty required fields
      # Capture the alert message displayed by the application
      #expected System blocks submission, shows alert "Please enter all details for the expense."
      
        

    @allure.title("Test - Expense Name Spaces Input Validation")
    @allure.description("Verify that entering only spaces in the Expense Name field triggers an error alert and does not add the expense to the list")
    def test03_expense_name_Spaces_Input_validation(self, atid_expense_flows: AtidExpenseFlows) -> None:
        result = atid_expense_flows.validate_expense_name_Spaces_Input(
            EXPENSE_NAME_NOTHING,
            AMOUNT_FOOD,
            DATE_FOR_FOOD,
            CATEGORY_TRANSPORT
        )
        WebVerify.verify_expense_not_added(result,EXPECTED_MESSAGE_ALL_FIELDS)
        WebVerify.count(atid_expense_flows.expense_page.expense_list, result, INITIAL_COUNT) 
        # but the application did not trigger any alert.
        # Instead, it silently added the expense with an empty name (only spaces).
        # Assuming this is the first test attempting to add an expense,
        # the list should remain empty.
        # The test expected 0 expenses in the table, but found 1.


        
    @allure.title("Test - Amount Rejects Non-Numeric Input")
    @allure.description("Verify that entering non-numeric value in Amount field triggers an error and prevents adding expense")
    def test04_amount_field_not_numeric(self, atid_expense_flows: AtidExpenseFlows):

        result = atid_expense_flows.validate_amount_numeric_input(
           EXPENSE_NAME_SEPCIAL,
            INVALID_AMOUNT_SEPCIAL,
            DATE_FOR_SEPCIAL,
            CATEGORY_TRANSPORT_SEPCIAL
        )
        WebVerify.verify_invalid_amount(result,EXPECTED_MESSAGE_ALL_FIELDS)
        #here used press_seqnentially the functions that we created in the flows 
        # to fill the fields and click on the add button, 
        # and we got the result of the alert text that we expected to get, 
        # but we didn't get it because the system allowed us 
        # to add an expense with a non-numeric amount without showing any error message.
        #the test expected that the system will show an alert with the message "Please enter all details for the expense." when trying to add an expense with a non-numeric amount. However, the system did not show any alert and allowed the expense to be added with the invalid amount. This is a failure because the system should have prevented adding an expense with a non-numeric amount and should have provided feedback to the user about the error. The test failed due to a logical issue in the application, not due to a coding error in the test itself.
        #that we got and the test passed 
            
                
    @allure.title("Test 05 - Invalid Category")
    @allure.description("Verify that injecting a non-existent category triggers an alert and blocks the expense")
    def test05_no_category_selected(self, atid_expense_flows: AtidExpenseFlows):
        result = atid_expense_flows.flow_add_no_category(
            VALID_EXPENSE_NAME,
            VALID_AMOUNT,
            VALID_DATE
        )
       
        WebVerify.verify_invalid_category_result(result, EXPECTED_ERROR_MESSAGE_INVALID_CATEGORY)


        #Verify that using a non-existent category is blocked and shows an alert.





    @allure.title("Test 06 - Negative Amount (Bug Validation)")
    @allure.description("Verify that the system blocks adding an expense with negative amount")
    def test06_negative_amount(self, atid_expense_flows: AtidExpenseFlows):
        result = atid_expense_flows.add_expense_with_negative_amount(
            EXPENSE_NAME_DRINKS,
            NEGATIVE_AMOUNT,
           DATE_FOR_DRINKS,
            CATEGORY_1
        )
        WebVerify.verify_no_expense_added(result["final_count"], result["initial_count"])
    
       #Verify that the system blocks adding an expense with a negative amount
       #Checks that expense count did not increase remain the same.



               
    @allure.title("Test - Delete Expense")
    @allure.description("Verify that an expense can be successfully deleted from the list")
    def test07_delete_expense(self, atid_expense_flows: AtidExpenseFlows):
        initial_count = atid_expense_flows.expense_page.expense_list.count()
        atid_expense_flows.add_expense(EXPENSE_NAME_SNACKS, AMOUNT_SNACKS, DATE_FOR_SNACKS, CATEGORY_2)
        atid_expense_flows.select_option_date(DATE_FOR_SNACKS)
        atid_expense_flows.click_add_expense_btn()
        WebVerify.count(atid_expense_flows.expense_page.expense_list, initial_count + 1)
        atid_expense_flows.delete_expense(EXPENSE_NAME_SNACKS)
        WebVerify.count(atid_expense_flows.expense_page.expense_list, initial_count)


    #Expense is added successfully
    #Verify that expense count increased by 1
    #the expenses are deleted successfully
    #Table returns to original state =0 




    @allure.title("test 08 AI Vision - Expense Name Empty Validation")
    def test08_ai_expense_name_empty(self, atid_expense_flows: AtidExpenseFlows):

        with patch.object(atid_expense_flows, "call_gemini", return_value="messgae"):
            
            result = atid_expense_flows.verify_with_vision(
                EXPENSE_NAME_AI_TEST,
                AMOUNT_AI,
                DATE_FOR_AI,
                CATEGORY_AI
            )
            WebVerify.verify_no_expense_added(result, EXPECTED_ERROR_MESSAGE)   


        
    

       
    
     
