from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from pages.add_employee_page import AddEmployeePage
from utilities.data_generator import DataGenerator

def test_add_employee(driver):

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim = PimPage(driver)
    employee = AddEmployeePage(driver)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    assert dashboard.is_dashboard_displayed()

    pim.open_pim()

    assert pim.is_pim_page_displayed()

    pim.click_add_employee()

    employee.add_employee(
    DataGenerator.first_name(),
    DataGenerator.middle_name(),
    DataGenerator.last_name()
)

    assert employee.employee_created()