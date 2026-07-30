from utilities.driver_factory import DriverFactory
from pages.login_page import LoginPage


def test_valid_login():

    driver = DriverFactory.get_driver()

    login = LoginPage(driver)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    assert "dashboard" in driver.current_url.lower()

    driver.quit()