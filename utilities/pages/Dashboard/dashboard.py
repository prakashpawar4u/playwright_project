import logging
from typing import Any
import allure  # Importing Allure

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DashboardPage:
    def __init__(self, page: Any):
        self.page = page
        logger.info("Initialized DashboardPage with page: %s", page)

    @allure.step("Viewing features")
    def viewfeatures(self) -> None:
        logger.info("Starting to view features")

        with allure.step("Select release '1.0'"):
            self.page.locator("#release").select_option("1.0")
            logger.info("Selected '1.0' for release")

        with allure.step("Select program 'SA_FDD'"):
            self.page.locator("#program").select_option("SA_FDD")
            logger.info("Selected 'SA_FDD' for program")

        with allure.step("Wait for 1 second"):
            import time

            time.sleep(1)
            logger.info("Waited for 1 second")


# import logging
# from typing import Any

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class DashboardPage:
#     def __init__(self, page: Any):
#         self.page = page
#         logger.info("Initialized DashboardPage with page: %s", page)

#     def viewfeatures(self) -> None:
#         logger.info("Starting to view features")

#         self.page.locator("#release").select_option("1.0")
#         logger.info("Selected '1.0' for release")

#         self.page.locator("#program").select_option("SA_FDD")
#         logger.info("Selected 'SA_FDD' for program")

#         import time
#         time.sleep(1)
#         logger.info("Waited for 1 second")
