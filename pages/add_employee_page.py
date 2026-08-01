from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddEmployeePage(BasePage):

    FIRST_NAME = (
        By.NAME,
        "firstName"
    )

    MIDDLE_NAME = (
        By.NAME,
        "middleName"
    )

    LAST_NAME = (
        By.NAME,
        "lastName"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    PERSONAL_DETAILS_HEADER = (
        By.XPATH,
        "//h6[text()='Personal Details']"
    )

    def add_employee(self, first_name, middle_name, last_name):

        self.enter_text(self.FIRST_NAME, first_name)

        self.enter_text(self.MIDDLE_NAME, middle_name)

        self.enter_text(self.LAST_NAME, last_name)

        self.click(self.SAVE_BUTTON)

    def employee_created(self):

        return (
            self.get_text(self.PERSONAL_DETAILS_HEADER)
            == "Personal Details"
        )