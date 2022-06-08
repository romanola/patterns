# Daniil Selivanov

from __future__ import annotations
from abc import ABC, abstractmethod


class Customer():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_business_logic(self, amount: int) -> None:
        print("Making payment")
        result = self._strategy.make_bank_account_payment(amount)


class Strategy(ABC):

    @abstractmethod
    def make_bank_account_payment(self, amount: int):
        pass


class BankAccountStrategy(Strategy):
    def make_bank_account_payment(self, amount: int) -> None:
        print(f"Payment of {amount} made from bank account.")


class PayPalStrategy(Strategy):
    def make_bank_account_payment(self, amount: int) -> None:
        print(f"Payment of {amount} made from pay pal.")


class GooglePayStrategy(Strategy):
    def make_bank_account_payment(self, amount: int) -> None:
        print(f"Payment of {amount} made from google pay.")


if __name__ == "__main__":

    customer = Customer(BankAccountStrategy())
    print("Client: Strategy is set to BankAccount.")
    customer.do_business_logic(100)
    print()

    print("Client: Strategy is set to PayPal.")
    customer.strategy = PayPalStrategy()
    customer.do_business_logic(200)
    print()

    print("Client: Strategy is set to GooglePay.")
    customer.strategy = GooglePayStrategy()
    customer.do_business_logic(500)
