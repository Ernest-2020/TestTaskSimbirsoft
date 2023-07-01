from typing import Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def fill_field(self, locator: Tuple[str, str], value: str, timeout: int = 10):
        return self.find_element(locator, timeout).send_keys(value)

    def click_element(self, locator, timeout=10):
        return self.find_element(locator, timeout).click()

    def wait_until_element_to_be_clickable(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: Tuple[str, str], time: int = 10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}")
