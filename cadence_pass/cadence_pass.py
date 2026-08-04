from .syncance import Syncance
from .rhythm import Rhythm
from .anchor_way import AnchorWay

class CadencePass:
    """A single transformation step in the cadence engine."""

    def __init__(self, rhythm: Rhythm, anchor: AnchorWay):
        self.rhythm = rhythm
        self.anchor = anchor

    def apply(self, syncance: Syncance):
        """Transform syncance based on rhythm and anchor-way."""
        # Minimal behaviour: amplify based on rhythm pattern length,
        # then stabilise using anchor-way.
        factor = len(self.rhythm.pattern)
        amplified = syncance.amplify(factor)
        stabilised = self.anchor.stabilise(amplified)
        return stabilised
