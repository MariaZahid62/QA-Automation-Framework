from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    USER_DROPDOWN = (
        By.CLASS_NAME,
        "oxd-userdropdown-tab"
    )

    LOGOUT = (
        By.XPATH,
        "//a[text()='Logout']"
    )

    def is_dashboard_displayed(self):
        return (
            self.get_text(self.DASHBOARD_HEADER)
            == "Dashboard"
        )

    def logout(self):

        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT)