import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.56.114:8012/login/?next=/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("ortseam@2024")
    page.get_by_role("button", name="Sign in").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
