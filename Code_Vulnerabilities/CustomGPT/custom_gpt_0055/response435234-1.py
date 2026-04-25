
import pkgutil
from . import manager  # Import the manager instance

# Automatically register all plugins found in this package
def register_plugins():
    package = __name__
    for _, module_name, _ in pkgutil.iter_modules([package]):
        __import__(f"{package}.{module_name}")

register_plugins()
