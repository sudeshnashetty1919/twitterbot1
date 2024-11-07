import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    driver = None

    @staticmethod
    def initialize_web_driver():
        """Initialize WebDriver if it's not already initialized."""
        if BasePage.driver is None:
            try:
                # Initialize the Chrome driver
                BasePage.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                BasePage.driver.maximize_window()
                BasePage.driver.implicitly_wait(60)
                BasePage.driver.get("https://x.com/i/flow/login")  # Add your desired URL here
            except Exception as e:
                print(f"Error initializing WebDriver: {e}")
                raise
        return BasePage.driver

    @staticmethod
    def quit_driver():
        """Quit the WebDriver if it's initialized."""
        if BasePage.driver is not None:
            BasePage.driver.quit()
            BasePage.driver = None


# pytest fixture to initialize and close WebDriver for each test scenario
@pytest.fixture(scope="function")
def driver():
    # Initialize the WebDriver before each test (or scenario)
    driver = BasePage.initialize_web_driver()
    yield driver  # Yield the driver to the test
    # Clean up after test (quit the driver)
    BasePage.quit_driver()
