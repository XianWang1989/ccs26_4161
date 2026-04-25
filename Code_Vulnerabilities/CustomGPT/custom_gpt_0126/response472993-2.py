
# mypackage/__init__.py
import sys
import os

# Add the directory of the plugins to PYTHONPATH
plugins_path = os.path.dirname(__file__)
sys.path.append(plugins_path)

import plugin1
import plugin2
