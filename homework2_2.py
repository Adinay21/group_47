class Figure:
    def __init__(self):
        unit = 'sm'

    def calculate_area(self):
        print('calculating area')

    def info(self):
        print('information about the figure')

class Square(Figure):
    def __init__(self, __side_length):
        super().__init__()
        self.__side_length = __side_length

    def calculate_area(self):
        return (self.__side_length * self.__side_length)

    def info(self):
        return print(f'side length: {self.__side_length}, area: {self.calculate_area()}')

class Rectangle(Figure):
    def __init__(self, __width, __height):
        super().__init__()
        self.__width = __width
        self.__height = __height

    def calculate_area(self):
        return (self.__width * self.__height)

    def info(self):
        return print(f'width: {self.__width}, height: {self.__height}, area: {self.calculate_area()}')

square_1 = Square(5)
square_2 = Square(10)
rectangle_1 = Rectangle(3, 7)
rectangle_2 = Rectangle(6, 11)
rectangle_3 = Rectangle(8, 12)
figures = [square_1, square_2, rectangle_1, rectangle_2, rectangle_3]

for fig in figures:
    fig.info()
