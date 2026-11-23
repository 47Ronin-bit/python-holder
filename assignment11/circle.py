import math
from shape import Shape


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    # Overrides Shape.get_area
    def get_area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return super().__str__() + ", Radius: " + str(self._radius)