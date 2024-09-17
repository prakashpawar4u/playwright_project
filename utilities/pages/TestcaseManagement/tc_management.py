import logging
from typing import Any
from playwright.sync_api import (
    Page,
)  # Assuming you're using Playwright for page interactions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


import allure
import time


class TestCaseManagementPage:
    def __init__(self, page: Page):
        self.page = page
        logger.info("Initialized Testcase management page: %s", page)

    def execute_test(self, direction):
        if direction == "DL":
            self.test_DL_alone()
        elif direction == "UL":
            self.test_UL_alone()
        elif direction == "Bidi":
            self.test_Bidi()
        else:
            logger.error(f"Invalid direction: {direction}")
            self.test_IntraDU_interfreq()

    @allure.step("Adds test cases to release")
    @allure.feature("Basic Sanity")
    @allure.story("Story Name")
    # @allure.testcase(title)
    @allure.tag("Sanity")
    def add_test_case(
        self,
        release,
        program,
        feature,
        title,
        goal,
        description,
        nr_topology,
        req_Id,
        ue_type,
        priority,
        direction,
    ):
        # import pdb; pdb.set_trace()
        self.page.get_by_role("link", name="Add Testcase").click()

        self.page.locator("#tc_release").wait_for(state="visible")
        # self.page.locator("#tc_release").wait_for(state="enabled")
        self.page.locator("#tc_release").select_option(release)
        logger.info(f"Selected release: {release}")

        # self.page.locator("#tc_release").select_option(release)
        self.page.locator("#tc_program").select_option(program)
        self.page.locator("#tc_feature").select_option(feature)
        self.page.get_by_role("textbox", name="Testcase title").click()
        self.page.get_by_role("textbox", name="Testcase title").fill(title)
        self.page.get_by_role("textbox", name="Testcase goal").click()
        self.page.get_by_role("textbox", name="Testcase goal").fill(goal)
        self.page.get_by_role("textbox", name="Description").click()
        self.page.get_by_role("textbox", name="Description").fill(description)
        # time.sleep(3)
        self.page.get_by_role("button", name="Submit").click()
        self.page.get_by_role("button", name="Add Details").click()
        time.sleep(1)
        self.page.query_selector('xpath=//*[@id="GetMoreDetails"]').click()

        # element = self.page.query_selector('xpath=//*[@id="GetMoreDetails"]').click()
        # element.click()

        # self.page.locator("#topology").select_option(nr_topology)

        self.page.get_by_placeholder("Requirement ID").click()
        self.page.get_by_placeholder("Requirement ID").fill(req_Id)
        # self.page.locator("#ue").select_option(ue_type)
        self.page.locator("#tc_priority").select_option(priority)
        self.execute_test(direction)

    def test_DL_alone(self):
        logger.info(f" Test DL alone is added")
        self.page.get_by_role("button", name="Common").click()
        self.page.query_selector('xpath=//*[@id="Perform Attach UE"]').dblclick()
        self.page.query_selector('xpath=//*[@id="Verify Attach UE"]').dblclick()
        self.page.get_by_role("button", name="Traffic").click()
        self.page.query_selector('xpath=//*[@id="Perform UDP DL Tput"]').dblclick()
        self.page.query_selector('xpath=//*[@id="Verify UDP DL Tput"]').dblclick()

        self.page.get_by_role("button", name="Common").click()
        self.page.query_selector('xpath=//*[@id="Verify Detach UE"]').dblclick()

        self.page.get_by_role("button", name="Traffic").click()
        self.page.query_selector('xpath=//*[@id="Verify UDP DL Tput"]').dblclick()
        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="Submit").click()

    def test_UL_alone(self):
        self.page.get_by_role("button", name="Common").click()
        time.sleep(1)
        self.page.wait_for_selector(
            'button[id="Perform Attach UE"][value="Perform Attach UE"]'
        )
        self.page.locator(
            'button[id="Perform Attach UE"][value="Perform Attach UE"]'
        ).click()
        time.sleep(1)
        self.page.wait_for_selector(
            'button[id="Verify Attach UE"][value="Verify Attach UE"]'
        )
        self.page.locator(
            'button[id="Verify Attach UE"][value="Verify Attach UE"]'
        ).click()

        # self.page.get_by_role("button", name="Perform Attach UE").click()
        # time.sleep(5)
        # self.page.get_by_role("button", name="Verify Attach UE").click()
        # time.sleep(2)
        # self.page.get_by_role("button", name="Traffic").click()
        # self.page.get_by_role("button", name="Perform UDP UL Tput").click()

        # time.sleep(1)
        # self.page.get_by_role("button", name="Common").click()
        # self.page.get_by_role("button", name="Perform Detach UE").click()
        # time.sleep(1)
        # self.page.get_by_role("button", name="Verify Detach UE").click()
        # time.sleep(1)

        # self.page.get_by_role("button", name="Traffic").click()
        # self.page.get_by_role("button", name="Verify UDP UL Tput").click()
        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="Submit").click()

        # self.page.query_selector('xpath=//*[@id="Perform UDP UL Tput"]').dblclick()
        # time.sleep(.5)

        # self.page.get_by_role("button", name="Common").click()
        # self.page.query_selector('xpath=//*[@id="Perform Detach UE"]').dblclick()
        # self.page.query_selector('xpath=//*[@id="Verify Detach UE"]').dblclick()
        # self.page.get_by_role("button", name="Traffic").click()
        # self.page.query_selector('xpath=//*[@id="Verify UDP UL Tput"]').dblclick()
        # self.page.get_by_role("button", name="Confirm").click()
        # self.page.get_by_role("button", name="Submit").click()
        # logger.info(f" Test UL alone is added")

    # def test_UL_alone(self):
    #     self.page.get_by_role("button", name="Common").click()
    #     time.sleep(.5)
    #     self.page.query_selector('xpath=//*[@id="Perform Attach UE"]').dblclick()
    #     time.sleep(.5)
    #     self.page.query_selector('xpath=//*[@id="Verify Attach UE"]').dblclick()
    #     time.sleep(.5)
    #     self.page.get_by_role("button", name="Traffic").click()
    #     self.page.query_selector('xpath=//*[@id="Perform UDP UL Tput"]').dblclick()
    #     time.sleep(.5)

    #     self.page.get_by_role("button", name="Common").click()
    #     self.page.query_selector('xpath=//*[@id="Perform Detach UE"]').dblclick()
    #     self.page.query_selector('xpath=//*[@id="Verify Detach UE"]').dblclick()
    #     self.page.get_by_role("button", name="Traffic").click()
    #     self.page.query_selector('xpath=//*[@id="Verify UDP UL Tput"]').dblclick()
    #     self.page.get_by_role("button", name="Confirm").click()
    #     self.page.get_by_role("button", name="Submit").click()
    #     logger.info(f" Test UL alone is added")

    def test_Bidi(self):
        # Click the "Common" button
        self.page.get_by_role("button", name="Common").click()
        self.page.wait_for_selector("#Perform\\ Attach\\ UE")
        self.page.locator("#Perform\\ Attach\\ UE").click()
        self.page.wait_for_timeout(500)  # Adding a small delay
        self.page.wait_for_selector("#Verify\\ Attach\\ UE")
        self.page.locator("#Verify\\ Attach\\ UE").click()
        self.page.wait_for_timeout(500)  # Adding a small delay

        # Click the "Traffic" button
        self.page.get_by_role("button", name="Traffic").click()
        self.page.wait_for_selector("#Perform\\ UDP\\ BiDi\\ Tput")
        self.page.locator("#Perform\\ UDP\\ BiDi\\ Tput").click()
        self.page.wait_for_timeout(500)  # Adding a small delay

        # Click the "Common" button again
        self.page.get_by_role("button", name="Common").click()
        self.page.wait_for_selector("#Perform\\ Detach\\ UE")
        self.page.locator("#Perform\\ Detach\\ UE").click()
        self.page.wait_for_timeout(500)  # Adding a small delay
        self.page.wait_for_selector("#Verify\\ Detach\\ UE")
        self.page.locator("#Verify\\ Detach\\ UE").click()
        self.page.wait_for_timeout(500)  # Adding a small delay

        # Click the "Traffic" button again
        self.page.get_by_role("button", name="Traffic").click()
        self.page.wait_for_selector("#Verify\\ UDP\\ BiDi\\ Tput")
        self.page.locator("#Verify\\ UDP\\ BiDi\\ Tput").click()
        self.page.wait_for_timeout(500)  # Adding a small delay

        # Confirm and submit
        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="Submit").click()
        logger.info(f"Test Bidi should get invoked")

    # def test_Bidi(self):
    #     self.page.get_by_role("button", name="Common").click()
    #     self.page.query_selector('xpath=//*[@id="Perform Attach UE"]').click()
    #     self.page.query_selector('xpath=//*[@id="Verify Attach UE"]').click()

    #     self.page.get_by_role("button", name="Traffic").click()
    #     #self.page.locator("[id='Perform UDP BiDi Tput']").dblclick()
    #     #//*[@id="Perform UDP BiDi Tput"]
    #     self.page.query_selector('xpath=//*[@id="Perform UDP BiDi Tput"]').click()
    #     #self.page.get_by_role("button", name="Perform UDP BiDi Tput").dblclick()

    #     self.page.get_by_role("button", name="Common").click()
    #     #self.page.locator("[id='Perform Detach UE']").dblclick()
    #     self.page.query_selector('xpath=//*[@id="Perform Detach UE"]').click()
    #     #self.page.get_by_role("button", name="Perform Detach UE").dblclick()
    #     #self.page.locator("[id='Verify Detach UE']").dblclick()
    #     self.page.query_selector('xpath=//*[@id="Verify Detach UE"]').click()
    #     #self.page.get_by_role("button", name="Verify Detach UE").dblclick()

    #     self.page.get_by_role("button", name="Traffic").click()
    #     #self.page.locator("[id='Verify UDP BiDi Tput']").dblclick()
    #     self.page.query_selector('xpath=//*[@id="Verify UDP BiDi Tput"]').click()

    #     #self.page.get_by_role("button", name="Verify UDP BiDi Tput").dblclick()
    #     self.page.get_by_role("button", name="Confirm").click()
    #     self.page.get_by_role("button", name="Submit").click()
    #     logger.info(f"Test Bidi should get invoked")

    def test_IntraDU_interfreq(self):
        self.page.get_by_role("button", name="Common").click()
        self.page.locator("[id='Perform Attach UE']").dblclick()
        self.page.locator("[id='Verify Attach UE']").dblclick()

        self.page.get_by_role("button", name="Feature").click()
        self.page.get_by_role("button", name="Intra DU HO").click()

        self.page.locator("[id='Perform IntraDU InterFreq HO']").dblclick()
        self.page.get_by_role("button", name="Common").click()
        self.page.locator("[id='Perform Detach UE']").dblclick()
        self.page.locator("[id='Verify Detach UE']").dblclick()
        self.page.get_by_role("button", name="Traffic").click()
        self.page.locator("[id='Verify IntraDU InterFreq HO']").dblclick()
        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="Submit").click()
        logger.info(f"Test IntraDU inter freq")

    #
    # # Add more methods as needed for different steps
