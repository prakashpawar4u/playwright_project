import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_features(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.56.114:8012/login/?next=/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Username").press("Enter")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("ortseam@2024")
    page.get_by_role("button", name="Sign in").click()
    page.locator("#release").select_option("1.0")
    page.locator("#program").select_option("SA_FDD")
    page.get_by_role("link", name=" Release Management").click()
    page.locator("#release").select_option("1.0")
    page.locator("#program").select_option("SA_FDD")
    page.locator("#feature").select_option("Basic Tput")
    page.get_by_placeholder("NR RU").click()
    page.get_by_placeholder("NR RU").fill("2")
    page.locator("#ue").select_option("Wired UE")
    page.get_by_role("button", name="Submit").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_add_features(playwright)
