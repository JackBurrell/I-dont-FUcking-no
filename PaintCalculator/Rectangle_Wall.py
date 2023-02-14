from PaintCalculator.Wall import Wall

class RectangleWall(Wall):
    _length = 10
    _height = 10

    def __init__(self, wallName, wallColor, wallLength, wallHeight):

        self._name = wallName
        self._color = wallColor
        self._length = wallLength
        self._height = wallHeight

    def getArea(self):

        wallArea = self._length * self._height

        return wallArea

    def toString(self):
        return self._name + (self._length * self._height) + "Rectangle" # can the middle term be typed as a function? something like self.getArea()?
    