
from selenium.webdriver.common.by import By

class AtidExpensAppiumePage:

    def __init__(self, driver):
        self.driver = driver  
        
        # לוקטורים
        self.name_field = (By.XPATH, "//*[@resource-id='expense-name']") # שיפור: resource-id נפוץ יותר במובייל
        self.amount_field = (By.XPATH, "//*[@resource-id='expense-amount']")
        self.date_field = (By.XPATH, "//*[@resource-id='expense-date']")
        self.category_selector = (By.XPATH, "//*[@text='Select Category']")
        self.add_button = (By.XPATH, "//*[@text='Add Expense']")
        self.ok_button = (By.XPATH, "//*[@resource-id='android:id/button1']")
        self.delete_btn_base = (By.XPATH, "//*[@text='Delete']")


    def click_delete_by_name(self, name):
        dynamic_xpath = f"//*[contains(@text, '{name}')]/..//*[@text='Delete']"
        self.driver.find_element(By.XPATH, dynamic_xpath).click()    
        #אם מחר המפתח ישנה את המבנה (למשל, כפתור המחיקה כבר לא יהיה תחת אותו "אבא"), את תצטרכי לתקן את זה רק במקום אחד – ב-Page Object.
        #כדי לשמור על encapsulation (כמיסה). ה-Flow לא צריך להכיר את ה-DOM או את ה-XPath, הוא רק צריך לדעת להפעיל שירותים שה-Page Object מספק."