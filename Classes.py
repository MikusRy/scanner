class Point:
    def __init__(self, x: int, y: int):
        """

        :param x:
        :param y:
        """
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, points: list):
        """

        :param points:
        """
        self.width = 0
        self.height = 0

        self.A = None
        self.B = None
        self.C = None
        self.D = None

        self.assign(points)
        self.measure()

    def assign(self, points: list):
        """

        :param points:
        :return:
        """
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

    def measure(self):
        """

        :return:
        """
        self.width = self.B.x - self.A.x
        self.height = self.D.y - self.A.y

    def contains(self, point: Point) -> bool:
        """

        :param point:
        :return:
        """
        if self.A.x <= point.x <= self.B.x and self.A.y <= point.y <= self.D.y:
            return True
        else:
            return False


class Answer:
    def __init__(self):
        """

        """
        self.A = False
        self.B = False
        self.C = False
        self.D = False
