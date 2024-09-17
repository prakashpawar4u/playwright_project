import logging
from typing import Any
import allure  # Importing Allure

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TopologyPage:
    def __init__(self, page: Any):
        self.page = page
        logger.info("Initialized TopologyPage with page: %s", page)

    @allure.step("Adding Single Cell topology")
    def add_topo(
        self, topology_name: str, cu_count: str, du_count: str, ru_count: str
    ) -> None:
        logger.info("Starting to add topology")
        if topology_name == "SingleCell":
            self.SingleCell(topology_name, cu_count, du_count, ru_count)
        elif topology_name == "IntraDU":
            self.IntraDU(topology_name, cu_count, du_count, ru_count)
        elif topology_name == "InterDU":
            self.InterDU(topology_name, cu_count, du_count, ru_count)
        elif topology_name == "InterCU":
            self.InterCU(topology_name, cu_count, du_count, ru_count)
        else:
            print("Unknown topology name")

        # self.page.get_by_role("link", name="Add Topology").click()
        # logger.info("Clicked on 'Add Topology' link")

        # add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
        # add_btn.click()
        # logger.info("Clicked on 'Add' button")

        # self.page.get_by_placeholder("Topology name").click()
        # self.page.get_by_placeholder("Topology name").fill(topology_name)
        # logger.info(f"Filled 'Topology name' with '{topology_name}'")

        # # self.page.get_by_placeholder("DU count for CU").click()
        # # self.page.get_by_placeholder("DU count for CU").fill(cu_count)
        # # logger.info(f"Filled 'DU count for CU' with '{cu_count}'")

        # self.page.get_by_placeholder("DU count for CU").click()
        # self.page.get_by_placeholder("DU count for CU").fill(du_count)
        # logger.info(f"Filled 'DU count for CU' with '{du_count}'")

        # self.page.get_by_placeholder("RU count for DU 1").click()
        # self.page.get_by_placeholder("RU count for DU 1").fill(ru_count)
        # logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        # self.page.get_by_placeholder("UE", exact=True).click()
        # self.page.get_by_placeholder("UE", exact=True).fill("1")
        # logger.info("Filled 'UE' with '1'")

        # self.page.get_by_label("RU 1 - DU1").check()
        # #self.page.get_by_label("RU 2 - DU2").check()
        # logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU2'")

        # self.page.get_by_role("button", name="Generate").click()
        # self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
        # logger.info("Clicked 'Generate' button in dialog")

        # self.page.get_by_role("button", name="Confirm").click()
        # self.page.get_by_role("button", name="OK").click()
        # logger.info("Confirmed and clicked 'OK'")

    def SingleCell(
        self, topology_name: str, cu_count: str, du_count: str, ru_count: str
    ) -> None:
        logger.info("Starting to add topology")

        self.page.get_by_role("link", name="Add Topology").click()
        logger.info("Clicked on 'Add Topology' link")

        add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
        add_btn.click()
        logger.info("Clicked on 'Add' button")

        self.page.get_by_placeholder("Topology name").click()
        self.page.get_by_placeholder("Topology name").fill(topology_name)
        logger.info(f"Filled 'Topology name' with '{topology_name}'")

        # self.page.get_by_placeholder("DU count for CU").click()
        # self.page.get_by_placeholder("DU count for CU").fill(cu_count)
        # logger.info(f"Filled 'DU count for CU' with '{cu_count}'")

        self.page.get_by_placeholder("DU count for CU").click()
        self.page.get_by_placeholder("DU count for CU").fill(du_count)
        logger.info(f"Filled 'DU count for CU' with '{du_count}'")

        self.page.get_by_placeholder("RU count for DU 1").click()
        self.page.get_by_placeholder("RU count for DU 1").fill(ru_count)
        logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        self.page.get_by_placeholder("UE", exact=True).click()
        self.page.get_by_placeholder("UE", exact=True).fill("1")
        logger.info("Filled 'UE' with '1'")

        self.page.get_by_label("RU 1 - DU1").check()
        # self.page.get_by_label("RU 2 - DU2").check()
        logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU2'")

        self.page.get_by_role("button", name="Generate").click()
        self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
        logger.info("Clicked 'Generate' button in dialog")

        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="OK").click()
        logger.info("Confirmed and clicked 'OK'")

    @allure.step("Adding topology")
    def IntraDU(
        self, topology_name: str, cu_count: str, du_count: str, ru_count: str
    ) -> None:
        logger.info("Starting to add topology")

        self.page.get_by_role("link", name="Add Topology").click()
        logger.info("Clicked on 'Add Topology' link")

        add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
        add_btn.click()
        logger.info("Clicked on 'Add' button")

        self.page.get_by_placeholder("Topology name").click()
        self.page.get_by_placeholder("Topology name").fill(topology_name)
        logger.info(f"Filled 'Topology name' with '{topology_name}'")

        # self.page.get_by_placeholder("DU count for CU").click()
        # self.page.get_by_placeholder("DU count for CU").fill(cu_count)
        # logger.info(f"Filled 'DU count for CU' with '{cu_count}'")

        self.page.get_by_placeholder("DU count for CU").click()
        self.page.get_by_placeholder("DU count for CU").fill(du_count)
        logger.info(f"Filled 'DU count for CU' with '{du_count}'")

        self.page.get_by_placeholder("RU count for DU 1").click()
        self.page.get_by_placeholder("RU count for DU 1").fill(ru_count)
        logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        self.page.get_by_placeholder("UE", exact=True).click()
        self.page.get_by_placeholder("UE", exact=True).fill("1")
        logger.info("Filled 'UE' with '1'")

        self.page.get_by_label("RU 1 - DU1").check()
        self.page.get_by_label("RU 2 - DU1").check()
        logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU1'")

        self.page.get_by_role("button", name="Generate").click()
        self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
        logger.info("Clicked 'Generate' button in dialog")

        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="OK").click()
        logger.info("Confirmed and clicked 'OK'")

    @allure.step("Adding topology")
    def InterDU(
        self, topology_name: str, cu_count: str, du_count: str, ru_count: str
    ) -> None:
        logger.info("Starting to add topology")

        self.page.get_by_role("link", name="Add Topology").click()
        logger.info("Clicked on 'Add Topology' link")

        add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
        add_btn.click()
        logger.info("Clicked on 'Add' button")

        self.page.get_by_placeholder("Topology name").click()
        self.page.get_by_placeholder("Topology name").fill(topology_name)
        logger.info(f"Filled 'Topology name' with '{topology_name}'")

        # self.page.get_by_placeholder("DU count for CU").click()
        # self.page.get_by_placeholder("DU count for CU").fill(cu_count)
        # logger.info(f"Filled 'DU count for CU' with '{cu_count}'")

        self.page.get_by_placeholder("DU count for CU").click()
        self.page.get_by_placeholder("DU count for CU").fill(du_count)
        logger.info(f"Filled 'DU count for CU' with '{du_count}'")

        self.page.get_by_placeholder("RU count for DU 1").click()
        self.page.get_by_placeholder("RU count for DU 1").fill(ru_count)
        logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        self.page.get_by_placeholder("RU count for DU 2").click()
        self.page.get_by_placeholder("RU count for DU 2").fill(ru_count)
        logger.info(f"Filled 'RU count for DU 2' with '{ru_count}'")

        self.page.get_by_placeholder("UE", exact=True).click()
        self.page.get_by_placeholder("UE", exact=True).fill("1")
        logger.info("Filled 'UE' with '1'")

        self.page.get_by_label("RU 1 - DU1").check()
        self.page.get_by_label("RU 2 - DU2").check()
        logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU2'")

        self.page.get_by_role("button", name="Generate").click()
        self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
        logger.info("Clicked 'Generate' button in dialog")

        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="OK").click()
        logger.info("Confirmed and clicked 'OK'")

    @allure.step("Adding topology")
    def InterCU(
        self, topology_name: str, cu_count: str, du_count: str, ru_count: str
    ) -> None:
        logger.info("Starting to add topology")

        self.page.get_by_role("link", name="Add Topology").click()
        logger.info("Clicked on 'Add Topology' link")

        add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
        add_btn.click()
        logger.info("Clicked on 'Add' button")

        self.page.get_by_placeholder("Topology name").click()
        self.page.get_by_placeholder("Topology name").fill(topology_name)
        logger.info(f"Filled 'Topology name' with '{topology_name}'")

        self.page.locator("#nr_cu").click()
        self.page.locator("#nr_cu").fill(cu_count)
        logger.info(f"Filled 'NR CU' with '{cu_count}'")

        self.page.get_by_placeholder("DU count for CU 1").click()
        self.page.get_by_placeholder("DU count for CU 1").fill(du_count)
        logger.info(f"Filled 'DU count for CU' with '{cu_count}'")

        self.page.get_by_placeholder("DU count for CU 2").click()
        self.page.get_by_placeholder("DU count for CU 2").fill(du_count)
        logger.info(f"Filled 'DU count for CU' with '{du_count}'")

        # self.page.get_by_placeholder("RU count for DU 1").click()
        # self.page.get_by_placeholder("RU count for DU 1").fill(ru_count)
        # logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        # self.page.get_by_placeholder("RU count for DU 1").click()
        # self.page.get_by_placeholder("RU count for DU 1").fill(ru_count)
        # logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        self.page.locator("#cu1du1").click()
        self.page.locator("#cu1du1").fill(ru_count)
        logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        self.page.locator("#cu2du1").click()
        self.page.locator("#cu2du1").fill(ru_count)
        logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        # self.page.get_by_id("cu1du1").click()
        # self.page.get_by_id("cu1du1").fill(ru_count)
        # logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        # self.page.get_by_id("cu2du1").click()
        # self.page.get_by_id("cu2du1").fill(ru_count)
        # logger.info(f"Filled 'RU count for DU 1' with '{ru_count}'")

        self.page.get_by_placeholder("UE", exact=True).click()
        self.page.get_by_placeholder("UE", exact=True).fill("1")
        logger.info("Filled 'UE' with '1'")

        self.page.get_by_label("RU 1 - DU1").check()
        self.page.get_by_label("RU 2 - DU2").check()
        logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU2'")

        self.page.get_by_role("button", name="Generate").click()
        self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
        logger.info("Clicked 'Generate' button in dialog")

        self.page.get_by_role("button", name="Confirm").click()
        self.page.get_by_role("button", name="OK").click()
        logger.info("Confirmed and clicked 'OK'")

    # def add_topology(self) -> None:
    #     logger.info("Starting to add topology")

    #     with allure.step("Click on 'Add Topology' link"):
    #         self.page.get_by_role("link", name="Add Topology").click()
    #         logger.info("Clicked on 'Add Topology' link")

    #     with allure.step("Click on 'Add' button"):
    #         add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
    #         add_btn.click()
    #         logger.info("Clicked on 'Add' button")

    #     with allure.step("Fill 'Topology name' with 'InterDU'"):
    #         self.page.get_by_placeholder("Topology name").click()
    #         self.page.get_by_placeholder("Topology name").fill("InterDU")
    #         logger.info("Filled 'Topology name' with 'InterDU'")

    #     with allure.step("Fill 'DU count for CU' with '1'"):
    #         self.page.get_by_placeholder("DU count for CU").click()
    #         self.page.get_by_placeholder("DU count for CU").fill("1")
    #         logger.info("Filled 'DU count for CU' with '1'")

    #     with allure.step("Fill 'DU count for CU' with '2'"):
    #         self.page.get_by_placeholder("DU count for CU").click()
    #         self.page.get_by_placeholder("DU count for CU").fill("2")
    #         logger.info("Filled 'DU count for CU' with '2'")

    #     with allure.step("Fill 'RU count for DU 1' with '1'"):
    #         self.page.get_by_placeholder("RU count for DU 1").click()
    #         self.page.get_by_placeholder("RU count for DU 1").fill("1")
    #         logger.info("Filled 'RU count for DU 1' with '1'")

    #     with allure.step("Fill 'RU count for DU 2' with '1'"):
    #         self.page.get_by_placeholder("RU count for DU 2").click()
    #         self.page.get_by_placeholder("RU count for DU 2").fill("1")
    #         logger.info("Filled 'RU count for DU 2' with '1'")

    #     with allure.step("Fill 'UE' with '1'"):
    #         self.page.get_by_placeholder("UE", exact=True).click()
    #         self.page.get_by_placeholder("UE", exact=True).fill("1")
    #         logger.info("Filled 'UE' with '1'")

    #     with allure.step("Check 'RU 1 - DU1' and 'RU 2 - DU2'"):
    #         self.page.get_by_label("RU 1 - DU1").check()
    #         self.page.get_by_label("RU 2 - DU2").check()
    #         logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU2'")

    #     with allure.step("Click 'Generate' button in dialog"):
    #         self.page.get_by_role("button", name="Generate").click()
    #         self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
    #         logger.info("Clicked 'Generate' button in dialog")

    #     with allure.step("Confirm and click 'OK'"):
    #         self.page.get_by_role("button", name="Confirm").click()
    #         self.page.get_by_role("button", name="OK").click()
    #         logger.info("Confirmed and clicked 'OK'")

    @allure.step("Viewing topology")
    def view_topology(self) -> None:
        logger.info("Starting to view topology")

        with allure.step("Click on 'Add Topology' link"):
            self.page.get_by_role("link", name="Add Topology").click()
            logger.info("Clicked on 'Add Topology' link")

        with allure.step("Click on 'View' link"):
            self.page.get_by_role("link", name="View").click()
            logger.info("Clicked on 'View' link")

        # with allure.step("Check radio button"):
        #     self.page.get_by_role("radio").check()
        #     logger.info("Checked radio button")

        self.page.locator(
            'input[type="radio"][data-id="2CU-2DU-2RU-1UE-OTAUE_InterCU"]'
        ).check()
        logger.info("Checked radio button with data-id '2CU-2DU-2RU-1UE-OTAUE_InterCU'")

        with allure.step("Click 'Show Topology' button"):
            self.page.get_by_role("button", name="Show Topology").click()
            logger.info("Clicked 'Show Topology' button")

        with allure.step("Click 'OK' button"):
            self.page.get_by_role("button", name="OK").click()
            logger.info("Clicked 'OK' button")


# import logging
# from typing import Any

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class TopologyPage:
#     def __init__(self, page: Any):
#         self.page = page
#         logger.info("Initialized TopologyPage with page: %s", page)

#     def add_topology(self) -> None:
#         logger.info("Starting to add topology")
#         self.page.get_by_role("link", name="Add Topology").click()
#         logger.info("Clicked on 'Add Topology' link")

#         add_btn = self.page.wait_for_selector('//*[@id="add_btn"]')
#         add_btn.click()
#         logger.info("Clicked on 'Add' button")

#         self.page.get_by_placeholder("Topology name").click()
#         self.page.get_by_placeholder("Topology name").fill("InterDU")
#         logger.info("Filled 'Topology name' with 'InterDU'")

#         self.page.get_by_placeholder("DU count for CU").click()
#         self.page.get_by_placeholder("DU count for CU").fill("1")
#         logger.info("Filled 'DU count for CU' with '1'")

#         self.page.get_by_placeholder("DU count for CU").click()
#         self.page.get_by_placeholder("DU count for CU").fill("2")
#         logger.info("Filled 'DU count for CU' with '2'")

#         self.page.get_by_placeholder("RU count for DU 1").click()
#         self.page.get_by_placeholder("RU count for DU 1").fill("1")
#         logger.info("Filled 'RU count for DU 1' with '1'")

#         self.page.get_by_placeholder("RU count for DU 2").click()
#         self.page.get_by_placeholder("RU count for DU 2").fill("1")
#         logger.info("Filled 'RU count for DU 2' with '1'")

#         self.page.get_by_placeholder("UE", exact=True).click()
#         self.page.get_by_placeholder("UE", exact=True).fill("1")
#         logger.info("Filled 'UE' with '1'")

#         self.page.get_by_label("RU 1 - DU1").check()
#         self.page.get_by_label("RU 2 - DU2").check()
#         logger.info("Checked 'RU 1 - DU1' and 'RU 2 - DU2'")

#         self.page.get_by_role("button", name="Generate").click()
#         self.page.get_by_role("dialog").get_by_role("button", name="Generate").click()
#         logger.info("Clicked 'Generate' button in dialog")

#         self.page.get_by_role("button", name="Confirm").click()
#         self.page.get_by_role("button", name="OK").click()
#         logger.info("Confirmed and clicked 'OK'")

#     def view_topology(self) -> None:
#         logger.info("Starting to view topology")
#         self.page.get_by_role("link", name="Add Topology").click()
#         logger.info("Clicked on 'Add Topology' link")

#         self.page.get_by_role("link", name="View").click()
#         logger.info("Clicked on 'View' link")

#         self.page.get_by_role("radio").check()
#         logger.info("Checked radio button")

#         self.page.get_by_role("button", name="Show Topology").click()
#         logger.info("Clicked 'Show Topology' button")

#         self.page.get_by_role("button", name="OK").click()
#         logger.info("Clicked 'OK' button")
