from pet import Pet


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name)

    # Overrides Pet.__str__ to add the bird's sound
    def __str__(self):
        return super().__str__() + " says Tweet!"