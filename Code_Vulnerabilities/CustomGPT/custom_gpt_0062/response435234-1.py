
from .plugin1 import plugin_function as plugin1_function
from .plugin2 import plugin_function as plugin2_function
# Add more imports as needed

# Automatic registration
from application import manager

def register_plugins():
    manager.register_plugin("Plugin 1", plugin1_function)
    manager.register_plugin("Plugin 2", plugin2_function)
    # Continue registering other plugins
register_plugins()
