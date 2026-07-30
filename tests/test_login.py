from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(driver):

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_displayed()


def test_invalid_login(driver):

    login = LoginPage(driver)

    login.open()
    login.login("Admin", "wrongpassword")

    assert "dashboard" not in driver.current_url.lower()