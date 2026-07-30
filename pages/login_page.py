from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Add this here
    ERROR_MESSAGE = (
        By.XPATH,
        "//p[contains(@class,'oxd-alert-content-text')]"
    )

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):

        self.enter_text(self.USERNAME, username)

        self.enter_text(self.PASSWORD, password)

        self.click(self.LOGIN_BUTTON)

    # Add this here
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)