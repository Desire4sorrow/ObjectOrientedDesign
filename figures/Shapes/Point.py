import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, second_point):
        point = Point(self.x - second_point.x, self.y - second_point.y)
        return point

    def get_length(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length
