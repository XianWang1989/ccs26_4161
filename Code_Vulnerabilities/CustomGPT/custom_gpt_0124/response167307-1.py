
import sys
import os

# Add custom paths to sys.path
sys.path.append('/path/to/your/module')
sys.path.append('/another/path/to/source')

# Optionally, prepend to give higher priority
sys.path.insert(0, '/path/to/priority/module')

# Now you can import your modules
try:
    import your_custom_module
except ImportError:
    print("Module not found! Check your PYTHONPATH settings.")
