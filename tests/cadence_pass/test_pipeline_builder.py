from loader.module_loader import GlyphgateConfig
from cadence_pass.pipeline_builder import PipelineBuilder
from cadence_pass.cadence_chain import CadenceChain
from cadence_pass.syncance import Syncance

def test_pipeline_builder_constructs_passes():
    cfg = GlyphgateConfig()
    builder = PipelineBuilder(cfg)
    passes = builder.build()

    chain = CadenceChain(passes)
    result = chain.run(Syncance(1.0))

    # With steady (len=6) and anchor=2.0:
    # each pass: (value * 6) / 2 = value * 3
    # pipeline modules = ["core", "ecology", "glyph_cadence_pass"]
    # 1.0 → 3.0 → 9.0 → 27.0
    assert result == 27.0
