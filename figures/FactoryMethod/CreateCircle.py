import re
import Shapes.CircleShape as CircleShape
import Shapes.Point as Point


class CreateCircle:
    def __init__(self):
        # singleton
        ('You cannot create more than 1 instance')

    @staticmethod
    def create_circle(information):
        matches = re.match(r'C=(.\d*),(.\d*); '
                           r'R=(.\d*)', information,
                           re.M | re.I)
        groups = list(map(int, matches.groups()))
        circle = CircleShape.CircleShape(
                Point.Point(groups[0], groups[1]),
                groups[2])

        return circle
