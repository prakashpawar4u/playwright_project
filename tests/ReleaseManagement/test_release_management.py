import pytest
import allure
import logging
from utilities.pages.navigation import Navigation
from utilities.pages.ReleaseManagement.release_management import ReleaseManagementPage

"""
This module contains tests for adding features to our release management page
"""

log = logging.getLogger(__name__)


@allure.feature("Test Release Management")
class TestReleaseManagement:

    @pytest.mark.parametrize(
        "feature_data",
        [
            {"feature": "IntraDU Intra freq", "prd_id": "111,121"},
            {"feature": "IntraDU Inter freq", "prd_id": "112,122"},
            {"feature": "InterDU Intra freq", "prd_id": "113,123"},
            {"feature": "InterDU Inter freq", "prd_id": "114,124"},
            {"feature": "InterCU Intra freq", "prd_id": "115,125"},
            {"feature": "InterCU Inter freq", "prd_id": "116,126"},
            {"feature": "Basic Tput", "prd_id": "11,21"},
            {"feature": "HO", "prd_id": "12,22"},
            {"feature": "CA", "prd_id": "13,23"},
            {"feature": "Sanity", "prd_id": "13,24"},
            # Add more features here as needed
        ],
    )
    @allure.story("Release Management")
    @allure.title("Add Features")
    @allure.description("This adds feature to the release management page")
    def test_add_feature(self, logged_in_page, feature_data):
        """Test case for adding a feature"""
        log.info("Starting test:: create_testplan")
        navigation = Navigation(logged_in_page)
        release_mgmt_page = ReleaseManagementPage(logged_in_page)

        # Navigate to the Release Management page
        log.info("Navigating to Release Management page")
        navigation.navigate_to_release_management()

        log.info("Starting test:: add features")
        release_mgmt_page.add_feature(
            feature=feature_data["feature"], release=feature_data["prd_id"]
        )

    @pytest.mark.parametrize(
        "release_data",
        [
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "du_per_cu": "1",
                "ru_per_du": "1",
                "max_cell": "6",
                "dl_tp": "380",
                "ul_tp": "75",
                "peak_du_dl": "380",
                "peak_du_ul": "75",
                "peak_cu_dl": "380",
                "peak_cu_ul": "75",
                "active_cell_users": "100",
                "active_du_users": "300",
                "active_cu_users": "900",
                "cucp_cores": "4",
                "cuup_cores": "8",
                "du_cores": "8",
                "uplane_latency": "40",
                "cplane_latency": "5",
            },
            {
                "release": "Drop1",
                "program": "SA_FDD",
                "objective": "IntraDU Handover ",
                "performance_target": "Successful Intra DU Handover by Dec end",
                "du_per_cu": "1",
                "ru_per_du": "1",
                "max_cell": "6",
                "dl_tp": "380",
                "ul_tp": "75",
                "peak_du_dl": "380",
                "peak_du_ul": "75",
                "peak_cu_dl": "380",
                "peak_cu_ul": "75",
                "active_cell_users": "100",
                "active_du_users": "300",
                "active_cu_users": "900",
                "cucp_cores": "4",
                "cuup_cores": "8",
                "du_cores": "8",
                "uplane_latency": "40",
                "cplane_latency": "5",
            },
            {
                "release": "Drop2",
                "program": "SA_FDD",
                "objective": "InterDU Handover",
                "performance_target": "Successful Inter DU Handover by Jan end",
                "du_per_cu": "1",
                "ru_per_du": "1",
                "max_cell": "6",
                "dl_tp": "380",
                "ul_tp": "75",
                "peak_du_dl": "380",
                "peak_du_ul": "75",
                "peak_cu_dl": "380",
                "peak_cu_ul": "75",
                "active_cell_users": "100",
                "active_du_users": "300",
                "active_cu_users": "900",
                "cucp_cores": "4",
                "cuup_cores": "8",
                "du_cores": "8",
                "uplane_latency": "40",
                "cplane_latency": "5",
            },
            {
                "release": "Drop3",
                "program": "SA_FDD",
                "objective": "InterCU Handover",
                "performance_target": "Successful inter CU Handover by Feb end",
                "du_per_cu": "1",
                "ru_per_du": "1",
                "max_cell": "6",
                "dl_tp": "380",
                "ul_tp": "75",
                "peak_du_dl": "380",
                "peak_du_ul": "75",
                "peak_cu_dl": "380",
                "peak_cu_ul": "75",
                "active_cell_users": "100",
                "active_du_users": "300",
                "active_cu_users": "900",
                "cucp_cores": "4",
                "cuup_cores": "8",
                "du_cores": "8",
                "uplane_latency": "40",
                "cplane_latency": "5",
            },
        ],
    )
    @allure.story("Release Management")
    @allure.title("Add Release")
    @allure.description("This adds feature to the release management page")
    def test_add_release(self, logged_in_page, release_data):
        """Test case for adding a release"""
        log.info("Starting test:: add release")
        navigation = Navigation(logged_in_page)
        release_mgmt_page = ReleaseManagementPage(logged_in_page)

        # Navigate to the Release Management page
        log.info("Navigating to Release Management page")
        navigation.navigate_to_release_management()

        release_mgmt_page.add_release(
            release=release_data["release"],
            program=release_data["program"],
            objective=release_data["objective"],
            performance_target=release_data["performance_target"],
            du_per_cu=release_data["du_per_cu"],
            ru_per_du=release_data["ru_per_du"],
            max_cell=release_data["max_cell"],
            dl_tp=release_data["dl_tp"],
            ul_tp=release_data["ul_tp"],
            peak_du_dl=release_data["peak_du_dl"],
            peak_du_ul=release_data["peak_du_ul"],
            peak_cu_dl=release_data["peak_cu_dl"],
            peak_cu_ul=release_data["peak_cu_ul"],
            active_cell_users=release_data["active_cell_users"],
            active_du_users=release_data["active_du_users"],
            active_cu_users=release_data["active_cu_users"],
            cucp_cores=release_data["cucp_cores"],
            cuup_cores=release_data["cuup_cores"],
            du_cores=release_data["du_cores"],
            # ru_per_du=release_data["ru_per_du"],
            uplane_latency=release_data["uplane_latency"],
            cplane_latency=release_data["cplane_latency"],
        )

    @pytest.mark.parametrize(
        "map_feature_data",
        [
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Basic Tput",
                "topo": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "111",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Sanity",
                "topo": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "112",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "CA",
                "topo": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "113",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "Drop1",
                "program": "SA_FDD",
                "feature": "IntraDU Intra freq",
                "topo": "1CU-1DU-2RU-1UE-OTAUE_IntraDU",
                "objective": "IntraDU Handover ",
                "performance_target": "Successful Intra DU Handover by Dec end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "121",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "Drop1",
                "program": "SA_FDD",
                "feature": "IntraDU Inter freq",
                "topo": "1CU-1DU-2RU-1UE-OTAUE_IntraDU",
                "objective": "IntraDU Handover ",
                "performance_target": "Successful Intra DU interfreq Handover by Dec end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "122",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "Drop2",
                "program": "SA_FDD",
                "feature": "IntraDU Intra freq",
                "topo": "1CU-2DU-2RU-1UE-OTAUE_InterDU",
                "objective": "InterDU Handover",
                "performance_target": "Successful Inter DU intra freq Handover by Jan end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "221",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "Drop2",
                "program": "SA_FDD",
                "feature": "IntraDU Inter freq",
                "topo": "1CU-2DU-2RU-1UE-OTAUE_InterDU",
                "objective": "InterDU Handover",
                "performance_target": "Successful Inter DU inter freq Handover by Jan end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "222",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "Drop3",
                "program": "SA_FDD",
                "feature": "IntraDU Intra freq",
                "topo": "2CU-2DU-2RU-1UE-OTAUE_InterCU",
                "objective": "InterCU Handover",
                "performance_target": "Successful inter CU intra freq Handover by Feb end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "121",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "Drop3",
                "program": "SA_FDD",
                "feature": "IntraDU Inter freq",
                "topo": "2CU-2DU-2RU-1UE-OTAUE_InterCU",
                "objective": "InterCU Handover",
                "performance_target": "Successful inter CU inter freq Handover by Feb end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "122",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
        ],
    )
    @allure.story("Release Management")
    @allure.title("Map Features")
    @allure.description("This adds feature to the release management page")
    def test_map_features(self, logged_in_page, map_feature_data):
        """Test case for adding a feature"""
        log.info("Starting test:: create_testplan")
        navigation = Navigation(logged_in_page)
        release_mgmt_page = ReleaseManagementPage(logged_in_page)

        # Navigate to the Release Management page
        log.info("Navigating to Release Management page")
        navigation.navigate_to_release_management()

        log.info("Starting test:: add features")
        release_mgmt_page.map_features(
            map_feature_data["release"],
            map_feature_data["program"],
            map_feature_data["feature"],
            map_feature_data["topo"],
            map_feature_data["objective"],
            map_feature_data["performance_target"],
            map_feature_data["cu_hw"],
            map_feature_data["du_hw"],
            map_feature_data["ru_hw"],
            map_feature_data["smo_hw"],
            map_feature_data["platform"],
            map_feature_data["user_stories"],
            map_feature_data["feature_interaction"],
            map_feature_data["estimated_tc"],
            map_feature_data["team_count"],
        )

    @pytest.mark.parametrize(
        "releaseplan_data",
        [
            {
                "release_plan": "FirstDropPlan",
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Basic Tput",
                "topo": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "111",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Sanity",
                "topo": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "112",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "CA",
                "topo": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "objective": "Attach Tput & Ping",
                "performance_target": "Attach Tput & Ping by Oct end",
                "cu_hw": "R740",
                "du_hw": "R750",
                "ru_hw": "MTI",
                "smo_hw": "R740",
                "platform": "Rocky",
                "user_stories": "113",
                "feature_interaction": "placeholder",
                "estimated_tc": "6",
                "team_count": "5",
            },
        ],
    )
    # release_plan: str, release: str, start_date: str, end_date: str,
    # objective: str, performance_tar: str
    @allure.story("Release Management")
    @allure.title("Create Release Plan")
    @allure.description("This creates release plan to the release management page")
    def test_create_releaseplan(self, logged_in_page, releaseplan_data):
        """Test case for adding a feature"""
        log.info("Starting test:: create_testplan")
        navigation = Navigation(logged_in_page)
        release_mgmt_page = ReleaseManagementPage(logged_in_page)

        # Navigate to the Release Management page
        log.info("Navigating to Release Management page")
        navigation.navigate_to_release_management()

        log.info("Starting test:: add features")
        release_mgmt_page.add_release(
            release=release_data["release"],
            program=release_data["program"],
            feature=release_data["feature"],
            nr_cu=release_data["NR CU"],
            nr_du=release_data["NR DU"],
            nr_ru=release_data["NR RU"],
            ue=release_data["ue"],
        )

    @allure.story("Release Management")
    @allure.title("Add Release")
    @allure.description("This adds feature to the release management page")
    def test_map_testplan(self, logged_in_page, release_data):
        """Test case for adding a feature"""
        log.info("Starting test:: create_testplan")
        navigation = Navigation(logged_in_page)
        release_mgmt_page = ReleaseManagementPage(logged_in_page)

        # Navigate to the Release Management page
        log.info("Navigating to Release Management page")
        navigation.navigate_to_release_management()

        log.info("Starting test:: add features")
        release_mgmt_page.add_release(
            release=release_data["release"],
            program=release_data["program"],
            feature=release_data["feature"],
            nr_cu=release_data["NR CU"],
            nr_du=release_data["NR DU"],
            nr_ru=release_data["NR RU"],
            ue=release_data["ue"],
        )

    @allure.story("Release Management")
    @allure.title("Add Release")
    @allure.description("This adds feature to the release management page")
    def test_view_releaseplan(self, logged_in_page, release_data):
        """Test case for adding a feature"""
        log.info("Starting test:: create_testplan")
        navigation = Navigation(logged_in_page)
        release_mgmt_page = ReleaseManagementPage(logged_in_page)

        # Navigate to the Release Management page
        log.info("Navigating to Release Management page")
        navigation.navigate_to_release_management()

        log.info("Starting test:: add features")
        release_mgmt_page.add_release(
            release=release_data["release"],
            program=release_data["program"],
            feature=release_data["feature"],
            nr_cu=release_data["NR CU"],
            nr_du=release_data["NR DU"],
            nr_ru=release_data["NR RU"],
            ue=release_data["ue"],
        )
