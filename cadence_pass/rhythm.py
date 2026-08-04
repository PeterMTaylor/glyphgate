class Rhythm:
    """Defines how syncance moves through modules."""

    def __init__(self, pattern: str = "steady"):
        self.pattern = pattern

    def shift(self, new_pattern: str):
        self.pattern = new_pattern
        return self.pattern
