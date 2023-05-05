import math
from numbers import Number
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> Number:
        pass

    @abstractmethod
    def perimeter(self) -> Number:
        pass

    def __str__(self):
        return f'{self.name}{self.__dict__}'


class Square(Shape):

    def __init__(self, side: Number):
        super().__init__()
        self.side = side

    def area(self) -> Number:
        return self.side * self.side

    def perimeter(self) -> Number:
        return 4 * self.side


class Circle(Shape):

    def __init__(self, radius: Number):
        super().__init__()
        self.radius = radius

    def area(self) -> Number:
        return self.radius ** 2 * math.pi

    def perimeter(self) -> Number:
        return 2 * self.radius * math.pi


class Rectangle(Shape):

    def __init__(self, width: Number, length: Number):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> Number:
        return self.length * self.width

    def perimeter(self) -> Number:
        return (self.width + self.length) * 2