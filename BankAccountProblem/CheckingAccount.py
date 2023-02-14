from BankAccountProblem.BankAccount import BankAccount


class CheckingAccount(BankAccount):
    _amountToWithdraw1 = 0

    def withdraw(self, amountToWithdraw1):
        balanceAfterWithdrawal1 = self._balance - amountToWithdraw1
        if amountToWithdraw1 > 0 and balanceAfterWithdrawal1 >= 0:
            self._balance = self._balance - amountToWithdraw1
            print("Withdrawal completed. Your new balance is " + str(self._balance))
        elif amountToWithdraw1 > 0 > balanceAfterWithdrawal1 > -100:
            self._balance = self._balance - amountToWithdraw1 - 10
            print(
                "Withdrawal completed. Since you have overdrawn your account a $10 overdraft fee has been "
                "automatically applied. Your new balance is " + str(self._balance))
        elif amountToWithdraw1 > 0 and balanceAfterWithdrawal1 <= -100:
            print("This withdrawal amount will take you beyond your -$100 minimum. Please try withdrawing less.")
        else:
            print("A withdraw needs to be greater than $0")
    # def withdraw(self):
    #     amountToWithdraw1 = int(input("Amount to withdraw: "))
    #     _balanceAfterWithdrawal1 = self._balance - amountToWithdraw1
    #     if amountToWithdraw1 > 0 and _balanceAfterWithdrawal1 >= 0:
    #         self._balance = self._balance - amountToWithdraw1
    #         print("Withdrawal completed. Your new balance is " + str(self._balance))
    #     elif amountToWithdraw1 > 0 > _balanceAfterWithdrawal1 > -100:
    #         self._balance = self._balance - amountToWithdraw1 - 10
    #         print(
    #             "Withdrawal completed. Since you have overdrawn your account a $10 overdraft fee has been "
    #             "automatically applied. Your new balance is " + str(self._balance))
    #     elif amountToWithdraw1 > 0 and _balanceAfterWithdrawal1 <= -100:
    #         print("This withdrawal amount will take you beyond your -$100 minimum. Please try withdrawing less.")
    #     else:
    #         print(self.SAYING1)
    #
