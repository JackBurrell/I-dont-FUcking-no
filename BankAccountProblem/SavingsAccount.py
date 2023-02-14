from BankAccountProblem.BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def withdraw(self, amountToWithdraw2):

        _balanceAfterWithdrawal2 = self._balance - amountToWithdraw2

        if amountToWithdraw2 > 0 and _balanceAfterWithdrawal2 > 150:
            self._balance = _balanceAfterWithdrawal2
            print("Withdrawal completed. Your new balance is " + str(self._balance))
        elif amountToWithdraw2 > 0 and _balanceAfterWithdrawal2 <= 150 and _balanceAfterWithdrawal2 >= 0:
            self._balance = (self._balance - amountToWithdraw2 - 2)
            print(
                "Withdrawal completed. Since you have surpassed the account minimum of $150 a $2 charge was automatically applied. Your new balance is " + str(
                    self._balance))
        elif amountToWithdraw2 > self._balance:
            print("You have tried to withdraw more than you currently have in your account. Please withdraw " + str(
                self._balance) + " or less.")
        else:
            print(self.SAYING1)