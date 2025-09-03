import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="function")
def driver():
    selenoid_url = os.getenv("SELENOID_URL")
    
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if selenoid_url:
        # Selenoid remote driver
        options.set_capability("browserName", "chrome")
        options.set_capability("selenoid:options", {"enableVNC": True})
        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        # Local Chrome driver (for Mac M1)
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
