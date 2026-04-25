
import sys
import os

# Add multiple directories to the sys.path
sys.path.append(os.path.abspath('path/to/your/source1'))
sys.path.append(os.path.abspath('path/to/your/source2'))
sys.path.append(os.path.abspath('path/to/test_code'))

# Now you can import modules from those directories
from my_module import MyClass
