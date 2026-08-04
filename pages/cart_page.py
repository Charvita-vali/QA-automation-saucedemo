from playwright.sync_api import Page, expect

from config import CART_URL, CHECKOUT_STEP_ONE_URL


class CartPage:
    """Page Object for the SauceDemo cart page."""

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.backpack_item = page.locator(
            "[data-test='inventory-item-name']",
            has_text="Sauce Labs Backpack",
        )

    def verify_cart_page(self):
        expect(self.page).to_have_url(CART_URL)

    def verify_backpack_is_present(self):
        expect(self.backpack_item).to_be_visible()

    def proceed_to_checkout(self):
        self.checkout_button.click()
        expect(self.page).to_have_url(CHECKOUT_STEP_ONE_URL)
