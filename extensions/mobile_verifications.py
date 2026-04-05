
import allure
from selenium.webdriver.common.by import By

class MobileVerifications:
    @staticmethod
    def is_displayed(name, driver):
        locator = (By.XPATH, f"//*[contains(@text, '{name}')]")
        assert driver.find_element(*locator).is_displayed(), f"Element with text {name} was not found!"
   

    @staticmethod
    def visible(driver, locator):
        assert driver.find_element(*locator).is_displayed(), \
            f"Element {locator} was not found!"   
    
    
    @staticmethod
    @allure.step("Verify expense added to table")
    def verify_expense_added(driver, name: str, amount: str):

        name_locator = (By.XPATH, f"//*[@text='{name}']")
        amount_locator = (By.XPATH, f"//*[@text='{amount}']")

        assert driver.find_element(*name_locator).is_displayed(), \
            f"Expense name '{name}' not found!"

        assert driver.find_element(*amount_locator).is_displayed(), \
            f"Expense amount '{amount}' not found!"     
        
    @staticmethod
    @allure.step("Verify expense was deleted")
    def verify_deleted(driver, name: str):
      
        locator = (By.XPATH, f"//*[contains(@text, '{name}')]")
        elements = driver.find_elements(*locator)
      
        assert len(elements) == 0, f"Failure: The expense '{name}' still exists in the list."