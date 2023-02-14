from PaintCalculator.Rectangle_Wall import RectangleWall
from PaintCalculator.Square_Wall import SquareWall
from PaintCalculator.Triangle_Wall import TriangleWall
from PaintCalculator.Wall import Wall


class UserInterface():
    wallList = []

    def __init__(self):




        action = int(
            input(
                "Please select the action you would like to complete\n [1] Add a wall\n [2] Calculate paint required\n"))

        if action == 1: # this adds a wall depending on what value is selected next
            name = str(input("What is the wall name?\n"))
            color = str(input("What is the color of the wall?\n"))
            wallType = int(
                input(
                    "Please select the type of wall you would like to add\n [1] rectangle\n [2] square\n [3] triangle"))

            if wallType == 1:
                length = int(input("What is the wall length?\n"))
                height = int(input("What is the wall height\n"))
                self.wallList.append(RectangleWall(name, color, length, height))

                # newWall.rectangleWall(name, color, length, height)
                # add to array using .append??

            elif wallType == 2:
                length = int(input("What is the wall length?\n"))

                self.wallList.append(SquareWall(name, color, length))

                # newWall.squareWall(name, color, length)
                # add to array  using .append??

            elif wallType == 3:
                base = int(input("What is the wall base?\n"))
                height = int(input("What is the wall height\n"))

                self.wallList.append(TriangleWall(name, color, base, height))

                # newWall.triangleWall(name, color, base, height)
                # add to array  using .append??

            else:
                print("Please type 1, 2, or 3.")

                # this doesnt feel like a good end point, maybe a place for a loop until 1, 2, or 3 is selected?
                # alternatively how to limit inputs to 1, 2, or 3 in the original input line?

        if action == 2:
            sumBalance = 0.0
            gallonsNeeded = 0
            for x in self.wallList:

                wall1: Wall = x
                wall1.getArea()
                sumBalance += wall1.getArea()
                gallonsNeeded = sumBalance / 400

            print(gallonsNeeded)


    # for wall in walls sum get area and divide by 400 - need a way to group paints by color


