# QA Automation — SauceDemo (Playwright + Python)

Automated test suite for [SauceDemo](https://www.saucedemo.com), built with Playwright and pytest. This automates core scenarios from my companion manual testing project ([qa-portfolio-saucedemo](https://github.com/Charvita-vali/QA-portfolio-saucedemo)).

## Tech Stack
- Python 3.12
- Playwright
- pytest
- pytest-playwright

## Test Coverage

### Login (`test_login.py`)
- Valid login
- Invalid login (wrong password)
- Locked out user

### Cart & Checkout (`test_cart_checkout.py`)
- Add single item to cart
- Add multiple items to cart
- Remove item from product page
- Full checkout flow (cart → checkout → order confirmation)
- Checkout validation — missing Last Name shows error

## How to Run

1. Clone this repo
2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies:
```bash
   pip install pytest playwright pytest-playwright
   playwright install
```
4. Run the tests:
```bash
   pytest --headed
```
   Remove `--headed` to run in headless mode (no visible browser, faster — used for CI/CD).

## Design Notes
- Uses a `pytest` fixture (`logged_in_page`) to handle login setup once, reused across cart/checkout tests — avoids repeating the same steps in every test (DRY principle)
- Tests use Playwright's built-in `expect()` assertions, which auto-wait for elements rather than relying on manual sleeps/timeouts — this makes tests more reliable and less flaky

## Next Steps
- Add CI/CD via GitHub Actions to run this suite automatically on every push
- Introduce Page Object Model as the suite grows
- Add HTML/Allure reporting