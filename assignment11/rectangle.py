from shape import Shape


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self._length = length
        self._width = width

    # Overrides Shape.get_area
    def get_area(self):
        return self._length * self._width

    def __str__(self):
        return super().__str__() + ", Length: " + str(self._length) + ", Width: " + str(self._width)