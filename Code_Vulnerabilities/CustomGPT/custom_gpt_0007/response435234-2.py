
from application import manager

PLUGIN_NAME = "AAC_Player"

def plugin_function(options):
    # Do something
    print(f'{PLUGIN_NAME} functionality executed with options: {options}')

manager.register_plugin(PLUGIN_NAME, plugin_function)
