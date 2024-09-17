import pytest
import allure
import logging
from utilities.pages.navigation import Navigation
from utilities.pages.Dashboard.dashboard import DashboardPage

log = logging.getLogger(__name__)


@allure.feature("Dashboard")
class TestDashboard:
    @pytest.mark.order(5)
    @allure.story("Dashboard")
    @allure.title("Show Features")
    @allure.description(
        "This test case adds a new topology and verifies the success message."
    )
    def test_view_dashboard(self, logged_in_page):
        """Test case for adding a new topology."""
        log.info("Starting test: add topology")
        navigation = Navigation(logged_in_page)
        dashboard_page = DashboardPage(logged_in_page)
        # Navigate to the topology page
        log.info("Navigating to Dashboard page")
        navigation.navigate_to_dashboard()
        # Add a new topology
        log.info("Showing added features on : Dashboard Page")
        dashboard_page.viewfeatures()

        # Verify success message
        # assert logged_in_page.locator("text=Topology added successfully").is_visible()
        log.info("Test add topology completed")
