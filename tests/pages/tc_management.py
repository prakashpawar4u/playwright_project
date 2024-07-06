from .base_page import BasePage
import logging

logger = logging.getLogger("app")


class TestCaseManagementPage(BasePage):
    def add_test_case(self, test_case_name: str, detailed_plan: str):
        self.page.fill("#test-case-name-input", test_case_name)
        self.page.fill("#detailed-plan-input", detailed_plan)
        self.page.click("#add-test-case-button")

    # Other methods for interacting with the Test Case Management page
