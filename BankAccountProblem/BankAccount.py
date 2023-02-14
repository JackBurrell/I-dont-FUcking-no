from BankAccountProblem.Accountable import Accountable


class BankAccount(Accountable):
    _accountHolderName = "word"
    _accountNumber = 1

    SAYING1 = "A withdraw needs to be greater than $0"
    #    def __init__(self, accountHolderName1, accountNumber1):
    #      self._accountHolderName = accountHolderName1
    #      self._accountNumber = accountNumber1
    #      self._balance = 0

    def __init__(self, accountHolderName2, accountNumber2, balance2):
        self._accountHolderName = accountHolderName2
        self._accountNumber = accountNumber2
        self._balance = balance2

    def deposit(self, amountToDeposit):
        if amountToDeposit > 0:
            self._balance = self._balance + amountToDeposit
            return self._balance
        else:
            print("A deposit needs to be greater than $0")

    def withdraw(self, amountToWithdraw):
        if amountToWithdraw > 0:
            self._balance = self._balance - amountToWithdraw
            return self._balance
        else:
            print(self.SAYING1)

    def getBalance(self):
        return self._balance

    def transferTo(self, destinationAccount, transferAmount):
        account: BankAccount = destinationAccount
        if 0 < transferAmount < self._balance:
            self.withdraw(transferAmount)
            account.deposit(transferAmount)
            account.getBalance()


