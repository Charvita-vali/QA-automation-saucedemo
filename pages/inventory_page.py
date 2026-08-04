from playwright.sync_api import Page, expect


class InventoryPage:
    """Page Object for the SauceDemo inventory page."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_backpack(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        ).click()

    def add_bike_light(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-bike-light']"
        ).click()

    def add_bolt_tshirt(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
        ).click()

    def remove_backpack(self):
        self.page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        ).click()

    def open_cart(self):
        self.cart_link.click()

    def verify_cart_count(self, expected_count: str):
        expect(self.cart_badge).to_have_text(expected_count)

    def verify_cart_badge_removed(self):
        expect(self.cart_badge).to_have_count(0)
