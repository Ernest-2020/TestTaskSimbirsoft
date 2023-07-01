import csv
from datetime import datetime

import allure


class CSVDataCreator:

    def __init__(self,
                 current_date_format: str,
                 date_format: str,
                 source_transaction_data: str,
                 name_transaction_data: str):
        self.current_date_format = current_date_format
        self.date_format = date_format
        self.source_transaction_data = source_transaction_data
        self.name_transaction_data = name_transaction_data

    def create_csv_data(self, data: list):
        headlines = ["Дата-времяТранзакции", "Сумма", "ТипТранзакции"]
        with open(self.source_transaction_data, "w", encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(headlines)
            for transaction in data:
                date = datetime.strptime(transaction["date"], self.current_date_format).strftime(self.date_format)
                amount = int(transaction["amount"])
                type_transaction = transaction["type"]
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow(
                    (
                        date,
                        amount,
                        type_transaction
                    )
                )
        allure.attach.file(source=self.source_transaction_data,
                           attachment_type=allure.attachment_type.CSV,
                           name=self.name_transaction_data)
