from BankAccountProblem.Accountable import Accountable


class CreditCardAccount(Accountable):
    accountHolder = "First Last"
    accountNumber = "132"
    debt = lambda self : (self._balance * -1)

    def getAccountHolder(self):
        return self.accountHolder

    def getAccountNumber(self):
        return self.accountNumber

    def pay(self, amountToPay):
        if 0 < amountToPay <= self.debt:
            self._balance = self._balance + amountToPay
            return self._balance
        else:
            print("Invalid")

    def charge(self, amountToCharge):
        if amountToCharge > 0:
            self._balance = self._balance - amountToCharge
        else:
            print("Invalid")

    def getBalance(self):
        return self._balance
