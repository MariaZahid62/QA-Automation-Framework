from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


def test_open_pim(driver):

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim = PimPage(driver)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    assert dashboard.is_dashboard_displayed()

    pim.open_pim()

    assert pim.is_pim_page_displayed()