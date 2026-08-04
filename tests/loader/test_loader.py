from loader.module_loader import GlyphgateConfig

def test_loader_reads_toml():
    cfg = GlyphgateConfig()
    modules = cfg.get_modules()
    assert isinstance(modules, dict)
    assert "core" in modules
