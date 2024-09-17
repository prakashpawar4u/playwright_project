import logging
from typing import Any
from playwright.sync_api import (
    Page,
)  # Assuming you're using Playwright for page interactions

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ReleaseManagementPage:
    def __init__(self, page: Page):
        self.page = page
        logger.info("Initialized ReleaseManagementPage with page: %s", page)

    def add_feature(self, feature: str, prd_id: str):
        logger.info("Adding feature: %s with PRD ID: %s", feature, prd_id)
        self.page.get_by_role("link", name="Add Feature").click()
        logger.info("Clicked on Add Feature link")
        self.page.get_by_role("button", name=" Add").click()
        self.page.get_by_role("textbox", name="Feature").click()
        self.page.get_by_role("textbox", name="Feature").fill(feature)
        logger.info("Filled feature: %s", feature)
        self.page.get_by_role("textbox", name="comma separated PRD numbers").click()
        self.page.get_by_role("textbox", name="comma separated PRD numbers").fill(
            prd_id
        )
        logger.info("Filled PRD ID: %s", prd_id)
        self.page.get_by_role("button", name="Add", exact=True).click()
        self.page.get_by_role("button", name="OK").click()
        logger.info("Feature added successfully")

    def add_release(
        self,
        release: str,
        program: str,
        objective: str,
        performance_target: str,
        du_per_cu: str,
        ru_per_du: str,
        max_cell: str,
        dl_tp: str,
        ul_tp: str,
        peak_du_dl: str,
        peak_du_ul: str,
        peak_cu_dl: str,
        peak_cu_ul: str,
        active_cell_users: str,
        active_du_users: str,
        active_cu_users: str,
        cucp_cores: str,
        cuup_cores: str,
        du_cores: str,
        uplane_latency: str,
        cplane_latency: str,
    ) -> None:
        logger.info("Adding a new release")
        self.page.get_by_role("link", name="Add Release").click()
        self.page.get_by_placeholder("release", exact=True).click()
        self.page.get_by_placeholder("release", exact=True).fill(release)
        logger.info(f"Filled release version: {release}")
        self.page.locator("#program").select_option(program)
        logger.info(f"Selected program: {program}")
        self.page.get_by_placeholder("High level objective for").click()
        self.page.get_by_placeholder("High level objective for").fill(objective)
        logger.info(f"Filled high level objective: {objective}")
        self.page.get_by_placeholder("High level performance target").click()
        self.page.get_by_placeholder("High level performance target").fill(
            performance_target
        )
        logger.info(f"Filled high level performance target: {performance_target}")
        self.page.get_by_placeholder("DU per CU").click()
        self.page.get_by_placeholder("DU per CU").fill(du_per_cu)
        logger.info(f"Filled DU per CU: {du_per_cu}")
        self.page.get_by_placeholder("RU per DU").click()
        self.page.get_by_placeholder("RU per DU").fill(ru_per_du)
        logger.info(f"Filled RU per DU: {ru_per_du}")
        self.page.get_by_placeholder("MaxCell").click()
        self.page.get_by_placeholder("MaxCell").fill(max_cell)
        logger.info(f"Filled MaxCell: {max_cell}")
        self.page.get_by_placeholder("DL TP").dblclick()
        self.page.get_by_placeholder("DL TP").fill(dl_tp)
        logger.info(f"Filled DL TP: {dl_tp}")
        self.page.get_by_placeholder("UL TP").dblclick()
        self.page.get_by_placeholder("UL TP").fill(ul_tp)
        logger.info(f"Filled UL TP: {ul_tp}")
        self.page.locator("#peak_du_dltput").dblclick()
        self.page.locator("#peak_du_dltput").fill(peak_du_dl)
        logger.info(f"Filled peak DU DL throughput: {peak_du_dl}")
        self.page.locator("#peak_du_ultput").dblclick()
        self.page.locator("#peak_du_ultput").fill(peak_du_ul)
        logger.info(f"Filled peak DU UL throughput: {peak_du_ul}")
        self.page.locator("#peak_cu_dltput").dblclick()
        self.page.locator("#peak_cu_dltput").fill(peak_cu_dl)
        logger.info(f"Filled peak CU DL throughput: {peak_cu_dl}")
        self.page.locator("#peak_cu_ultput").dblclick()
        self.page.locator("#peak_cu_ultput").fill(peak_cu_ul)
        logger.info(f"Filled peak CU UL throughput: {peak_cu_ul}")
        self.page.get_by_text("Release Program Select").click()
        self.page.get_by_placeholder("Active CellUsers").dblclick()
        self.page.get_by_placeholder("Active CellUsers").fill(active_cell_users)
        logger.info(f"Filled Active CellUsers: {active_cell_users}")
        self.page.get_by_placeholder("Active DUUsers").dblclick()
        self.page.get_by_placeholder("Active DUUsers").fill(active_du_users)
        logger.info(f"Filled Active DUUsers: {active_du_users}")
        self.page.get_by_placeholder("Active CUUsers").dblclick()
        self.page.get_by_placeholder("Active CUUsers").fill(active_cu_users)
        logger.info(f"Filled Active CUUsers: {active_cu_users}")
        self.page.get_by_placeholder("CUCP cores").click()
        self.page.get_by_placeholder("CUCP cores").fill(cucp_cores)
        logger.info(f"Filled CUCP cores: {cucp_cores}")
        self.page.get_by_placeholder("CUUP cores").dblclick()
        self.page.get_by_placeholder("CUUP cores").fill(cuup_cores)
        logger.info(f"Filled CUUP cores: {cuup_cores}")
        self.page.get_by_placeholder("DU cores").click()
        self.page.get_by_placeholder("DU cores").fill(du_cores)
        logger.info(f"Filled DU cores: {du_cores}")
        self.page.locator("#uplane_max_latency").dblclick()
        self.page.locator("#uplane_max_latency").fill(uplane_latency)
        logger.info(f"Filled U-plane max latency: {uplane_latency}")
        self.page.locator("#cplane_max_latency").dblclick()
        self.page.locator("#cplane_max_latency").fill(cplane_latency)
        logger.info(f"Filled C-plane max latency: {cplane_latency}")
        self.page.get_by_role("button", name="Submit").click()
        logger.info("Submitted the release")

    def map_features(
        self,
        release: str,
        program: str,
        feature: str,
        topology: str,
        objective: str,
        performance_tar: str,
        cu_hw: str,
        du_hw: str,
        ru_hw: str,
        smo_hw: str,
        platform: str,
        user_stories: str,
        feature_interaction: str,
        estimated_tc: str,
        team_count: str,
    ) -> None:
        logger.debug(
            f"Mapping features for release: {release}, program: {program}, feature: {feature}"
        )
        self.page.get_by_role("link", name="Map Features").click()
        self.page.locator("#release").select_option(release)
        self.page.locator("#program").select_option(program)
        self.page.locator("#feature").select_option(feature)
        self.page.get_by_role("listbox").select_option(topology)
        self.page.get_by_placeholder("High level objective for").click()
        self.page.get_by_placeholder("High level objective for").fill(objective)
        self.page.get_by_placeholder("High level Performance Target").click()
        self.page.get_by_placeholder("High level Performance Target").fill(
            performance_tar
        )
        self.page.get_by_placeholder("CU Hardware").click()
        self.page.get_by_placeholder("CU Hardware").fill(cu_hw)
        self.page.get_by_placeholder("DU Hardware").click()
        self.page.get_by_placeholder("DU Hardware").fill(du_hw)
        self.page.get_by_placeholder("RU Hardware").click()
        self.page.get_by_placeholder("RU Hardware").fill(ru_hw)
        self.page.get_by_placeholder("SMO Hardware").click()
        self.page.get_by_placeholder("SMO Hardware").fill(smo_hw)
        self.page.get_by_placeholder("platform").click()
        self.page.get_by_placeholder("platform").fill(platform)
        self.page.get_by_placeholder("platform").press("Tab")
        self.page.get_by_placeholder("user_stories").fill(user_stories)
        self.page.get_by_placeholder("feature_interactions").click()
        self.page.get_by_placeholder("feature_interactions").fill(feature_interaction)
        self.page.get_by_placeholder("tc_count").click()
        self.page.get_by_placeholder("tc_count").fill(estimated_tc)
        self.page.get_by_role("button", name="Submit").click()

    def create_release_plan(
        self,
        release_plan: str,
        release: str,
        start_date: str,
        end_date: str,
        objective: str,
        performance_tar: str,
    ) -> None:
        logger.debug(
            f"Creating release plan: {release_plan} for release: {release}, from {start_date} to {end_date}"
        )
        self.page.get_by_role("link", name="Create Release Plan").click()
        self.page.get_by_placeholder("Unique Release Plan name").click()
        self.page.get_by_placeholder("Unique Release Plan name").fill(release_plan)
        self.page.locator("#release").select_option(release)
        self.page.locator("#start_date").fill(start_date)
        self.page.locator("#end_date").fill(end_date)
        self.page.get_by_placeholder("Objective").click()
        self.page.get_by_placeholder("Objective").fill(objective)
        self.page.get_by_placeholder("Performance Target").click()
        self.page.get_by_placeholder("Performance Target").fill(performance_tar)
        self.page.get_by_role("button", name="Submit").click()

    def map_testplan(self):
        """this will associate release to release plan"""
        pass

    def is_feature_added(self, feature: str) -> bool:
        logger.debug("Checking if feature '%s' is added", feature)
        return self.page.is_visible(f"text={feature} added successfully")


#     def is_feature_added(self, feature: str) -> bool:
#         logger.debug(f"Checking if feature '{feature}' is added")
#         return self.page.is_visible(f"text={feature} added successfully")
#     # Other methods for interacting with the Release Management page
