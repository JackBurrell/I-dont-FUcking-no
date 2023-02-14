

question1 = int(input("Please select the action you would like to complete\n [1] Add a wall\n [2] Calculate paint required\n"))

if question1 == 1:
    name = str(input("What is the wall name?\n"))
    color = str(input("What is the color of the wall?\n"))
    question2if1 = int(input("Please select the type of wall you would like to add\n [1] rectangle\n [2] square\n [3] triangle"))

    if question2if1 == 1:
        length = int(input("What is the wall length?\n"))
        height = int(input("What is the wall height\n"))

        #newWall.rectangleWall(name, color, length, height)
        #add to array using .append??

    elif question2if1 == 2:
        length = int(input("What is the wall length?\n"))

        #newWall.squareWall(name, color, length)
        #add to array  using .append??

    elif question2if1 == 3:
        base = int(input("What is the wall base?\n"))
        height = int(input("What is the wall height\n"))

        #newWall.triangleWall(name, color, base, height)
        #add to array  using .append??

    else:
        print("Please type 1, 2, or 3.")

        # this doesnt feel like a good end point, maybe a place for a loop until 1, 2, or 3 is selected?
        # alternatively how to limit inputs to 1, 2, or 3 in the original input line?

if question1 == 2:
    # for wall in walls sum get area and divide by 400