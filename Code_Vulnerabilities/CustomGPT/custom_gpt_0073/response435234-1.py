
import os
import pkgutil
import importlib

# Automatically import all plugin modules
package_name = __name__

for _, module_name, _ in pkgutil.iter_modules([os.path.dirname(__file__)]):
    importlib.import_module(f'{package_name}.{module_name}')
