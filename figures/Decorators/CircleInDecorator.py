import math
import Shapes.CircleShape as CircleShape


class CircleInDecorator:
    def __init__(self, circle=CircleShape.CircleShape()):
        self.circle = circle

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.circle.get_radius()
        return perimeter

    def get_area(self):
        area = math.pi * self.circle.get_radius() ** 2
        return area

    def visit(self, visitor):
        number = visitor.visit_circle(self)
        return number
