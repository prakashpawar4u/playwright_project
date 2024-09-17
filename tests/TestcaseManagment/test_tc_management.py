"""
This module contains tests for the Test Case Management functionality.
It includes various test cases to ensure that the test case management works as expected under different scenarios and inputs.
"""

import pytest
import allure
import logging
from utilities.pages.navigation import Navigation
from utilities.pages.TestcaseManagement.tc_management import TestCaseManagementPage

log = logging.getLogger(__name__)
from utilities.DB.db_singleton import DatabaseSingleton


@allure.feature("Testcase Management")
class TestTCManagement:
    # @pytest.fixture(scope="class")
    def db(self):
        db = DatabaseSingleton(
            dbname="otaf_git",
            user="postgres",
            password="postgres",
            host="192.168.56.114",
            port="5432",
        )
        yield db
        db.close()

    @pytest.mark.parametrize(
        "tc_data",
        [
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Basic Tput",
                "title": "Perform Bidi UDP throughput",
                "goal": "Throughput",
                "description": "perform basic throughput",
                "NR Topology": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "req_Id": "111",
                "ue_type": "OTA UE",
                "priority": "P0",
                "direction": "Bidi",
            },
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Basic Tput",
                "title": "Peak DL UDP throughput",
                "goal": "Throughput",
                "description": "perform basic throughput",
                "NR Topology": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "req_Id": "112",
                "ue_type": "OTA UE",
                "priority": "P0",
                "direction": "DL",
            },
            {
                "release": "FirstDrop",
                "program": "SA_FDD",
                "feature": "Basic Tput",
                "title": "Peak UL UDP throughput",
                "goal": "Throughput",
                "description": "perform basic throughput",
                "NR Topology": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
                "req_Id": "113",
                "ue_type": "OTA UE",
                "priority": "P0",
                "direction": "UL",
            },
            # {
            #     "release": "FistrDrop", "program": "SA_FDD", "feature": "Basic Tput",
            #     "title": "IntraDU IntraFreq", "goal": "Throughput",
            #     "description": "perform basic throughput", "NR Topology": "1CU-1DU-1RU-1UE-OTAUE_SingleCell",
            #     "req_Id": "114","ue_type": "OTA UE", "priority": "P0", "direction":"Bidi"
            # }
        ],
    )
    @pytest.mark.order(7)
    @allure.step("Adds test cases to release")
    @allure.story("Testcase Management")
    @allure.description("This will add test cases to the TC management")
    @allure.title("Add Test cases")
    def test_add_testcases(self, logged_in_page, tc_data):
        """Adding test cases to test case management page

        Args:
            logged_in_page (_type_): _description_
            tc_data (_type_): _description_
        """
        log.info("Starting test :: Add test cases")
        navigation = Navigation(logged_in_page)
        test_case_page = TestCaseManagementPage(logged_in_page)

        # Navigate to Testcase Management page
        log.info("Navigating to Testcase Management page")
        navigation.navigate_to_testcase_management()

        # Add new test cases
        test_case_page.add_test_case(
            release=tc_data["release"],
            program=tc_data["program"],
            feature=tc_data["feature"],
            title=tc_data["title"],
            goal=tc_data["goal"],
            description=tc_data["description"],
            nr_topology=tc_data["NR Topology"],
            req_Id=tc_data["req_Id"],
            ue_type=tc_data["ue_type"],
            priority=tc_data["priority"],
            direction=tc_data["direction"],
        )

    # def test_validate_feature_names(self, db):
    #     expected_features = ["Basic Tput", "HO"]
    #     assert db.validate_feature_names(expected_features), f"Features did not match. Expected: {expected_features}"

    # def test_validate_titles(self, db):
    #     expected_titles = ["Perform Bidi UDP throughput", "IntraDU handover with bidi throughput"]
    #     assert
