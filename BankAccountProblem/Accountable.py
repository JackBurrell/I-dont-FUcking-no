import abc
from abc import ABC

class Accountable(ABC):
    _balance = 0

    @abc.abstractmethod
    def getBalance(self):
        return self._balance
