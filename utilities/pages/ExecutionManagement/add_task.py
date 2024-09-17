import logging
import pytest

logger = logging.getLogger("app")

from .base_page import BasePage


class TestCaseExecutionPage(BasePage):
    def navigate_to_test_execution_management(self):
        self.page.get_by_role("link", name=" Add New Task").click()

    def add_executions(
        self,
        jobname,
        jobdescription,
        release,
        program,
        build,
        ue_type,
        bw,
        upgrade,
        tl_selection,
        testline,
        jobtype,
        label,
        jira,
        jobpriority,
    ):
        logger.info(jobname, jobdescription)
        self.page.get_by_role("link", name=" Add New Task").click()
        self.page.get_by_placeholder("Unique jobname").click()
        self.page.get_by_placeholder("Unique jobname").fill(jobname)
        self.page.get_by_placeholder("Job Description").click()
        self.page.get_by_placeholder("Job Description").fill(jobdescription)
        self.page.locator("#release").select_option(release)
        self.page.locator("#program").select_option(program)
        self.page.get_by_placeholder("load").click()
        self.page.get_by_placeholder("load").fill(build)
        self.page.locator("#bandwidth").select_option(bw)
        self.page.locator("#upgrade").select_option(upgrade)
        self.page.locator("#tl_selection").select_option(tl_selection)
        self.page.locator("#testline").select_option(testline)
        self.page.locator("#job_type").select_option(jobtype)
        self.page.get_by_placeholder("jira").click()
        self.page.get_by_placeholder("jira").fill(jira)
        self.page.locator("#job_priority").select_option(jobpriority)
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("row", name="Basic Tput").get_by_label("").check()
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("button", name="Submit").click()
