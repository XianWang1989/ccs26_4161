
from application import manager

plugins = [
    "plugin1",
    "plugin2",
    "example_plugin",
    "plugin3.player"
]

for plugin in plugins:
    __import__(f"plugins.{plugin}")
