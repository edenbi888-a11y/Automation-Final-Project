
import time

import allure
import pytest
from extensions.mobile_verifications import MobileVerifications
from workflows.mobile.atid_expense_appium_flows import AtidExpenseAppiumFlows
from page_objects.mobile.atid_expense_appium_page import AtidExpensAppiumePage
from appium import webdriver
from selenium.webdriver.common.by import By  
from extensions.mobile_actions import MobileActions


@pytest.mark.usefixtures("driver_setup")
class TestMobileExpense:
    
    @allure.title("Test 01 - Verify Expense Added")
    def test01_verify_execution(self,atid_expense_appium_flows: AtidExpenseAppiumFlows):
        atid_expense_appium_flows.add_expenses("meals", "100", "15", "Food")
        MobileVerifications.visible(self.driver, (By.XPATH, "//*[@text='meals']"))
        
            # Improved answer: "I used a locator in the test because this is an element created at runtime, not a static page element,
            # Ensures that the expense actually appears on the screen after being added.
            # (assert): The element with the text "meals" is displayed on the screen.
            # Sanity test – a basic check that the system works and that adding an expense functions properly.
            
    def test02_positive_full_flow(self,atid_expense_appium_flows: AtidExpenseAppiumFlows):
        atid_expense_appium_flows.add_expenses("train ticket", "100", "20", "Transportation")
        MobileVerifications.visible(self.driver, (By.XPATH, "//*[@text='train ticket']"))
        #  Full flow with different data (edge/varied values). He verifies that the system can handle different categories (such as Transportation) and different dates.
        # Validation that the text "bus ticket" is accepted — here we also check that the field supports multiple words, not just a single word.
        # Ensures that the expense name text appears (in the code, there is a "bus ticket" assert).

    def test03_ui_keyboard_interference(self,atid_expense_appium_flows: AtidExpenseAppiumFlows):
        atid_expense_appium_flows.add_expenses("book", "200", "25", "Education")
        MobileVerifications.visible(self.driver, (By.XPATH, "//*[@text='book']"))   
        #  UI stability on mobile — when the keyboard opens, it may hide buttons.
        # The verification here is to confirm that the expense was added; if the "Add" button was hidden, it wouldn’t have been possible to add it.
        # The element with the expense name "tutor" appears on the screen. assert
    @allure.title("Test 04 - Expense Persistence")
    @allure.title("Test 04 - Expense Persistence")
    def test04_persistence(self, atid_expense_appium_flows: AtidExpenseAppiumFlows):
        atid_expense_appium_flows.add_expenses("travel", "200", "10", "Accommodation")

        # Send to background
        atid_expense_appium_flows.send_app_to_background()

        # Give the app a moment to settle after coming back
        
        time.sleep(2) 

        expense_locator = (By.XPATH, "//*[@text='travel']")
        
        # Use your verification
        MobileVerifications.visible(self.driver, expense_locator)
     
    def test05_delete_expense(self, atid_expense_appium_flows: AtidExpenseAppiumFlows):
        expense_name = "Pizza"
        atid_expense_appium_flows.add_expenses(expense_name, "50", "1", "Food")
        
        atid_expense_appium_flows.delete_expense_flow(expense_name)
        MobileVerifications.verify_deleted(self.driver, expense_name)