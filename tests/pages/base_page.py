from playwright.sync_api import Page
import logging

logger = logging.getLogger("app")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
