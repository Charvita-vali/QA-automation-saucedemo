from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # Navigate to SauceDemo
    page.goto("https://www.saucedemo.com")

    # Fill in valid credentials
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    # Click login
    page.click("#login-button")

    # Assert we landed on the Products page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")

    # Assert error message is shown
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")


def test_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Sorry, this user has been locked out")