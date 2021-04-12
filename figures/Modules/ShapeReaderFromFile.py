import FactoryMethod.CreateTriangle as FactoryMethodTriangle
import FactoryMethod.CreateRectangle as FactoryMethodRectangle
import FactoryMethod.CreateCircle as FactoryMethodCircle


class ShapeReaderFromFile:
    TRIANGLE = 'TRIANGLE'
    RECTANGLE = 'RECTANGLE'
    CIRCLE = 'CIRCLE'

    def __init__(self, input_file_name='input.txt'):
        self.input_file_name = input_file_name
        self.shapes_list = []

    def read_shape_from_file(self):
        with open(self.input_file_name) as input_file:
            for line in input_file:
                data = line.strip().split(':', 1)
                type_shape = data[0]
                information = data[1].strip()
                if type_shape == ShapeReaderFromFile.TRIANGLE:
                    self.shapes_list.append(FactoryMethodTriangle.CreateTriangle.create_triangle(information))

                elif type_shape == ShapeReaderFromFile.RECTANGLE:
                    self.shapes_list.append(FactoryMethodRectangle.CreateRectangle.create_rectangle(information))

                elif type_shape == ShapeReaderFromFile.CIRCLE:
                    self.shapes_list.append(FactoryMethodCircle.CreateCircle.create_circle(information))

                else:
                    raise TypeError('Incorrect shape type!')

        return self.shapes_list
