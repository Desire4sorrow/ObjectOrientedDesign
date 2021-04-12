import Shapes.Point as Point


class TriangleShape:
    def __init__(self, point1=Point.Point(),
                 point2=Point.Point(), point3=Point.Point()):

        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.coordinates_list = [point1.x, point1.y, point2.x, point2.y, point3.x, point3.y]

    def get_point1(self):
        return self.point1

    def get_point2(self):
        return self.point2

    def get_point3(self):
        return self.point3

    def get_coordinates(self):
        coordinates = (self.get_point1(), self.get_point2(), self.get_point3())
        return coordinates

    def display(self, canvas):
        coordinates_list = self.coordinates_list[:] + [self.coordinates_list[0]] + [
            self.coordinates_list[1]]
        canvas.create_line(*coordinates_list)
