from .base_page import BasePage
import logging

logger = logging.getLogger("app")


class ReleaseManagementPage(BasePage):
    def navigate_to_release_management(self):
        logger.debug("Navigating to Release Management page")
        self.page.get_by_role("link", name=" Release Management").click()

    def add_feature(
        self, release: str, program: str, feature: str, nr_ru: str, ue: str
    ):
        logger.debug(
            f"Adding feature: {feature} for release: {release}, program: {program}"
        )
        self.page.locator("#release").select_option(release)
        self.page.locator("#program").select_option(program)
        self.page.locator("#feature").select_option(feature)
        self.page.get_by_placeholder("NR RU").click()
        self.page.get_by_placeholder("NR RU").fill(nr_ru)
        self.page.locator("#ue").select_option(ue)
        self.page.get_by_role("button", name="Submit").click()
        logger.debug("Feature added")

    def is_feature_added(self):
        logger.debug("Checking if feature is added")
        return self.page.is_visible("text=Feature added successfully")

    # Other methods for interacting with the Release Management page
