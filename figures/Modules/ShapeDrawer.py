from tkinter import Canvas, Frame, BOTH


class ShapeDrawer(Frame):
    def __init__(self, shape_reader, shape_info):
        super().__init__()
        self.canvas = Canvas(self)
        self.pack(fill=BOTH, expand=True)

        self.shapes = shape_reader.read_shape_from_file()
        shape_info.get_information_about_shapes(self.shapes)

        for shape in self.shapes:
            shape.display(self.canvas)

        self.canvas.pack(fill=BOTH, expand=True)
