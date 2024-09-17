import pytest
import allure
import logging
from utilities.pages.navigation import Navigation
from utilities.pages.Topology.add_topology import TopologyPage

log = logging.getLogger(__name__)


@allure.feature("Topology Management")
class TestTopology:
    @pytest.mark.parametrize(
        "topology_data",
        [
            {
                "topology_name": "SingleCell",
                "cu_count": "1",
                "du_count": "1",
                "ru_count": "1",
            },
            {
                "topology_name": "IntraDU",
                "cu_count": "1",
                "du_count": "1",
                "ru_count": "2",
            },
            {
                "topology_name": "InterDU",
                "cu_count": "1",
                "du_count": "2",
                "ru_count": "1",
            },
            {
                "topology_name": "InterCU",
                "cu_count": "2",
                "du_count": "1",
                "ru_count": "1",
            },
            # Add more features here as needed
        ],
    )
    @pytest.mark.order(1)
    @allure.story("Add Topology")
    @allure.title("Test Add Topology")
    @allure.description(
        "This test case adds a new topology and verifies the success message."
    )
    def test_add_topology(self, logged_in_page, topology_data):
        """Test case for adding a new topology."""
        log.info("Starting test: add topology")
        navigation = Navigation(logged_in_page)
        topology_page = TopologyPage(logged_in_page)
        # Navigate to the topology page
        log.info("Navigating to topology page")
        navigation.navigate_to_topology()
        # Add a new topology
        log.info("Adding new topology: Test Topology")
        topology_page.add_topo(
            topology_name=topology_data["topology_name"],
            cu_count=topology_data["cu_count"],
            du_count=topology_data["du_count"],
            ru_count=topology_data["ru_count"],
        )

    @pytest.mark.order(2)
    @allure.story("View Topology")
    @allure.title("Test View Topology")
    @allure.description("This test case views an existing topology.")
    def test_view_topology(self, logged_in_page):
        """Test case for viewing an existing topology."""
        log.info("Starting test: view topology")
        navigation = Navigation(logged_in_page)
        topology_page = TopologyPage(logged_in_page)
        log.info("Navigating to topology page")
        navigation.navigate_to_topology()
        # View topology
        log.info("Viewing topology")
        topology_page.view_topology()
        log.info("Test view topology completed")
