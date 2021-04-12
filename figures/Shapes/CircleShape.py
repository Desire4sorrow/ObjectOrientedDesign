import Shapes.Point as Point


class CircleShape:
    def __init__(self, centre=Point.Point(), radius=0):
        self.centre = centre
        self.radius = radius

    def get_centre(self):
        return self.centre

    def get_radius(self):
        return self.radius

    def display(self, canvas):
        canvas.create_oval(self.centre.x - self.radius, self.centre.y - self.radius,
                           self.centre.x + self.radius, self.centre.y + self.radius)
