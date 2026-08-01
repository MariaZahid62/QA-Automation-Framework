from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    EMPLOYEE_LIST = (
    By.XPATH,
    "//div[@class='oxd-table-body']"
    )

    DELETE_BUTTON = (
    By.XPATH,
    "//i[contains(@class,'bi-trash')]"
    )

    CONFIRM_DELETE = (
    By.XPATH,
    "//button[normalize-space()='Yes, Delete']"
    )

    NO_RECORDS_FOUND = (
    By.XPATH,
    "//span[text()='No Records Found']"
)

    def open_pim(self):

        self.click(self.PIM_MENU)

    def is_pim_page_displayed(self):

        return self.get_text(self.HEADER) == "PIM"

    def click_add_employee(self):

        self.click(self.ADD_BUTTON)

    def search_employee(self, employee_name):

       element = self.find(self.EMPLOYEE_NAME_INPUT)
       element.clear()
       element.send_keys(employee_name)

       self.click(self.SEARCH_BUTTON)

    def employee_exists(self):

        return self.is_visible(self.EMPLOYEE_RECORD)

    def delete_employee(self):

        self.click(self.DELETE_BUTTON)

        self.click(self.CONFIRM_DELETE)


    def delete_successful(self):

         toast = self.wait.until(
        EC.visibility_of_element_located(self.SUCCESS_DELETE_TOAST)
        )

         return "Successfully Deleted" in toast.text

    SUCCESS_DELETE_TOAST = (
    By.XPATH,
    "//div[contains(@class,'oxd-toast')]//p[contains(text(),'Successfully Deleted')]"
)

    def no_records_found(self):

     return self.is_visible(self.NO_RECORDS_FOUND)

    def employee_list_visible(self):

     return self.is_visible(self.EMPLOYEE_LIST)