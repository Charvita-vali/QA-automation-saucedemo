from playwright.sync_api import Page, expect

def test_add_single_item_to_cart(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")

    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")


def test_add_multiple_items_to_cart(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bike-light")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")

    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("3")


def test_remove_item_from_product_page(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.click("#remove-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)


def test_full_checkout_flow(logged_in_page: Page):
    page = logged_in_page

    # Add an item and go to cart
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    # Proceed to checkout
    page.click("#checkout")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    # Fill in checkout info
    page.fill("#first-name", "Charvita")
    page.fill("#last-name", "Vali")
    page.fill("#postal-code", "33496")
    page.click("#continue")

    # Verify overview page and finish order
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    page.click("#finish")

    # Verify order confirmation
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")


def test_checkout_missing_last_name_shows_error(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    page.fill("#first-name", "Charvita")
    page.fill("#postal-code", "33496")
    page.click("#continue")

    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Last Name is required")
