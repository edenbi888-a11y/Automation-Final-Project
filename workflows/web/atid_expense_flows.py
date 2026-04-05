
from tkinter import dialog
from unittest import result
import allure
from playwright.sync_api import Page
import pytest
from data.web.atid_expense_data import *
from extensions.ui_actions import UIActions
from page_objects.web.atid_expense_page import AtidExpensePage
from google import genai
from google.genai import types
from PIL import Image
import io



class AtidExpenseFlows:

    def __init__(self,page:Page):
        self.page = page
        self.expense_page = AtidExpensePage(page)
        self.last_alert_text = ""  
        self.client = genai.Client(api_key=GEMENI_API_KEY)
        
        
    @allure.step("Add expense")
    def add_expense(self,expense_name:str,amount:str,date:str,category:str) -> None:
        UIActions.update_text(self.expense_page.expense_name_field,expense_name)
        UIActions.update_text(self.expense_page.amount_field,amount)
        UIActions.select_option(self.expense_page.category_selector, category)

    def select_option_date(self,date:str)->None:
        UIActions.select_date(self.expense_page.date_field,date)


        
    def click_add_expense_btn(self)->None:
        UIActions.click(self.expense_page.add_expense_button)   


   #2
    @allure.step("Validate mandatory fields Alert")
    def mandatory_validation_empty_fields(self) -> str:
        dialog_text = {}

        def handle(dialog):
            dialog_text['message'] = dialog.message
            dialog.accept()

        self.page.once("dialog", handle)
        UIActions.click(self.expense_page.add_expense_button)
        return dialog_text['message']
    

    @allure.step("dialog handler to capture alert text")
    def dialog_hendler(self,dialog):
        self.last_alert_text = dialog.message
        dialog.accept()

   #3
    def validate_expense_name_Spaces_Input(self, name, amount, date, category):
        initial_count = self.expense_page.expense_list.count()

        UIActions.update_text(self.expense_page.expense_name_field, name)
        UIActions.update_text(self.expense_page.amount_field, amount)
        self.select_option_date(date)
        UIActions.select_option(self.expense_page.category_selector, category)

        UIActions.click(self.expense_page.add_expense_button)

       
        self.page.wait_for_timeout(500)

        return {
            "initial_count": initial_count,
            "final_count": self.expense_page.expense_list.count()
        }
        
    
        
           
     #4
    def _handle_dialog(self, dialog):
        self.last_alert_text = dialog.message
        dialog.accept()

    @allure.step("Validate Amount numeric input: {amount}")
    def validate_amount_numeric_input(self, name: str, amount: str, date: str, category: str) -> dict:
        initial_count = self.expense_page.expense_list.count()
        captured_data = {"alert_text": ""}
        def handle_dialog(dialog):
            captured_data["alert_text"] = dialog.message
            dialog.accept()
        self.page.once("dialog", handle_dialog)
        UIActions.update_text(self.expense_page.expense_name_field, name)
        self.expense_page.amount_field.clear()
        self.expense_page.amount_field.press_sequentially(amount)
        self.select_option_date(date)
        UIActions.select_option(self.expense_page.category_selector, category)
        UIActions.click(self.expense_page.add_expense_button)
        self.page.wait_for_timeout(500) 

        return {
            "initial_count": initial_count,
            "final_count": self.expense_page.expense_list.count(),
            "alert_text": captured_data["alert_text"]
        }


        #5
       
    @allure.step("Flow: Attempt to add expense without choosing category")
    def flow_add_no_category(self, expense_name, amount, date):
        initial_count = self.expense_page.expense_list.count()
        alert_data = {"message": ""}
        
        def handle_dialog(dialog):
            alert_data["message"] = dialog.message
            dialog.accept()
            
        self.page.once("dialog", handle_dialog)
        
        UIActions.update_text(self.expense_page.expense_name_field, expense_name)
        UIActions.update_text(self.expense_page.amount_field, amount)
        self.select_option_date(date)
        # UIActions.select_option(self.expense_page.category_selector, "") 
        UIActions.click(self.expense_page.add_expense_button)
        self.page.wait_for_timeout(500)
        
        return {
            "alert_text": alert_data["message"],
            "initial_count": initial_count,
            "final_count": self.expense_page.expense_list.count()
        }
        



            #test06 - negative amount
    @allure.step("Add expense with negative amount")
    def add_expense_with_negative_amount(self, expense_name: str, amount: str, date: str, category: str):

        initial_count = self.expense_page.expense_list.count()

        UIActions.update_text(self.expense_page.expense_name_field, expense_name)
        UIActions.update_text(self.expense_page.amount_field, amount)
        self.select_option_date(date)
        UIActions.select_option(self.expense_page.category_selector, category)
        UIActions.click(self.expense_page.add_expense_button)
        final_count = self.expense_page.expense_list.count()

        return {
            "initial_count": initial_count,
            "final_count": final_count
        }
    


    @allure.step("verifing long term name ,empty field and space")
    def add_expense_ddt(self, data: dict) -> dict:
        self.last_alert_text = ""

        def capture_dialog(dialog):
            self.last_alert_text = dialog.message
            dialog.accept()

        self.page.once("dialog", capture_dialog)

        initial_count = self.expense_page.expense_list.count()

        UIActions.update_text(self.expense_page.expense_name_field, data['expense_name'])
        UIActions.update_text(self.expense_page.amount_field, data['amount'])
        self.select_option_date(data['date'])
        UIActions.select_option(self.expense_page.category_selector, data['category'])
        UIActions.click(self.expense_page.add_expense_button)

        final_count = self.expense_page.expense_list.count()

        return {
            "initial_count": initial_count,
            "final_count": final_count,
            "alert_text": self.last_alert_text
        }   



        #invalid category
    @allure.step("Validate invalid category")
    def validate_invalid_category(self, expense_name, amount, date, invalid_category):

        alert_text = {}

        def handle(dialog):
            alert_text["message"] = dialog.message
            dialog.accept()

        self.page.once("dialog", handle)

        UIActions.update_text(self.expense_page.expense_name_field, expense_name)
        UIActions.update_text(self.expense_page.amount_field, amount)
        self.select_option_date(date)
        self.page.evaluate(
            f"document.querySelector('#expense-category').value = '{invalid_category}'"
        )

        UIActions.click(self.expense_page.add_expense_button)

        return alert_text.get("message", "")
    
    
    
     
      #deletion of expense-7    
    @allure.step("Delete expense: {name}")
    def delete_expense(self, name: str):
        delete_button = self.page.locator(f"//li[contains(., '{name}')]//button[text()='Delete']")
        UIActions.click(delete_button)
        self.page.wait_for_timeout(1000)

 


    @allure.step("verifing long term name ,empty field and space")
    def add_expense_ddt(self, data: dict) -> dict:
        self.last_alert_text = ""

        def capture_dialog(dialog):
            self.last_alert_text = dialog.message
            dialog.accept()

        self.page.once("dialog", capture_dialog)

        initial_count = self.expense_page.expense_list.count()

        UIActions.update_text(self.expense_page.expense_name_field, data['expense_name'])
        UIActions.update_text(self.expense_page.amount_field, data['amount'])
        self.select_option_date(data['date'])
        UIActions.select_option(self.expense_page.category_selector, data['category'])
        UIActions.click(self.expense_page.add_expense_button)

        final_count = self.expense_page.expense_list.count()

        return {
            "initial_count": initial_count,
            "final_count": final_count,
            "alert_text": self.last_alert_text
        }   

    #Code for image comparison with the expected image FOR AI test - 8 
    @allure.step("Verify expense details using Gemini Vision API")
    def verify_with_vision(self, expected_name: str, expected_amount: str, expected_date: str, expected_category: str)->str:
        alert_message = ""

        # 🔔 Handle alert BEFORE clicking
        def handle_dialog(dialog):
            nonlocal alert_message
            alert_message = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)

        #  Fill form
        UIActions.update_text(self.expense_page.expense_name_field, expected_name)
        UIActions.update_text(self.expense_page.amount_field, expected_amount)
        self.select_option_date(expected_date)
        UIActions.select_option(self.expense_page.category_selector, expected_category)

        #  Trigger action
        UIActions.click(self.expense_page.add_expense_button)

        # If alert appeared → invalid case → stop here
        if alert_message:
            print(f"Alert appeared: {alert_message}")
            return alert_message

        #Take screenshot only if no alert
        screenshot_bytes = self.page.screenshot(type='png')

        # Optimize image
        img = Image.open(io.BytesIO(screenshot_bytes)).convert('RGB')
        img.thumbnail((1024, 1024))

        optimized_bio = io.BytesIO()
        img.save(optimized_bio, format='JPEG', quality=80)
        optimized_bytes = optimized_bio.getvalue()

        # Build AI prompt
        prompt_text = f"""
        You are a strict UI testing assistant.

        Check the screenshot and determine:
        Is there a row in the expense table with EXACTLY these values:

        - Name: "{expected_name}"
        - Amount: "{expected_amount}"
        - Date: "{expected_date}"
        - Category: "{expected_category}"

        Rules:
        - Match must be exact
        - If  the atid expense result equals to the expected values in  return yes
        - If the atid expense result does not equal the expected values → return no

        Answer ONLY with:
        Yes
        or
        No
        """
        # Call Gemini (mocked in tests)
        return self.call_gemini(prompt_text, optimized_bytes)




       #CODE FOR CALLING GEMINI API -8
    def call_gemini(self, prompt_text, image_bytes):
        try:
           
            client = genai.Client(api_key=GEMENI_API_KEY)

            
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=[
                    prompt_text,
                    {"mime_type": "image/jpeg", "data": image_bytes}
                ]
            )

            result = response.text.strip().lower()
            print(f"\nGemini response from AI: {result}")
            return result

        except Exception as e:
            print(f"Gemini failed: {e}")
            return "false"

            

    @allure.step("Capture alert message and accept the dialog")
    def _store_alert(self, dialog):
        self.last_alert_text = dialog.message
        dialog.accept()



    @allure.step("Navigte to:")
    def navigate_to(self,url:str)->None:
        UIActions.navigate_to(self.page,url)


    # @allure.step("verifing long term name ,empty field and space")
    # def verify_long_expense_ddt(self, expense_data):
    #     """
    #     ממלא את טופס ההוצאות ומחזיר את טקסט ה-Alert.
    #     """
    #     # 1. איפוס ה-Alert הקודם
    #     self.last_alert_text = ""

    #     # 2. הזנת שם ההוצאה והסכום
    #     self.expense_page.expense_name_field.fill(expense_data['expense_name'])
    #     self.expense_page.amount_field.fill(str(expense_data['amount']))

    #     # 3. בחירת תאריך
    #     self.select_option_date(expense_data['date'])

    #     # 4. בחירת קטגוריה (פקודה ישירה ל-Dropdown)
    #     # וודאי שב-CSV הערכים הם: Food, Fashion, Entertainment, Transportation
    #     self.expense_page.category_selector.select_option(label=expense_data['category'])

    #     # 5. הגדרת המאזין ל-Alert
    #     self.page.once("dialog", lambda dialog: self._store_alert(dialog))

    #     # 6. לחיצה על הוספה
    #     self.click_add_expense_btn()

    #     # 7. המתנה קלה לסנכרון הדיאלוג
    #     self.page.wait_for_timeout(500)


    


    