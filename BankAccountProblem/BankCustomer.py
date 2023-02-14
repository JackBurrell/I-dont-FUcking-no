from BankAccountProblem import BankAccount


class BankCustomer:
    name = "First Last"
    address = "1 west street"
    phoneNumber = "132"
    accountList = []
    sumBalance = 0
    isVip = lambda self : True if self.sumBalance > 25000 else False
    
    def __init__(self, name, address, phoneNumber):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    def getSumBalance(self):
        return self.sumBalance
        
    def addAccount(self, account: BankAccount):
        self.accountList.append(account)

    def sumAccounts(self):
        sumBalance = 0
        for x in self.accountList:
            v: BankAccount = x
            v.getBalance()
            sumBalance += v.getBalance()
            self.sumBalance = sumBalance
        return self.sumBalance

