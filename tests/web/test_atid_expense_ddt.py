from typing import Any

import allure
from utils.ai_utils import AIUtils  
import pytest
from data.web.atid_expense_data import *
from extensions.web_verifications import WebVerify
from page_objects.web.atid_expense_page import AtidExpensePage
from utils.common_ops import read_data_from_csv
from workflows.web.atid_expense_flows import AtidExpenseFlows

EXPENSE_DATA_PATH = r"data/ddt/atid_expense_data.csv"

class TestAtidExpenseDDT:

    @allure.title("Test05: verify Expense Tracker DDT Validation")
    @allure.description("This test verify Expense Tracker name=space,empty field and long name values with DDT")
    @pytest.mark.parametrize("expense_data", read_data_from_csv(EXPENSE_DATA_PATH))
    def test05_expense_boundry_ddt(self, atid_expense_flows: AtidExpenseFlows, expense_data: Any):
        result = atid_expense_flows.add_expense_ddt(expense_data)
        WebVerify.verify_expense_ddt_result(result, expense_data)
       