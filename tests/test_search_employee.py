from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


def test_search_employee(driver):

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

    pim.search_employee("Maria")

    assert pim.employee_exists()