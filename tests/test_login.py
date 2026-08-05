from playwright.sync_api import Page

from config import (
    INVALID_PASSWORD,
    LOCKED_OUT_USER,
    PASSWORD,
    STANDARD_USER,
)
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    login_page.verify_successful_login()


def test_invalid_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(STANDARD_USER, INVALID_PASSWORD)
    login_page.verify_error_message(
        "Username and password do not match"
    )


def test_locked_out_user(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(LOCKED_OUT_USER, PASSWORD)
    login_page.verify_error_message(
        "Sorry, this user has been locked out"
    )
