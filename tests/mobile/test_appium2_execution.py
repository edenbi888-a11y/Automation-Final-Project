
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
        #תשובה המשופרת: "השתמשתי בלוקטור בטסט כי זהו אלמנט שנוצר בזמן ריצה (Runtime) ולא אלמנט סטטי של הדף
        # , אך דאגתי לרכז את הלוגיקה ב-Flows כדי לשמור על סדר."
     #"meals", הטקסט "meals" הוא לא חלק קבוע מהאפליקציה (כמו כפתור "שמור"), אלא נתון שאת יצרת הרגע.
        #מוודא שההוצאה אכן מופיעה במסך לאחר ההוספה.
       #(assert):האלמנט עם הטקסט "meals" מוצג על המסך
       # Santiy_ test – בדיקה בסיסית שהמערכת עובדת, שהוספת הוצאה עובדת.
      
    def test02_positive_full_flow(self,atid_expense_appium_flows: AtidExpenseAppiumFlows):
        atid_expense_appium_flows.add_expenses("train ticket", "100", "20", "Transportation")
        MobileVerifications.visible(self.driver, (By.XPATH, "//*[@text='train ticket']"))
    #מה הוא בדק: זרימה מלאה עם נתונים שונים (ערכי קצה/שונים). הוא מוודא שהמערכת יודעת להתמודד עם קטגוריות שונות (כמו Transportation) ותאריכים שונים.
    #בדיקה שהטקסט "bus ticket, כאן גם בודקים השדה מקבל כמה מילים  ולא מילה אחת 
    #מוודא שהטקסט עם שם ההוצאה מופיע (למעשה בקוד יש bus ticket assert

    def test03_ui_keyboard_interference(self,atid_expense_appium_flows: AtidExpenseAppiumFlows):
        atid_expense_appium_flows.add_expenses("book", "200", "25", "Education")
        MobileVerifications.visible(self.driver, (By.XPATH, "//*[@text='book']"))   
    #מה הוא בדק: יציבות ממשק משתמש,במובייל, כשמקלדת נפתחת, יכולה  להסתיר כפתורים ה
    # הוידואי כאן הוא אימות שההוצאה נוספה אם הכפתור  הוספה  היה נסתר אז לא היתה אפשרות להוספה
     #האלמנט עם שם ההוצאה "tutor" מופיע במסך.assert
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
        
      #שולח את האפליקציה לרקע (background) ומחזיר אותה לפוקוס
      #מוודא שהנתונים נשמרו וההוצאה "travel" עדיין מופיעה.
      #האלמנט "travel" עדיין מוצג במסך.assert
     # Data Persistence– לוודא שהמערכת שומרת את 
     # הנתונים גם אם האפליקציה יוצאת מהרקע או שהמשתמש מקבל שיחה וכו’.
    def test05_delete_expense(self, atid_expense_appium_flows: AtidExpenseAppiumFlows):
        expense_name = "Pizza"
        
        # 1. הוספה (Flow)
        atid_expense_appium_flows.add_expenses(expense_name, "50", "1", "Food")
        
        # 2. מחיקה (Flow)
        atid_expense_appium_flows.delete_expense_flow(expense_name)
        
        # 3. אימות מחיקה (Verify החדש שלך)
        MobileVerifications.verify_deleted(self.driver, expense_name)