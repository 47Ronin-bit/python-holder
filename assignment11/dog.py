from pet import Pet


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    # Overrides Pet.__str__ to add the dog's sound
    def __str__(self):
        return super().__str__() + " says Woof!"