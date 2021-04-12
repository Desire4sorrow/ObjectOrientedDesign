import re
import Shapes.RectangleShape as RectangleShape
import Shapes.Point as Point


class CreateRectangle:
    def __init__(self):
        #singleton
        raise ValueError('You cannot create more than 1 instance')

    @staticmethod
    def create_rectangle(information):
        matches = re.match(r'P1=(.\d*),(.\d*); '
                           r'P2=(.\d*),(.\d*)',
                           information, re.M | re.I)
        groups = list(map(int, matches.groups()))
        rectangle = RectangleShape.RectangleShape(
                Point.Point(groups[0], groups[1]),
                Point.Point(groups[2], groups[3])
        )

        return rectangle
