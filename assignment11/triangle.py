from shape import Shape


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self._base = base
        self._height = height

    # Overrides Shape.get_area
    def get_area(self):
        return 0.5 * self._base * self._height

    def __str__(self):
        return super().__str__() + ", Base: " + str(self._base) + ", Height: " + str(self._height)