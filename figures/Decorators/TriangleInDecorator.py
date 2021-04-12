import Shapes.TriangleShape as TriangleShape


class TriangleInDecorator:
    def __init__(self, triangle=TriangleShape.TriangleShape()):
        self.triangle = triangle

    def get_perimeter(self):
        a, b, c = self.triangle.get_coordinates()
        perimeter = (a-b).get_length() + (b-c).get_length() + (c-a).get_length()
        return perimeter

    def get_area(self):
        a, b, c = self.triangle.get_coordinates()
        area = abs((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y-a.y)) / 2
        return area

    def visit(self, visitor):
        number = visitor.visit_triangle(self)
        return number
