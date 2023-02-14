import abc
from abc import ABC

class Wall(ABC):

    _name = "wallname"
    _color = "wallcolor"

    @abc.abstractmethod
    def getArea(self):
        pass

    def getColor(self):
        return self._color

    def getName(self):
        return self._name