import logging
from typing import Any
from playwright.sync_api import (
    Page,
)  # Assuming you're using Playwright for page interactions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestPlanManagementPage:
    def __init__(self, page: Page):
        self.page = page
        logger.info("Initialized ReleaseManagementPage with page: %s", page)
        page.get_by_role("link", name=" Test Plan Management ").click()

    def create_testplan(self, tp_name: str, release: str, program: str, feature: str):
        self.page.get_by_role("link", name="Create Test Plan").click()
        logger.info("Adding Testplan name : %s", tp_name)
        self.page.get_by_role("link", name="Create Test Plan").click()
        self.page.get_by_placeholder("Enter Test Plan Name").click()
        self.page.get_by_placeholder("Enter Test Plan Name").fill(tp_name)
        self.page.locator("#tc_release").select_option(release)
        self.page.locator("#tc_program").select_option(program)
        self.page.locator("#tc_feature").select_option(feature)

        self.page.locator("#select-all").check()
        self.page.get_by_role("button", name="Create").click()

    def view_testplan(self, release: str, program: str, feature: str):
        self.page.get_by_role("link", name="View Test Plan").click()
        logger.info("Clicked on Add Feature link")
        self.page.locator("#tc_release").select_option(release)
        self.page.locator("#tc_program").select_option(program)
        self.page.locator("#tc_feature").select_option(feature)

        with self.page.expect_popup() as page1_info:
            self.page.get_by_role("link", name="").click()
            import time

            time.sleep(4)
        page1 = page1_info.value
        page1.close()
        # self.page.close()
