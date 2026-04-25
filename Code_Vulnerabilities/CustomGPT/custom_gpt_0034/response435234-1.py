
from application import manager

# List of all plugin modules to import
plugins = [
    "plugin1",
    "plugin2",
    "example_plugin",
    "plugin3.player"  # Include submodules if necessary
]

for plugin in plugins:
    __import__(f"plugins.{plugin}")
