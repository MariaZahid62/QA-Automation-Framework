from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PimPage(BasePage):

    PIM_MENU = (
        By.XPATH,
        "//span[text()='PIM']"
    )

    HEADER = (
        By.XPATH,
        "//h6[text()='PIM']"
    )

    ADD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Add']"
    )

    EMPLOYEE_NAME_INPUT = (
        By.XPATH,
        "(//input[@placeholder='Type for hints...'])[1]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    EMPLOYEE_RECORD = (
        By.XPATH,
        "//div[@class='oxd-table-body']"
    )

    def open_pim(self):

        self.click(self.PIM_MENU)

    def is_pim_page_displayed(self):

        return self.get_text(self.HEADER) == "PIM"

    def click_add_employee(self):

        self.click(self.ADD_BUTTON)

    def search_employee(self, employee_name):

        self.enter_text(self.EMPLOYEE_NAME_INPUT, employee_name)

        self.click(self.SEARCH_BUTTON)

    def employee_exists(self):

        return self.is_visible(self.EMPLOYEE_RECORD)