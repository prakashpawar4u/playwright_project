import pytest
import logging
import logging.config
from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright
from tests.pages.login_page import LoginPage
from tests.pages.release_management import ReleaseManagementPage
from tests.pages.tc_management import TestCaseManagementPage
from tests.pages.tc_plan_management import TestPlanManagementPage


# Load environment variables from .env file
load_dotenv()

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("app")


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def release_management_page(page):
    return ReleaseManagementPage(page)


@pytest.fixture
def test_case_management_page(page):
    return TestCaseManagementPage(page)


@pytest.fixture
def test_plan_management_page(page):
    return TestPlanManagementPage(page)
