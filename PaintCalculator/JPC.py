from Rectangle_Wall import RectangleWall
from Square_Wall import SquareWall
from Triangle_Wall import TriangleWall
from Wall import Wall


class PaintCalculator:
    walls: list = list()

    def __init__(self):
        self.main()

    def main(self):
        while True:
            userChoice = input("[1] Add a wall [2] Calculate paint required (and Exit) Please choose >>> ")
            if userChoice == "1":
                newWall: Wall = None
# this is a change
                name = input("What's the name of the new wall?")
                color = input("What color is the wall?")
                shapeChoice = input("What kind of wall?" + "\n[1] Rectangle\n[2] Square\n[3] Triangle")
                if shapeChoice == "1":
                    height = int(input("Enter wall height >>> "))
                    length = int(input("Enter wall length >>> "))
                    newWall = RectangleWall(name, color, height, length)
                elif shapeChoice == "2":
                    sideLength: int = int(input("Enter wall side length >>> "))
                    newWall = SquareWall(name, color, sideLength)
                elif shapeChoice == "3":
                    height: int = int(input("Enter wall height >>> "))
                    base: int = int(input("Enter wall base >>> "))
                    newWall = TriangleWall(name, color, height, base)
                print("Added " + newWall.toString() + " wall - "
                      + str(newWall.getArea()) + " square feet")
                self.walls.append(newWall)
            elif userChoice == "2":
                colorChoiceAreas: dict = dict()
                totalArea: int = 0

                i: int = 1
                for wall in self.walls:
                    print("Wall " + str(i) + ": " + wall.toString() + " - " + wall.getArea() + " square ft")
                    totalArea += wall.getArea()
                    colorChoiceAreas.setdefault(wall.getColor(), 0)
                    colorChoiceAreas[wall.getColor()] = colorChoiceAreas.get(wall.getColor()) + wall.getArea()

                print("===============================");
                print("Total Area: " + str(totalArea) + " square feet");

                # 1 gallon of paint covers 400 square feet
                for colorEntry in colorChoiceAreas:
                    gallonsRequiredForColor = colorEntry.getValue() / 400
                    print(colorEntry.getKey() + " Paint Required: " + str(gallonsRequiredForColor) + " gallons")

                return