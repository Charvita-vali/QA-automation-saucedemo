from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_add_single_item_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack()
    inventory_page.verify_cart_count("1")


def test_add_multiple_items_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    inventory_page.add_bolt_tshirt()
    inventory_page.verify_cart_count("3")


def test_remove_item_from_product_page(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack()
    inventory_page.verify_cart_count("1")

    inventory_page.remove_backpack()
    inventory_page.verify_cart_badge_removed()


def test_full_checkout_flow(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack()
    inventory_page.open_cart()

    cart_page.verify_cart_page()
    cart_page.verify_backpack_is_present()
    cart_page.proceed_to_checkout()

    checkout_page.enter_checkout_information(
        first_name="Charvita",
        last_name="Vali",
        postal_code="33496",
    )
    checkout_page.continue_to_overview()
    checkout_page.finish_order()
    checkout_page.verify_order_confirmation()


def test_checkout_missing_last_name_shows_error(
    logged_in_page: Page,
):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack()
    inventory_page.open_cart()

    cart_page.proceed_to_checkout()

    checkout_page.enter_checkout_information(
        first_name="Charvita",
        last_name="",
        postal_code="33496",
    )
    checkout_page.continue_button.click()
    checkout_page.verify_error_message(
        "Last Name is required"
    )
