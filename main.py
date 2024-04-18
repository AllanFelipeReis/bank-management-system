from bank_accounts.investment_account import InvestmentAccount
from bank_accounts.account import Account
from bank_accounts.interest.simple_interest_calculator import SimpleInterestCalculator
from services.account_service import AccountService
from transactions.deposit import Deposit
from transactions.withdrawal import Withdrawal


def main():
    # Criando contas Bancárias
    account1 = Account(account_id=1, balance=1000)
    investment_account1 = InvestmentAccount(
        account_id=2, balance=5000, interest_calculator=SimpleInterestCalculator())

    # Criando uma instância do AccountService
    account_service1 = AccountService(account1)

    # Realizando algumas transações
    account_service1.process_transaction(Deposit(500))
    account_service1.process_transaction(Withdrawal(200))
    investment_account1.add_interest()

    # Exibindo Saldo das Contas
    print("Saldo da Conta Bancária 1: ", account1.get_balance())
    print("Saldo da Conta de Investimento 1: ",
          investment_account1.get_balance())


if __name__ == "__main__":
    main()
