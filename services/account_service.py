from transactions.deposit import Deposit
from transactions.withdrawal import Withdrawal


class AccountService:
    def __init__(self, account):
        self.account = account

    def process_transaction(self, transaction):
        if isinstance(transaction, Deposit):
            self.account.deposit(transaction.amount)

        elif isinstance(transaction, Withdrawal):
            self.account.withdraw(transaction.amount)
