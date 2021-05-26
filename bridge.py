class GeometricFigure:
    def DrawingFigure(self, color):
        pass

class Square(GeometricFigure):
    def DrawingFigure(self, color):
        print('Нарисован {} квадрат'.format(color))

class Circle(GeometricFigure):
    def DrawingFigure(self, color):
        print('Нарисован {} круг'.format(color))

class ColorFigure:
    def GetColor(self):
        pass

class ColorGeometricFigure(ColorFigure):
    def __init__(self, color, Figure):
        self.__color = color
        self.__figure = Figure

    def GetColor(self):
        self.__figure.DrawingFigure(self.__color)


draw = ColorGeometricFigure('красный', Square())
draw.GetColor()

draw = ColorGeometricFigure('синий', Square())
draw.GetColor()

draw = ColorGeometricFigure('зеленый', Circle())
draw.GetColor()

draw = ColorGeometricFigure('зеленый', Circle())
draw.GetColor()
