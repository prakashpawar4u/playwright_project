import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.56.114:8012/login/?next=/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("ortseam@2024")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("link", name=" Release Management").click()
    page.locator("#release").select_option("1.0")
    page.get_by_text("Program Select Program SA FDD").click()
    page.locator("#program").select_option("SA_FDD")
    page.locator("#feature").select_option("HO")
    page.get_by_placeholder("NR RU").click()
    page.get_by_placeholder("NR RU").click()
    page.get_by_placeholder("NR RU").click()
    page.get_by_placeholder("NR RU").fill("2")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name=" Test Case Management").click()
    page.locator("#tc_release").select_option("1.0")
    page.locator("#tc_program").select_option("SA_FDD")
    page.locator("#tc_feature").select_option("Basic Tput")
    page.locator("#tc_feature").select_option("HO")
    page.get_by_role("textbox", name="Testcase title").click()
    page.get_by_role("textbox", name="Testcase title").fill("Perform")
    page.get_by_role("textbox", name="Testcase goal").click()
    page.get_by_role("textbox", name="Testcase goal").fill("HO")
    page.get_by_role("textbox", name="Description").click()
    page.get_by_role("textbox", name="Description").fill("ho")
    page.get_by_text("Submit Add Details").click()
    page.get_by_role("button", name="Add Details").click()
    page.get_by_placeholder("NR RU").click()
    page.get_by_placeholder("NR RU").click()
    page.get_by_placeholder("NR RU").fill("2")
    page.locator("#tc_details").click()
    page.locator("#tc_priority").select_option("P0")
    page.get_by_role("button", name="Attach UE").click()
    page.get_by_role("button", name="Detach UE").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()


    page.locator("#state_block_div").get_by_role("button", name="Attach UE").click()
    page.get_by_role("form").locator("#cell_id").click()
    page.get_by_role("form").locator("#cell_id").fill("1")
    page.get_by_role("form").locator("#rsrp").click()
    page.get_by_role("form").locator("#rsrp").fill("83")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()
    page.locator("#state_block_div").get_by_role("button", name="Detach UE").click()
    page.get_by_role("form").locator("#detach_type").select_option("UE Initiated")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name=" Test Plan Management").click()
    page.get_by_role("link", name="Perform").click()
    page.get_by_role("button", name="Verification").click()
    page.get_by_role("button", name="Verify IntraDU IntraFreq HO").click()
    page.get_by_role("button", name="Verify Tput Bidi").click()
    page.locator("#state_block_div").get_by_role("button", name="Verify IntraDU IntraFreq HO").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("button", name="Verify Tput Bidi").click()
    page.get_by_role("form").locator("#ul_tput_file").click()
    page.get_by_role("form").locator("#ul_tput_file").fill("5")
    page.get_by_role("form").locator("#ul_tolerance").click()
    page.get_by_role("form").locator("#ul_tolerance").fill("5")
    page.get_by_role("form").locator("#dl_tput_file").fill("5")
    page.get_by_role("form").locator("#dl_tput_file").click()
    page.get_by_role("form").locator("#dl_tput_file").fill("55")
    page.get_by_role("form").locator("#dl_tolerance").click()
    page.get_by_role("form").locator("#dl_tolerance").fill("5")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Add").click()
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name=" Test Plan Management").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#oneliner28").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#script28").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
