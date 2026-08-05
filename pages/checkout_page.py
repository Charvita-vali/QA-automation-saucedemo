from playwright.sync_api import Page, expect

from config import (
    CHECKOUT_COMPLETE_URL,
    CHECKOUT_STEP_TWO_URL,
)


class CheckoutPage:
    """Page Object for SauceDemo checkout pages."""

    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.error_message = page.locator("[data-test='error']")
        self.complete_header = page.locator(".complete-header")

    def enter_checkout_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()
        expect(self.page).to_have_url(CHECKOUT_STEP_TWO_URL)

    def finish_order(self):
        self.finish_button.click()
        expect(self.page).to_have_url(CHECKOUT_COMPLETE_URL)

    def verify_order_confirmation(self):
        expect(self.complete_header).to_have_text(
            "Thank you for your order!"
        )

    def verify_error_message(self, expected_message: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_message)
