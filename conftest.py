import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.calculate_deposit import CalculateDeposit
from utils.csv_data_creator import CSVDataCreator
from config import DEFAULT_SOURCE_TRANSACTION_DATA, \
    DEFAULT_NAME_TRANSACTION_DATA, \
    DEFAULT_DATE_FORMAT, \
    DEFAULT_CURRENT_DATE_FORMAT


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Remote(options=options, command_executor="http://192.168.1.64:4444/wd/hub")
    yield driver
    driver.quit()


@pytest.fixture
def get_calculate_deposit():
    return CalculateDeposit()


@pytest.fixture
def get_csv_data_creator():
    return CSVDataCreator(
        DEFAULT_CURRENT_DATE_FORMAT,
        DEFAULT_DATE_FORMAT,
        DEFAULT_SOURCE_TRANSACTION_DATA,
        DEFAULT_NAME_TRANSACTION_DATA
    )
