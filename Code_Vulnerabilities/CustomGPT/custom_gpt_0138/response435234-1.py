
# plugin1.py

from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # do something

# This block will execute when the plugin is imported
if __name__ == "__main__":
    manager.register_plugin(PLUGIN_NAME, plugin_function)
else:
    manager.register_plugin(PLUGIN_NAME, plugin_function)
