import pytest

# import logging
# import logging.config
# from dotenv import load_dotenv
# import os

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def new_page(playwright_browser):
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    context.close()
