from loader.module_loader import GlyphgateConfig
from .cadence_pass import CadencePass
from .rhythm import Rhythm
from .anchor_way import AnchorWay

class PipelineBuilder:
    """Constructs cadence pipelines from glyphgate.toml."""

    def __init__(self, config: GlyphgateConfig):
        self.config = config

    def build(self):
        cadence_cfg = self.config.data.get("cadence", {})
        pipeline_cfg = cadence_cfg.get("pipeline", {})

        rhythm = Rhythm(cadence_cfg.get("default_rhythm", "steady"))
        anchor_strength = cadence_cfg.get("default_anchor_strength", 1.0)

        passes = []
        for module_name in pipeline_cfg.get("modules", []):
            # In future: module-specific rhythm/anchor
            anchor = AnchorWay(anchor_strength)
            cp = CadencePass(rhythm, anchor)
            passes.append(cp)

        return passes
