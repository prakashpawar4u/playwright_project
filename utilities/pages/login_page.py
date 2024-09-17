# from .base_page import BasePage

from playwright.sync_api import Page

import logging

logger = logging.getLogger("app")


class LoginPage:
    def __init__(self, url, page: Page):
        self.page = page
        self.url = url

    def load(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        logger.debug(f"Navigating to login URL: {self.url}")
        logger.debug(f"Logging in with USER_LOGIN: {username}")
        self.page.get_by_placeholder("Username").click()
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        self.page.screenshot(path="login.png")
        logger.debug("Login button clicked")

    def is_logged_in(self):
        logger.debug("Checking if user is logged in")
        return self.page.get_by_role("link", name="Dashboard")
        # return self.page.is_visible("link", "Features")
