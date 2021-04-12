class InformationAboutAreaVisitor:
    def __init__(self):
        self.area = 0

    def visit_triangle(self, decorator_triangle):
        self.area = decorator_triangle.get_area()
        return self.area

    def visit_rectangle(self, decorator_rectangle):
        self.area = decorator_rectangle.get_area()
        return self.area

    def visit_circle(self, decorator_circle):
        self.area = decorator_circle.get_area()
        return self.area
