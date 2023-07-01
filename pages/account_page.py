from datetime import datetime

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    _BUTTON_DEPOSIT = (By.XPATH, "//button[@ng-click='deposit()']")
    _BUTTON_WITHDRAWN = (By.XPATH, "//button[@ng-click='withdrawl()']")
    _BUTTON_TRANSACTION = (By.XPATH, "//button[@ng-click='transactions()']")
    _BUTTON_MAKE_DEPOSIT = (By.XPATH, "//button[text()='Deposit']")
    _BUTTON_MAKE_WITHDRAWN = (By.XPATH, "//button[text()='Withdraw']")
    _INPUT_DEPOSIT = (By.XPATH, "//form[@ng-submit='deposit()']/div/input")
    _INPUT_WITHDRAWN = (By.XPATH, "//form[@ng-submit='withdrawl()']/div/input")
    _SPAN_DEPOSIT_SUCCESSFUL = (By.XPATH, "//span[text()='Deposit Successful']")
    _SPAN_TRANSACTION_SUCCESSFUL = (By.XPATH, "//span[text()='Transaction successful']")
    _STRONG_BALANCE = (By.XPATH, "//strong[2]")
    _TR_TRANSACTIONS_BASE = "//tr[contains(@id, 'anchor')]/"
    _TR_TRANSACTIONS_DATE = (By.XPATH, f"{_TR_TRANSACTIONS_BASE}td[1]")
    _TR_TRANSACTIONS_AMOUNT = (By.XPATH, f"{_TR_TRANSACTIONS_BASE}td[2]")
    _TR_TRANSACTIONS_TYPE = (By.XPATH, f"{_TR_TRANSACTIONS_BASE}td[3]")
    _INPUT_CALENDAR_START = (By.XPATH, "//input[@id='start']")
    _DATE_FORMAT = "%b %d, %Y %I:%M:%S %p"

    def deposit(self, amount_deposit: str):
        self.wait_until_element_to_be_clickable(self._BUTTON_DEPOSIT).click()
        self.fill_field(self._INPUT_DEPOSIT, amount_deposit)
        self.click_element(self._BUTTON_MAKE_DEPOSIT)
        date = datetime.now().strftime(self._DATE_FORMAT)
        self.find_element(self._SPAN_DEPOSIT_SUCCESSFUL)
        transaction_data = {"date": date, "amount": str(amount_deposit), "type": "Credit"}
        return transaction_data

    def withdraw(self, amount_withdraw: str):
        self.wait_until_element_to_be_clickable(self._BUTTON_WITHDRAWN).click()
        self.fill_field(self._INPUT_WITHDRAWN, amount_withdraw)
        self.click_element(self._BUTTON_MAKE_WITHDRAWN)
        date = datetime.now().strftime(self._DATE_FORMAT)
        self.find_element(self._SPAN_TRANSACTION_SUCCESSFUL)
        transaction_data = {"date": date, "amount": str(amount_withdraw), "type": "Debit"}
        return transaction_data

    def get_balance(self):
        return self.find_element(self._STRONG_BALANCE).text

    def open_transaction(self):
        self.wait_until_element_to_be_clickable(self._BUTTON_TRANSACTION).click()

    def get_transactions_data(self):
        self.wait_until_element_to_be_clickable(self._INPUT_CALENDAR_START)
        self.driver.refresh()
        transactions_date = self.find_elements(self._TR_TRANSACTIONS_DATE)
        transactions_amount = self.find_elements(self._TR_TRANSACTIONS_AMOUNT)
        transactions_type = self.find_elements(self._TR_TRANSACTIONS_TYPE)
        transactions_data = []
        for i in range(len(transactions_date)):
            date = datetime.strptime(transactions_date[i].text, self._DATE_FORMAT).strftime(self._DATE_FORMAT)
            transactions_data.append({"date": date,
                                      "amount": transactions_amount[i].text,
                                      "type": transactions_type[i].text
                                      })
        return transactions_data
