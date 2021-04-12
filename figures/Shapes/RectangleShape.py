import Shapes.Point as Point


class RectangleShape:
    def __init__(self, point1=Point.Point(), point2=Point.Point()):
        self.point1 = point1
        self.point2 = point2

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    def display(self, canvas):
        canvas.create_rectangle(self.point1.x, self.point1.y, self.point2.x, self.point2.y)
