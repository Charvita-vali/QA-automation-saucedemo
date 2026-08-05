# 🚀 QA Automation — SauceDemo (Playwright + Python)

A self-directed UI automation testing project built using **Playwright**, **Python**, and **pytest**. This project automates critical user journeys of the SauceDemo e-commerce application and demonstrates modern UI automation framework design using the **Page Object Model (POM)**.

---

## 🎯 Project Goals

- Practice modern UI automation using Playwright
- Build a maintainable automation framework using Page Object Model (POM)
- Automate critical business workflows
- Reduce duplicated code using reusable pytest fixtures
- Demonstrate automation skills for Junior QA / SDET roles

---

## 🛠 Tech Stack

- Python 3.12
- Playwright
- pytest
- pytest-playwright
- Git & GitHub

---

## 📁 Project Structure

```text
QA-automation-saucedemo/
│
├── README.md
├── config.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_cart_checkout.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
└── .gitignore
```

---

## ✅ Test Coverage

### Login

- Valid Login
- Invalid Password
- Locked Out User

### Cart

- Add Single Item
- Add Multiple Items
- Remove Item

### Checkout

- Complete Checkout Flow
- Required Field Validation

---

## ⚙ Framework Features

- Page Object Model (POM)
- Reusable pytest fixtures
- Shared configuration
- Playwright auto-wait assertions
- Independent test execution
- Headed & Headless execution

---

## ▶ Running the Tests

Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

Run tests

```bash
pytest
```

Run headed

```bash
pytest --headed
```

---

## 💡 Automation Concepts Demonstrated

- UI Automation
- Playwright Locators
- Page Object Model
- pytest Fixtures
- Assertions
- Auto Waiting
- Positive Testing
- Negative Testing
- End-to-End Testing
- Test Organization
- Maintainable Automation Framework

---

## 📊 Project Metrics

| Metric | Value |
|---------|------:|
| Pages Automated | 4 |
| Test Files | 2 |
| Automated Test Cases | 8 |
| Framework Pattern | Page Object Model |
| Test Framework | pytest |
| Automation Tool | Playwright |

---

## 🚀 Future Enhancements

- Cross-browser execution
- Parallel execution
- HTML reports
- Screenshot capture on failures
- GitHub Actions CI/CD
- Data-driven testing

---

## 📌 Note

This project was created for learning and portfolio purposes to demonstrate Playwright UI automation skills using the SauceDemo demo application provided by Sauce Labs.
