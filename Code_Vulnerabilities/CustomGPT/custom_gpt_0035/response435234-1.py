
import os
import pkgutil
from application import manager

# Automatically import all plugin modules
def load_plugins():
    package = __name__
    for _, module_name, _ in pkgutil.walk_packages(__path__, package + "."):
        __import__(module_name)

load_plugins()
