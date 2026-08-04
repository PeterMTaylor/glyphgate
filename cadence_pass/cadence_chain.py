from .cadence_pass import CadencePass
from .syncance import Syncance

class CadenceChain:
    """Runs syncance through a sequence of cadence passes."""

    def __init__(self, passes: list[CadencePass]):
        self.passes = passes

    def run(self, syncance: Syncance):
        """Apply each cadence pass in order."""
        current = syncance
        for p in self.passes:
            value = p.apply(current)
            current = Syncance(value)
        return current.value
