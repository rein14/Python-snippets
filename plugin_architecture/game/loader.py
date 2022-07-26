import importlib

class ModuleInterface:
    """Represents a plugin interface"""

    @staticmethod
    def register() -> None:
        """Register the necesssary items"""


def import_module(name:str) -> ModuleInterface:
    """Import a module from a string"""

    mod = importlib.import_module(name)
    return mod # type: ignore

def load_plugins(plugins: list[str]) -> None:
    for plugin_file in plugins:
        plugin = import_module(plugin_file)
        plugin.register()
