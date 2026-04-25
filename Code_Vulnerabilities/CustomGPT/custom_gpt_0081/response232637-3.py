
from package import *

name = input('Please Enter your question: ').lower()

# Check length of name input to determine which module to execute
if len(name) >= 3:
    MODULE1.run_module1(name)
elif len(name) >= 3:
    MODULE2.run_module2(name)
# Continue similarly for other modules if necessary
