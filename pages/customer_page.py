from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage
from config import BASE_PAGE, USER_NAME


class CustomerPage(BasePage):
    _SELECT_CUSTOMER = (By.XPATH, "//select[@id='userSelect']")
    _CUSTOMER = (By.XPATH, f"//option[text()='{USER_NAME}']")
    _BUTTON_LOGIN = (By.XPATH, "//button[text()='Login']")

    def select_customer(self):
        self.wait_until_element_to_be_clickable(self._SELECT_CUSTOMER).click()
        self.wait_until_element_to_be_clickable(self._CUSTOMER).click()
        self.click_element(self._BUTTON_LOGIN)
        return AccountPage(self.driver, BASE_PAGE + "/account")
