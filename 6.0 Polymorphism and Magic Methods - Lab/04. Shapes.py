from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return Circle.PI * self.__radius ** 2

    def calculate_perimeter(self):
        return Circle.PI * 2 * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return (self.__width + self.__height) * 2


# --------------------------------------------
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

'''
78.53981633974483
31.41592653589793
200
60
'''
