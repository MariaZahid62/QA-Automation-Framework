from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.excel_reader import ExcelReader


def test_login_using_excel(driver):

    username, password = ExcelReader.read_login_data(
        "test_data/login_data.xlsx"
    )

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()

    login.login(username, password)

    assert dashboard.is_dashboard_displayed()