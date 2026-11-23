from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, side):
        # A square is a rectangle whose length and width are equal
        super().__init__(name, side, side)