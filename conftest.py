import pytest
from utilities.driver_factory import DriverFactory
from utilities.logger import Logger


@pytest.fixture
def driver():

    logger = Logger.get_logger()

    logger.info("Launching Chrome Browser")

    driver = DriverFactory.get_driver()

    yield driver

    logger.info("Closing Browser")

    driver.quit()
    
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            driver.save_screenshot(
                f"screenshots/{item.name}.png"
            )    