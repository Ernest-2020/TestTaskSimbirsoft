from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.customer_page import CustomerPage
from config import BASE_PAGE


class LoginPage(BasePage):
    _CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Customer Login']")

    def login(self):
        self.wait_until_element_to_be_clickable(self._CUSTOMER_LOGIN_BUTTON).click()
        return CustomerPage(self.driver, BASE_PAGE + "/customer")
