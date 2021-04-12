import Shapes.TriangleShape as TriangleShape
import Shapes.RectangleShape as RectangleShape
import Shapes.CircleShape as CircleShape

import Decorators.TriangleInDecorator as TriangleInDecorator
import Decorators.CircleInDecorator as CircleInDecorator
import Decorators.RectangleInDecorator as RectangleInDecorator

import Visitor.InformationAboutPerimeterVisitor as InformationAboutPerimeterVisitor
import Visitor.InformationAboutAreaVisitor as InformationAboutAreaVisitor


class ShapeInformationAboutPerimeterAndArea:
    def __init__(self, output_file_name='output.txt'):
        self.output_file_name = output_file_name

    def get_information_about_shapes(self, shapes_list):
        with open(self.output_file_name, 'w') as output_file:
            for shape in shapes_list:
                visitor_perimeter = InformationAboutPerimeterVisitor.InformationAboutPerimeterVisitor()
                visitor_area = InformationAboutAreaVisitor.InformationAboutAreaVisitor()

                if type(shape) == TriangleShape.TriangleShape:
                    type_shape = 'TRIANGLE'
                    perimeter = TriangleInDecorator.TriangleInDecorator(shape).visit(visitor_perimeter)
                    area = TriangleInDecorator.TriangleInDecorator(shape).visit(visitor_area)
                elif type(shape) == RectangleShape.RectangleShape:
                    type_shape = 'RECTANGLE'
                    perimeter = RectangleInDecorator.RectangleInDecorator(shape).visit(visitor_perimeter)
                    area = RectangleInDecorator.RectangleInDecorator(shape).visit(visitor_area)
                elif type(shape) == CircleShape.CircleShape:
                    type_shape = 'CIRCLE'
                    perimeter = CircleInDecorator.CircleInDecorator(shape).visit(visitor_perimeter)
                    area = CircleInDecorator.CircleInDecorator(shape).visit(visitor_area)

                output_file.write(type_shape + ': P=' + str(round(perimeter, 2)) + '; S=' + str(round(area, 2)) + ';\n')
