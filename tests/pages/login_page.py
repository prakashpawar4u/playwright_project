from .base_page import BasePage
import logging

logger = logging.getLogger("app")


class LoginPage(BasePage):
    def login(self, url: str, username: str, password: str):
        # logger.debug(f"Logging in with username: {username}")
        logger.debug(f"Navigating to login URL: {url}")
        # self.page.goto('http://192.168.56.114:8012/login/')

        self.page.goto(url)
        logger.debug(f"Logging in with username: {username}")
        self.page.get_by_placeholder("Username").click()
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()
        logger.debug("Login button clicked")

    def is_logged_in(self):
        # Check for an element that is present only when logged in
        logger.debug("Checking if user is logged in")
        return self.page.get_by_role("link", name="Features")
        # return self.page.is_visible("link", "Features")


# from playwright.sync_api import Playwright, sync_playwright, expect


# def test_login(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://192.168.56.114:8012/login/")
#     page.get_by_placeholder("Username").click()
#     page.get_by_placeholder("Username").fill("admin")
#     page.get_by_placeholder("Password").click()
#     page.get_by_placeholder("Password").fill("ortseam@2024")
#     page.get_by_role("button", name="Sign in").click()
#     page.get_by_role("link", name="Features").click()
#     page.close()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     test_login(playwright)
