import os
from dotenv import load_dotenv

load_dotenv()

BASE_PAGE = os.environ.get("BASE_PAGE_URL")
USER_NAME = os.environ.get("USER_NAME")
DEFAULT_CURRENT_DATE_FORMAT = "%b %d, %Y %I:%M:%S %p"
DEFAULT_DATE_FORMAT = "%d %b %Y %I:%M:%S"
DEFAULT_SOURCE_TRANSACTION_DATA = "transaction_data.csv"
DEFAULT_NAME_TRANSACTION_DATA = "transaction_data"
