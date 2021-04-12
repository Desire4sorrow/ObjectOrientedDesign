import re
import Shapes.TriangleShape as TriangleShape
import Shapes.Point as Point


class CreateTriangle:
    def __init__(self):
        #singleton
        raise ValueError('You cannot create more than 1 instance')

    @staticmethod
    def create_triangle(information):
        matches = re.match(r'P1=(.\d*),(.\d*); '
                           r'P2=(.\d*),(.\d*); '
                           r'P3=(.\d*),(.\d*)',
                           information, re.M | re.I)
        groups = list(map(int, matches.groups()))
        triangle = TriangleShape.TriangleShape(
                Point.Point(groups[0], groups[1]),
                Point.Point(groups[2], groups[3]),
                Point.Point(groups[4], groups[5]),
        )

        return triangle
