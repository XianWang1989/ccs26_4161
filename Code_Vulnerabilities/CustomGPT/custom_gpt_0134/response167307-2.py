
import sys
import os

# Adding directories
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'external_lib'))

# Now import your modules
from some_module import SomeClass
