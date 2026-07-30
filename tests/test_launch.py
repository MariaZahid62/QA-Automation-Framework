from utilities.driver_factory import DriverFactory


def test_launch_google():

    driver = DriverFactory.get_driver()

    driver.get("https://www.google.com")

    print("Title:", driver.title)

    assert "Google" in driver.title

    driver.quit()