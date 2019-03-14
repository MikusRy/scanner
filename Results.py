import Classes

# TODO: Pomyslec co dalej
def convert(rectangles):

    square_list = []
    for item in rectangles:

        points_temp = []
        for point in item:
            points_temp.append(Classes.Point(point[0], point[1]))

        square_list.append(Classes.Rectangle(points_temp))
