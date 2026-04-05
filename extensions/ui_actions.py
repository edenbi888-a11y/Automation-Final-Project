import allure
from playwright.sync_api import Locator, Page

from data.web.atid_expense_data import*
from utils.common_ops import load_config

CONFIG = load_config()
DEFAULT_TIMEOUT = CONFIG["DEFAULT_COMMAND_TIMEOUT"]


class UIActions:
  #website
    @staticmethod
    @allure.step("Navigte to")
    def navigate_to(page:Page,url:str):
        page.goto(url)

    @staticmethod
    @allure.step("Click on element")
    def click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.wait_for(state="attached", timeout=timeout)
        element.click(timeout=timeout)

    @staticmethod
    @allure.step("Force click on element (JS click)")
    def force_click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="attached", timeout=timeout)
        element.evaluate("el => el.click()")

    @staticmethod
    @allure.step("Get text from element")
    def get_text(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        element.wait_for(state="visible", timeout=timeout)

        tag_name = element.evaluate("el => el.tagName.toLowerCase()")

        if tag_name in ["input", "textarea"]:
            text = element.input_value(timeout=timeout)
        else:
            text = element.inner_text(timeout=timeout)

        return text.strip()

    @staticmethod
    @allure.step("Update text in element to: '{text}'")
    def update_text(element: Locator, text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.fill("")  # clear first (more stable)
        element.fill(text, timeout=timeout)

    @staticmethod   
    @allure.step("Select date '{date}' in date picker")
    def select_date(element: Locator, date: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.fill(date, timeout=timeout)
      


    @staticmethod
    @allure.step("Select option '{option_value}' from dropdown")
    def select_option(page: Page, locator: Locator, option_value: str): 
       
        page.select_option(locator, value=option_value)

    # @staticmethod
    # @allure.step("Mouse hover on element")
    # def mouse_hover(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
    #     element.wait_for(state="visible", timeout=timeout)
    #     element.hover(timeout=timeout)

    #test4
    @staticmethod
    @allure.step("Update text in element to: '{value}'")
    def update_text(element: Locator, value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
       #wait for element to be visible before interacting
        element.wait_for(state="visible", timeout=timeout)
        
    
        element.fill("")
        
       
        element.fill(value)

    @staticmethod
    @allure.step("Select option from dropdown")
    def select_option(element: Locator, value: str):
        element.select_option(label=value)
 

    @staticmethod
    @allure.step("Click on element")
    def click(element: Locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element.wait_for(state="visible", timeout=timeout)
        element.click()    
    

   #invalid category test06
    @staticmethod
    @allure.step("Update text in element: '{value}'")
    def update_text(element: Locator, value: str, timeout: int = DEFAULT_TIMEOUT):
        element.wait_for(state="visible", timeout=timeout)
        element.fill("")  # clear
        element.fill(value, timeout=timeout)

    @staticmethod
    @allure.step("Click on element")
    def click(element: Locator, timeout: int = DEFAULT_TIMEOUT):
        element.wait_for(state="visible", timeout=timeout)
        element.click(timeout=timeout)

    @staticmethod
    @allure.step("Select date '{date}' in date picker")
    def select_date(element: Locator, date: str, timeout: int = DEFAULT_TIMEOUT):
        element.wait_for(state="visible", timeout=timeout)
        element.fill(date, timeout=timeout)

    @staticmethod
    @allure.step("Select option '{option_value}' from dropdown")
    def select_option(element: Locator, option_value: str):
        element.select_option(label=option_value)
        
   
    @staticmethod
    @allure.step("Performing delete action on element")
    def click_delete(element):
        element.click()    

      
            
     


    

        