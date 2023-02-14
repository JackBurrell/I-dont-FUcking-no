from unittest import TestCase

from BankAccountProblem.CheckingAccount import CheckingAccount
from BankAccountProblem.SavingsAccount import SavingsAccount


class TestBankAccount(TestCase):
    def test_transfer_to_normal(self):
        checking = CheckingAccount("jack", 123, 500)
        savings = SavingsAccount("jack", 321, 500)
        checking1 = checking
        checking1.transferTo(savings, 100)
        if checking.getBalance() == 400 and savings.getBalance() == 600:
            pass

        else:
            self.fail()

