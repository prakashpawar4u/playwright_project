from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class Navigation:
    def __init__(self, page):
        self.page = page

    def homepage(self, url, username, password):
        """Log into the application and land on the dashboard page."""
        logger.debug(f"Navigating to login URL: {url}")
        logger.debug(f"Logging in with USER_LOGIN: {username}")

        self.page.goto(url)
        self.page.locator("input[name='username']").fill(username)
        self.page.locator("input[name='password']").fill(password)
        self.page.get_by_role("button", name="Login").click()
        self.page.screenshot(path="login.png")
        logger.debug("Login button clicked")

    def is_logged_in(self):
        logger.debug("Checking if user is logged in")
        return self.page.get_by_role("link", name=" Dashboard").is_visible()

    def navigate_to_dashboard(self):
        """Navigate to the dashboard page directly."""
        self.page.get_by_role("link", name=" Dashboard").click()

    def navigate_to_topology(self):
        """Navigate to Topology page."""
        self.page.get_by_role("link", name=" Topology ").click()

    def navigate_to_release_management(self):
        """Navigate to Release Management page."""
        self.page.get_by_role("link", name=" Release Management ").click()

    # def navigate_to_add_features(self):
    #     """Navigate to Add Features page."""
    #     self.navigate_to_release_management()
    #     self.page.get_by_role("link", name="Add Feature").click()

    # def navigate_to_add_release(self):
    #     """Navigate to Add Release page."""
    #     self.navigate_to_release_management()
    #     self.page.get_by_role("link", name="Add Release").click()

    # def navigate_to_map_testplans(self):
    #     """Navigate to Map Test Plans page."""
    #     self.navigate_to_release_management()
    #     self.page.get_by_role("link", name="Map Testplans").click()

    def navigate_to_testcase_management(self):
        """Navigate to Test Case Management page."""
        self.page.get_by_role("link", name=" Testcase Management ").click()

    def navigate_to_testplan_management(self):
        """Navigate to Test Plan Management page."""
        self.page.get_by_role("link", name=" Test Plan Management ").click()

    # def navigate_to_add_testcase(self):
    #     """Navigate to Add Testcase page."""
    #     self.navigate_to_testcase_management()
    #     self.page.get_by_role("link", name="Add Testcase").click()

    def navigate_to_testcase_controller(self):
        """Navigate to Test Case Controller page."""
        self.navigate_to_testcase_management()
        self.page.get_by_role("link", name="Testcase Controller").click()
