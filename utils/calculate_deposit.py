from datetime import datetime


class CalculateDeposit:
    def get_deposit(self):
        return self.calculate_fibonachi_number(datetime.now().day + 1)

    from functools import lru_cache

    @lru_cache
    def calculate_fibonachi_number(self, n: int):
        if n <= 3:
            if n == 0:
                return 0
            return 1
        a = self.calculate_fibonachi_number(n - 2) + self.calculate_fibonachi_number(n - 1)
        return a
