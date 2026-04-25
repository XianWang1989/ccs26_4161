
from application import manager

# List all your plugin modules here
from . import example_plugin
from . import plugin1
from . import plugin2
from .plugin3.player  # Assuming player.py contains a plugin

# Register plugins
def register_plugins():
    # Call any specific registration logic here if needed.
    pass

# Automatically register plugins on import
register_plugins()
