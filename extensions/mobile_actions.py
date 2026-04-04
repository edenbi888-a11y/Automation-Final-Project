
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MobileActions:
    @staticmethod
    @allure.step("Mobile: Update text in element to: '{value}'")
    def update_text(driver, locator, value: str) -> None:
        wait = WebDriverWait(driver, 10)
        # שימוש בכוכבית כדי לפרק את ה-tuple של (By.XPATH, "...")
        el = wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    @staticmethod
    @allure.step("Mobile: Click on element")
    def click(driver, locator) -> None:
        wait = WebDriverWait(driver, 10)
        el = wait.until(EC.element_to_be_clickable(locator))
        el.click()

    