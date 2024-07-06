import os


def test_login(login_page):
    login_url = os.getenv("LOGIN_URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    # login_page.navigate(login_url)
    login_page.login(login_url, "admin", password)
    assert login_page.is_logged_in(), "User should be logged in"
