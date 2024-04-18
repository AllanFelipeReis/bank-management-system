from .account import Account


class InvestmentAccount(Account):
    def __init__(self, account_id, balance, interest_calculator):
        super().__init__(account_id, balance)
        self.interest_calculator = interest_calculator

    def add_interest(self):
        interest = self.interest_calculator.calculate_interest(
            balance=self.balance)
        self.deposit(interest)
