import pytest
import allure
import logging
from utilities.pages.navigation import Navigation
from utilities.pages.TestcasePlanManagement.tc_plan_management import (
    TestPlanManagementPage,
)

log = logging.getLogger(__name__)


@allure.feature("Test Plan Management")
class TestPlanManagement:

    @pytest.mark.parametrize(
        "testplan_data",
        [
            {
                "plan_name": "FirstTestPlan",
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Basic Tput",
            },
            # {"plan_name": "FirstTestPlan", "release": "FirstDrop","program": "SA_FDD", "feature": "Basic Tput"},
            # {"plan_name": "FirstTestPlan", "release": "FirstDrop","program": "SA_FDD", "feature": "Basic Tput"}
            # Add more features here as needed
        ],
    )
    @pytest.mark.order(8)
    @allure.story("Testplan Management")
    @allure.title("Create Test Plan")
    @allure.description(
        "This test case adds features to release management page & verifies if the feature is added successfully."
    )
    def test_create_testplan(self, logged_in_page, testplan_data):
        """Test case for adding a test plan"""
        log.info("Starting test:: create_testplan")
        navigation = Navigation(logged_in_page)
        testplan_mgmt_page = TestPlanManagementPage(logged_in_page)

        # Navigate to the test plan management page
        log.info("Navigating to Testplan Management page")
        navigation.navigate_to_testplan_management()

        # Add a new feature
        testplan_mgmt_page.create_testplan(
            tp_name=testplan_data["plan_name"],
            release=testplan_data["release"],
            program=testplan_data["program"],
            feature=testplan_data["feature"],
        )

    @pytest.mark.parametrize(
        "viewplan_data",
        [
            {"release": "FirstDrop", "program": "SA_FDD", "feature": "Basic Tput"},
            # {"plan_name": "FirstTestPlan", "release": "FirstDrop","program": "SA_FDD", "feature": "Basic Tput"},
            # {"plan_name": "FirstTestPlan", "release": "FirstDrop","program": "SA_FDD", "feature": "Basic Tput"}
            # Add more features here as needed
        ],
    )
    @pytest.mark.order(9)
    @allure.story("Test Plan Management")
    @allure.title("View test plan")
    @allure.description(
        "This test case adds features to release management page & verifies if the feature is added successfully."
    )
    def test_view_testplan(self, logged_in_page, viewplan_data):
        """Test case for adding a new feature."""
        log.info("Starting test: add features")
        navigation = Navigation(logged_in_page)
        testplan_mgmt_page = TestPlanManagementPage(logged_in_page)

        # Navigate to the test plan management page
        log.info("Navigating to Testplan Management page")
        navigation.navigate_to_testplan_management()

        # Add a new feature
        testplan_mgmt_page.view_testplan(
            release=viewplan_data["release"],
            program=viewplan_data["program"],
            feature=viewplan_data["feature"],
        )
