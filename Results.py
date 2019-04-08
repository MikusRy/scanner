import Classes

# TODO: Pomyslec co dalej


def extract_rectangles(data, size: dict):


    square_list = []
    for item in data:

        points_temp = []
        for point in item:
            points_temp.append(Classes.Point(point[0], point[1]))

        square_list.append(Classes.Rectangle(points_temp))


def convert(data):
    pass

