class InformationAboutPerimeterVisitor:
    def __init__(self):
        self.perimeter = 0

    def visit_triangle(self, decorator_triangle):
        self.perimeter = decorator_triangle.get_perimeter()
        return self.perimeter

    def visit_rectangle(self, decorator_rectangle):
        self.perimeter = decorator_rectangle.get_perimeter()
        return self.perimeter

    def visit_circle(self, decorator_circle):
        self.perimeter = decorator_circle.get_perimeter()
        return self.perimeter
