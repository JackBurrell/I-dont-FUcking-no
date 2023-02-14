from PaintCalculator.Wall import Wall


class TriangleWall(Wall):

    _base = 0
    _height = 0
    walls = []

    def __init__(self, wallName, wallColor, wallBase, wallHeight):

        self._name = wallName
        self._color = wallColor
        self._base = wallBase
        self._height = wallHeight

    def getArea(self):

        wallArea = (self._base * self._height)/2

        return wallArea

    def toString(self):
        return self._name + ((self._base * self._height)/2) + "Triangle"

    def addWall(self):
        TriangleWall("name1", "color1", 5, 5), TriangleWall("name2", "color2", 10, 10)