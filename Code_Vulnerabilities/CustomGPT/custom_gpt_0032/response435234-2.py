
def plugin_function(options):
    # Plugin functionality here
    pass

def register(manager):
    PLUGIN_NAME = "AAC_Player"
    manager.register_plugin(PLUGIN_NAME, plugin_function)
