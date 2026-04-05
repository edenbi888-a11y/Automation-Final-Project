

import sqlite3

import pytest
import allure
from pytest import FixtureRequest
from playwright.sync_api import APIRequestContext, Page, Playwright
from data.web.atid_expense_data import *
from utils.fixture_helpers import* 
from extensions.db_actions import DBActions
from utils.common_ops import load_config
from utils.fixture_helpers import get_browser
from workflows.api.chuck_norris_flows import ChuckNorrisFlows
from workflows.mobile.atid_expense_appium_flows import AtidExpenseAppiumFlows
from workflows.web.atid_expense_flows import AtidExpenseFlows
from appium import webdriver
from data.api.chuck_norris_data import CHUCK_BASE_URL
# Load the configuration
CONFIG = load_config()     

@pytest.fixture(scope="class")
def page(playwright: Playwright, request:FixtureRequest):
    browser = get_browser(playwright,CONFIG["BROWSER_TYPE"].lower())
    context = browser.new_context(no_viewport=True)   
    context.tracing.start(screenshots=True, snapshots=True, sources=True) # Start tracing for this context.     
    page = context.new_page()
    page.goto(EXPENSE_URL)
    yield page    
    # Best practice: Close page before context
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope= "class")
def request_context(playwright: Playwright, request:FixtureRequest):
    request_context=playwright.request.new_context(base_url= CHUCK_BASE_URL)
    yield request_context
    request_context.dispose()


@pytest.fixture
def chuck_norris_flows(request_context):
    return   ChuckNorrisFlows(request_context)



    
@pytest.fixture(scope="class",autouse=True)
def db(request:FixtureRequest):
        data_base = sqlite3.connect(CONFIG["DB_PATH"])
        db_actions =DBActions(data_base)
        yield  db_actions
        db_actions.close_db()


# conftest.py

@pytest.fixture(scope="class")
def driver_setup(request):
    dc = {
        'udid': 'RZCY10TYKBT',
        'appPackage': 'com.atidcollege.atidexpensetracker',
        'appActivity': '.MainActivity',
        'platformName': 'android',
        'noReset': True  
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)
    driver.implicitly_wait(10)
    
   
    if request.cls is not None:
        request.cls.driver = driver
    
    yield driver
    driver.quit()

@pytest.fixture
def atid_expense_appium_flows(driver_setup):
    return AtidExpenseAppiumFlows(driver_setup)   



@pytest.fixture
def atid_expense_flows(page: Page):
    return AtidExpenseFlows(page)


#Listen to console messages
def handle_console_message(msg):
    if msg.type == "error":
        print(f"Error detected in console: {msg.text}")
    if "the server responded with a status of 404" in msg.text:
        raise AssertionError(f"Test Failed: 404 Error Detected in Console - {msg.text}")


        
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page: Page = item.funcargs.get("page")

        if page:
            # Screenshot
            allure.attach(
                page.screenshot(full_page=True),
                name="web_screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

            #  TRACE
            trace_path = f"trace_{item.name}.zip"

            page.context.tracing.stop(path=trace_path)

            allure.attach.file(
                trace_path,
                name=f"Trace: {item.name}",
                attachment_type=allure.attachment_type.ZIP
            )

        # Mobile (Appium)
        driver = item.funcargs.get("driver_setup")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="mobile_screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )        
 



    
      




   
