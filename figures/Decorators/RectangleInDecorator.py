import Shapes.RectangleShape as RectangleShape


class RectangleInDecorator:
    def __init__(self, rectangle=RectangleShape.RectangleShape()):
        self.rectangle = rectangle

    def get_perimeter(self):
        point1 = self.rectangle.get_point1()
        point2 = self.rectangle.get_point2()
        perimeter = 2 * (abs(point1.x - point2.x) + abs(point1.y - point2.y))
        return perimeter

    def get_area(self):
        point1 = self.rectangle.get_point1()
        point2 = self.rectangle.get_point2()
        area = abs(point1.x - point2.x) * abs(point1.y - point2.y)
        return area

    def visit(self, visitor):
        number = visitor.visit_rectangle(self)
        return number
