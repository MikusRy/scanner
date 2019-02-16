"""File containing all important classes"""


class Point:
    def __init__(self, coords: list):
        self.x = coords[0]
        self.y = coords[1]


class Rectangle:
    def __init__(self, points: list):
        self.points = points


class Columns:
    def __init__(self, rectangles: list):
        self.rectangles = rectangles


def get_second(val):
    return val[0][1]


def fix_values(ToFix: list):
    Fixed = []


def get_min_max():
    if temp_min == 0:
        temp_min = item[0][0]
        temp_max = item[0][0]
        print("min : " + temp_min + " max : " + temp_max)
    elif temp_min > item[0][0]:
        temp_min = item[0][0]
        print("min : " + temp_min + " max : " + temp_max)
    elif temp_max < item[0][0]:
        temp_max = item[0][0]
        print("min : " + temp_min + " max : " + temp_max)

def normalize(answers: list):
    normalized = []
    answers.sort()

    # temporary values for min and max values
    temp_min = 0
    temp = []

    for item in answers:
        if temp_min == 0:
            temp_min = item[0][0]
            temp.append(item)
        else:
            if temp_min + 10 > item[0][0]:
                temp.append(item)
            else:
                temp_min = 0

                normalized.append(temp.copy())




