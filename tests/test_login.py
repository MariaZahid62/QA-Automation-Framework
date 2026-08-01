from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.logger import Logger


def test_valid_login(driver):

    logger = Logger.get_logger()

    logger.info("Starting Valid Login Test")

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    logger.info("Opening Login Page")

    login.open()

    login.login("Admin", "admin123")

    logger.info("Login Successful")

    assert dashboard.is_dashboard_displayed()

    logger.info("Dashboard Verified")

    logger.info("Valid Login Test Passed")


def test_invalid_login(driver):

    login = LoginPage(driver)

    login.open()

    login.login("Admin", "wrongpassword")

    assert login.get_error_message() == "Invalid credentials"