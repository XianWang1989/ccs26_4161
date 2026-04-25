
# my_script.py
import sys

# Adding multiple source directories
sys.path.append('/path/to/production_code')
sys.path.append('/path/to/testing_code')

# Now you can import your modules
from production_module import some_function
from testing_module import test_function

some_function()
test_function()
