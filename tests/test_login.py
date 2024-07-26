import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.base_page import BasePage
from resources.config import Config
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(browser):
    # Open ParaBank demo website
    browser.get("https://parabank.parasoft.com/parabank/index.jsp")

    # Create an instance of the LoginPage
    login_page = LoginPage(browser)

    # Perform login actions
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_login_button()

    # Print page title and current URL for debugging
    print("Page Title:", browser.title)
    print("Current URL:", browser.current_url)

    # Check if login was successful
    if "Accounts Overview" in browser.title:
        print("Login was successful")
    else:
        print("Login failed")
        # Print the error message from the page
        error_message = browser.find_element(By.CLASS_NAME, "error").text
        print("Error message:", error_message)

    # Verify login was successful
    assert "Accounts Overview" in browser.title, f"Expected 'Accounts Overview' but got '{browser.title}'"
