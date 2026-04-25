
from .plugin1 import plugin_function as plugin1_function
from .example_plugin import plugin_function as example_plugin_function
# Import other plugins as needed

# Register plugins
from application import manager

manager.register_plugin("Plugin1", plugin1_function)
manager.register_plugin("ExamplePlugin", example_plugin_function)
