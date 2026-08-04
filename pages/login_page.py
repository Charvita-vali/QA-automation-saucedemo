from playwright.sync_api import Page, expect

from config import BASE_URL, INVENTORY_URL


class LoginPage:
    """Page Object for the SauceDemo login page."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_successful_login(self):
        expect(self.page).to_have_url(INVENTORY_URL)
        expect(self.page.locator(".title")).to_have_text("Products")

    def verify_error_message(self, expected_message: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_message)
