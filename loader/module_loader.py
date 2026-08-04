import tomllib
from pathlib import Path

class GlyphgateConfig:
    def __init__(self, path: str = "glyphgate.toml"):
        self.path = Path(path)
        self.data = self._load()

    def _load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"Config file not found: {self.path}")

        with self.path.open("rb") as f:
            return tomllib.load(f)

    def get_modules(self):
        """Return the list of modules declared in glyphgate.toml."""
        return self.data.get("modules", [])

    def get_version(self):
        """Return the declared version from glyphgate.toml."""
        return self.data.get("version", "0.0.0")
