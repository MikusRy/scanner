class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, points: list):
        self.A = None
        self.B = None
        self.C = None
        self.D = None

        self.assign(points)

    def assign(self, points: list):
        temp = []
        for item in points:
            temp.append(Point(item[0], item[1]))

        if temp[0].y < temp[1].y:
            self.A = temp[0]
            self.D = temp[1]
        else:
            self.A = temp[1]
            self.D = temp[0]

        if temp[2].y < temp[3].y:
            self.B = temp[2]
            self.C = temp[3]
        else:
            self.B = temp[3]
            self.C = temp[2]


class Answer:
    def __init__(self):
        self.A = False
        self.B = False
        self.C = False
        self.D = False
