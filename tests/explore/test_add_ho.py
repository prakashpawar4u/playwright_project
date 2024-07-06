"""
This module contains tests for the add functionality.
It includes various test cases to ensure that the add functionality
works as expected under different scenarios and inputs.
"""

from playwright.sync_api import Playwright, sync_playwright

# from playwright.sync_api import Playwright, sync_playwright, expect


def test_intradu_interfreq(playwright: Playwright) -> None:
    """
    Test IntraDU inter freq with (Bidi Tput).

    This function launches a Chromium browser instance in non-headless mode,
    creates a new browser context and page.

    Args:
        playwright (Playwright): The Playwright instance to use for launching
                                 the browser and creating the context and page.

    Returns:
        None
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.56.114:8012/login/?next=/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("ortseam@2024")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("link", name=" Test Case Management").click()
    page.locator("#tc_release").select_option("1.0")
    page.locator("#tc_program").select_option("SA_FDD")
    page.locator("#tc_feature").select_option("HO")
    page.get_by_role("textbox", name="Testcase title").click()
    page.get_by_role("textbox", name="Testcase title").fill(
        "IntraDU handover with bidi throughput"
    )
    page.get_by_role("textbox", name="Testcase goal").click()
    page.get_by_role("textbox", name="Testcase goal").fill("handover ")
    page.get_by_role("textbox", name="Testcase title").dblclick()

    page.get_by_role("textbox", name="Testcase goal").click()
    page.get_by_role("textbox", name="Testcase goal").fill(
        "IntraDU inter frequency handover"
    )
    page.get_by_role("textbox", name="Description").click()
    page.get_by_role("textbox", name="Description").fill("ho with throughput")
    page.get_by_role("button", name="Add Details").click()

    page.get_by_placeholder("NR RU").fill("2")
    page.locator("#tc_priority").select_option("P0")

    page.get_by_label("Radio Status").uncheck()
    page.get_by_role("button", name="Attach UE").dblclick()

    page.get_by_role("button", name="Verification").click()
    page.get_by_role("button", name="Verify Attach").dblclick()

    page.get_by_role("button", name="Feature").click()
    page.get_by_role("button", name="Basic Tput", exact=True).click()
    page.get_by_role("button", name="Perform UDP BiDi Tput").dblclick()

    page.get_by_role("button", name="HO", exact=True).click()
    page.get_by_role("button", name="Perform IntraDU InterFreq HO").dblclick()

    page.get_by_role("button", name="Common").click()
    page.get_by_role("button", name="Detach UE").dblclick()

    page.get_by_role("button", name="Verification").click()
    page.get_by_role("button", name="Verify Detach").dblclick()

    page.get_by_role("button", name="Verify IntraDU InterFreq HO").dblclick()

    page.get_by_role("button", name="Verify Tput Bidi").dblclick()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()
    # page.get_by_role("button",name="FinalConfirm").click()

    page.locator("#state_block_div").get_by_role("button", name="Attach UE").click()
    page.get_by_role("button", name="Attach UE").click()
    page.get_by_role("form").locator("#cell_id").click()
    page.get_by_role("form").locator("#cell_id").fill("1")
    page.get_by_role("form").locator("#rsrp").click()
    page.get_by_role("form").locator("#rsrp").fill("85")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()

    page.get_by_role("button", name="Perform UDP BiDi Tput").click()
    page.get_by_role("form").locator("#dl_pkt_length").click()
    page.get_by_role("form").locator("#dl_pkt_length").fill("1400")
    page.get_by_role("form").locator("#dl_tput_duration").click()
    page.get_by_role("form").locator("#dl_tput_duration").fill("300")
    page.get_by_role("form").locator("#dl_bandwidth").click()
    page.get_by_role("form").locator("#dl_bandwidth").fill("20")
    page.get_by_role("form").locator("#ul_tput_duration").click()
    page.get_by_role("form").locator("#ul_tput_duration").fill("1380")
    page.get_by_role("form").locator("#ul_pkt_length").click()
    page.get_by_role("form").locator("#ul_pkt_length").fill("300")
    page.get_by_role("form").locator("#ul_bandwidth").click()
    page.get_by_role("form").locator("#ul_bandwidth").fill("20")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()

    page.get_by_role("button", name="Perform IntraDU InterFreq HO").click()
    page.get_by_role("form").locator("#initial_cell").click()
    page.get_by_role("form").locator("#initial_cell").fill("1")
    page.get_by_role("form").locator("#final_cell").click()
    page.get_by_role("form").locator("#final_cell").fill("2")
    page.get_by_role("textbox", name="db/sec").click()
    page.get_by_role("textbox", name="db/sec").fill("2")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()

    page.locator("#state_block_div").get_by_role("button", name="Detach UE").click()
    page.get_by_role("form").locator("#detach_type").select_option("UE Initiated")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()

    page.get_by_role("button", name="Verify Tput Bidi").click()
    page.get_by_role("form").locator("#ul_tput_file").click()
    page.get_by_role("form").locator("#ul_tput_file").fill("380")
    page.get_by_role("form").locator("#ul_tolerance").click()
    page.get_by_role("form").locator("#ul_tolerance").fill("2")
    page.get_by_role("form").locator("#dl_tput_file").click()
    page.get_by_role("form").locator("#dl_tput_file").fill("75")
    page.get_by_role("form").locator("#dl_tolerance").click()
    page.get_by_role("form").locator("#dl_tolerance").fill("2")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()

    page.get_by_role("button", name="Submit").click()

    # page.get_by_role("link", name=" Test Plan Management").click()
    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.locator("#oneliner45").click()

    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.locator("#smblocks45").click()

    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.locator("#word45").click()

    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.locator("#script45").click()

    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_intradu_interfreq(playwright)
