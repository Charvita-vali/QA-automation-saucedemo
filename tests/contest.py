import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def logged_in_page(page: Page):
    """Log in before each test that uses this fixture."""
    page.goto("https://www.saucedemo.com")
    page.fill("[data-test='username']", "standard_user")
    page.fill("[data-test='password']", "secret_sauce")
    page.click("[data-test='login-button']")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    return page
