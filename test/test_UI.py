import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.calculate_deposit import CalculateDeposit
from utils.csv_data_creator import CSVDataCreator
from pages.login_page import LoginPage
from config import BASE_PAGE


class TestTransactions:

    @allure.feature('Open pages')
    @allure.story('Проверка работы транзакций')
    @allure.severity('blocker')
    def test_transactions(self, driver: WebDriver,
                          get_calculate_deposit: CalculateDeposit,
                          get_csv_data_creator: CSVDataCreator):
        deposit = get_calculate_deposit.get_deposit()
        login_page = LoginPage(driver, BASE_PAGE + "/login")
        login_page.open()
        customer_page = login_page.login()
        account_page = customer_page.select_customer()
        deposit_data = account_page.deposit(deposit)
        withdraw_data = account_page.withdraw(deposit)
        assert int(account_page.get_balance()) == 0
        account_page.open_transaction()
        transactions = account_page.get_transactions_data()
        assert deposit_data in transactions and withdraw_data in transactions
        get_csv_data_creator.create_csv_data(transactions)
