class AnchorWay:
    """Stabilises syncance and resolves drift."""

    def __init__(self, strength: float = 1.0):
        self.strength = strength

    def stabilise(self, syncance_value: float):
        return syncance_value / self.strength
