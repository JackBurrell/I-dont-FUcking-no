from PaintCalculator.Rectangle_Wall import RectangleWall


class SquareWall(RectangleWall):

    def __init__(self, wallName, wallColor, wallLength):

        self._name = wallName
        self._color = wallColor
        self._length = wallLength
        self._height = wallLength # I have added this for the getArea function to work correctly when inherited from the Rectangle_Wall class

    def toString(self):
        return self._name + (self._length ** 2) + "Rectangle"