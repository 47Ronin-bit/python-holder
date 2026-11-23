class Shape:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    # Overridden by each subclass
    def get_area(self):
        return 0.0

    def __str__(self):
        return "Name: " + self._name