def test_launch_google(driver):

    driver.get("https://www.google.com")

    assert "Google" in driver.title