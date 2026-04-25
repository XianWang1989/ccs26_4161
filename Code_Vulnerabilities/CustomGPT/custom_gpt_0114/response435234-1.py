
from application import manager
import pkgutil

# Automatically import and register all plugins
for module_info in pkgutil.iter_modules(__path__):
    module_name = module_info.name
    if module_name != '__init__':
        __import__(f".{module_name}", locals(), globals())
