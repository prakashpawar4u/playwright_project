import pytest
import allure
import logging
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from utilities.pages.navigation import Navigation
from dotenv import load_dotenv
from typing import Dict


def setup_logger():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Create a directory for the current date
    log_dir = os.path.join("Logs", current_date)
    os.makedirs(log_dir, exist_ok=True)

    # Generate a log file name with date and timestamp
    log_file = os.path.join(log_dir, datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log"))

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)',
        format="%(asctime)s - %(name)s -> %(lineno)d - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
    logger = logging.getLogger(__name__)
    return logger


# Initialize logger
logger = setup_logger()

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "utilities/.env"))


@pytest.fixture(scope="session")
def playwright_browser():
    """Launch the browser session."""
    logger.info("Launching browser session")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless to True in CI/CD
        # browser = p.chromium.launch(headless=False, slow_mo=200)
        yield browser
        logger.info("Closing browser session")
        browser.close()


@pytest.fixture(scope="session")
def login_credentials() -> Dict[str, str]:
    """Load login credentials from environment variables."""
    logger.info("Loading login credentials from environment variables")
    return {
        "url": os.getenv("LOGIN_URL"),
        "username": os.getenv("USER_LOGIN"),
        "password": os.getenv("PASSWORD"),
    }


@pytest.fixture(scope="session")
def logged_in_page(playwright_browser, login_credentials):
    """Log into the application before running the test cases."""
    logger.info("Logging into the application")
    context = playwright_browser.new_context()
    page = context.new_page()

    # Initialize the Navigation class
    navigation = Navigation(page)
    navigation.homepage(
        login_credentials["url"],
        login_credentials["username"],
        login_credentials["password"],
    )
    logger.info("Logged in and initialized Navigation class")

    # After login, return the page object for further use
    yield page
    logger.info("Closing context")
    context.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure Allure environment."""
    logger.info("Configuring Allure environment")
    if not hasattr(config, "workerinput"):
        # Only set environment variables if not running in a distributed mode
        with open("allure-results/environment.properties", "w") as f:
            f.write("Browser=Chromium\n")
            f.write("Headless=False\n")
            f.write("URL={}\n".format(os.getenv("LOGIN_URL")))
        logger.info("Allure environment configured")


### WORKING ONE
# import pytest
# import allure
# import logging
# from playwright.sync_api import sync_playwright
# from utilities.pages.navigation import Navigation
# from dotenv import load_dotenv
# import os
# from typing import Dict

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("test_log.log"),
#         logging.StreamHandler()
#     ]
# )
# logger = logging.getLogger(__name__)

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), 'utilities/.env'))

# @pytest.fixture(scope="session")
# def playwright_browser():
#     """Launch the browser session."""
#     logger.info("Launching browser session")
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # Set headless to True in CI/CD
#         yield browser
#         logger.info("Closing browser session")
#         browser.close()

# @pytest.fixture(scope='session')
# def login_credentials() -> Dict[str, str]:
#     """Load login credentials from environment variables."""
#     logger.info("Loading login credentials from environment variables")
#     return {
#         "url": os.getenv('LOGIN_URL'),
#         "username": os.getenv('USER_LOGIN'),
#         "password": os.getenv('PASSWORD')
#     }

# @pytest.fixture(scope='session')
# def logged_in_page(playwright_browser, login_credentials):
#     """Log into the application before running the test cases."""
#     logger.info("Logging into the application")
#     context = playwright_browser.new_context()
#     page = context.new_page()

#     # Initialize the Navigation class
#     navigation = Navigation(page)
#     navigation.homepage(login_credentials["url"], login_credentials["username"], login_credentials["password"])
#     logger.info("Logged in and initialized Navigation class")

#     # After login, return the page object for further use
#     yield page
#     logger.info("Closing context")
#     context.close()

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     """Configure Allure environment."""
#     logger.info("Configuring Allure environment")
#     if not hasattr(config, 'workerinput'):
#         # Only set environment variables if not running in a distributed mode
#         with open('allure-results/environment.properties', 'w') as f:
#             f.write('Browser=Chromium\n')
#             f.write('Headless=False\n')
#             f.write('URL={}\n'.format(os.getenv('LOGIN_URL')))
#         logger.info("Allure environment configured")
