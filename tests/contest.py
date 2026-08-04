import pytest
from playwright.sync_api import Page, expect

from config import BASE_URL, INVENTORY_URL, PASSWORD, STANDARD_USER


@pytest.fixture
def logged_in_page(page: Page):
    """Log in before each test that uses this fixture."""
    page.goto(BASE_URL)

    page.fill("[data-test='username']", STANDARD_USER)
    page.fill("[data-test='password']", PASSWORD)
    page.click("[data-test='login-button']")

    expect(page).to_have_url(INVENTORY_URL)

    return page
