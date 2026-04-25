
def register_plugins(manager):
    # Automatically import all plugins to register themselves
    from .plugin1 import PLUGIN_NAME as plugin1_name, plugin_function as plugin1_function
    manager.register_plugin(plugin1_name, plugin1_function)

    from .example_plugin import PLUGIN_NAME as example_name, plugin_function as example_function
    manager.register_plugin(example_name, example_function)

    # Import additional plugins as needed
