from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_logout(driver):

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()

    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_displayed()

    dashboard.logout()

    assert "login" in driver.current_url.lower()