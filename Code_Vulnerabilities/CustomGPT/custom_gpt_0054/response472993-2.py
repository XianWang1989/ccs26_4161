
import sys
import os

# Add the directory containing your plugins to PYTHONPATH
plugin_path = os.path.dirname(__file__)  # Current directory where the package is located
sys.path.append(plugin_path)

# Now you can import your plugins
import plugin1
import plugin2
