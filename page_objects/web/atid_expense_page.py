from playwright.sync_api import Page
class AtidExpensePage:
    def __init__(self,page:Page):
        
        self.expense_name_field  = page.locator("[id='expense-name']")
        self.amount_field       = page.locator("[id='expense-amount']")
        self.date_field        = page.locator("[id='expense-date']")
        self.category_selector  = "[id='expense-category']"
        self.category_selector  = page.locator("[id='expense-category']")
        self.add_expense_button = page.locator("[id='add-expense']")
        self.expense_list      = page.locator("//ul[@id = 'expense-list']/li")
        self.delete_btn =page.locator("//ul[@id='expense-list']/li//button[text()='Delete']")
        

   
    