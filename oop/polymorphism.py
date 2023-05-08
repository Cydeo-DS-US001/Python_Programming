from abstraction import Shape, Circle, Square, Rectangle
from class_and_objects import Dog


def display_area_and_perimeter(shape: Shape):
    print(f'The area of {shape.name} is {shape.area()}, and the perimeter is {shape.perimeter()}')


circle = Circle(5)

square = Square(6)

rectangle = Rectangle(10, 20)


display_area_and_perimeter(circle)
display_area_and_perimeter(square)
display_area_and_perimeter(rectangle)

"""
dog1 = Dog("Lessy", "Corgi", "Female", "Small", 1, "Gold and White")
display_area_and_perimeter(dog1)
"""


#display_area_and_perimeter("Cydeo")