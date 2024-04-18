from interfaces.depositable import Depositable
from interfaces.withdrawable import Withdrawable
from interfaces.balance_inquirable import BalanceInquirable


class Account(Depositable, Withdrawable, BalanceInquirable):
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Saldo insuficiente")

    def get_balance(self):
        return self.balance
