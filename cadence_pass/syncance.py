class Syncance:
    """A unit of narrative energy flowing through the system."""

    def __init__(self, value: float = 1.0):
        self.value = value

    def amplify(self, factor: float):
        self.value *= factor
        return self.value
