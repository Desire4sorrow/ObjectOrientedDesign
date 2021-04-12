from tkinter import Tk
from Modules.ShapeReaderFromFile import ShapeReaderFromFile
from Modules.ShapeInformationAboutPerimeterAndArea import ShapeInformationAboutPerimeterAndArea
from Modules.ShapeDrawer import ShapeDrawer


class MainProgram:
    def __init__(self, width=600, height=600):
        root = Tk()
        root.title('Фигуры')
        root.geometry(str(width) + 'x' + str(height))

        shape_read = ShapeReaderFromFile()
        shape_information = ShapeInformationAboutPerimeterAndArea()
        ShapeDrawer(shape_read, shape_information)

        root.mainloop()


if __name__ == '__main__':
    MainProgram()
