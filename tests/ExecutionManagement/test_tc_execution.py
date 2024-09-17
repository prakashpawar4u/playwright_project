"""
This module contains tests for the Test TC Execution functionality.
It includes various test cases to ensure that the test case management works as expected under different scenarios and inputs.
"""

import pytest


@pytest.mark.usefixtures("login")
class TestExecutionManagement:
    @pytest.mark.parametrize(
        "execution_data",
        [
            {
                "jobname": "CI Suite",
                "job_description": "CI_Basic_Sanity",
                "release": "1.0",
                "program": "SA_FDD",
                "build": "5.3.24.1",
                "ue": "OTA UE",
                "bw": "20Mbps",
                "upgrade": "With Bringup",
                "tl_selection": "Static",
                "testline": "TL1",
                "jobtype": "CI",
                "label": "P0",
                "jira": "1234",
                "jobpriority": "P0",
            }
        ],
    )
    def test_add_executions(self, test_case_execution_page, execution_data):
        # Navigate to the Test Case Management page

        # Add a new feature
        test_case_execution_page.add_executions(
            jobname=execution_data["jobname"],
            jobdescription=execution_data["job_description"],
            release=execution_data["release"],
            program=execution_data["program"],
            build=execution_data["build"],
            ue_type=execution_data["ue"],
            bw=execution_data["bw"],
            upgrade=execution_data["upgrade"],
            tl_selection=execution_data["tl_selection"],
            testline=execution_data["testline"],
            jobtype=execution_data["jobtype"],
            label=execution_data["label"],
            jira=execution_data["jira"],
            jobpriority=execution_data["jobpriority"],
        )

        # test_case_management_page.test_DL_alone()
        # test_case_management_page.test_UL_alone()
        # test_case_management_page.test_IntraDU_interfreq()
