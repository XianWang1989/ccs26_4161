
import sys

# Ensure the path is included
if 'C:/Users/..../Documents/maya/2014-x64/scripts' not in sys.path:
    sys.path.append('C:/Users/..../Documents/maya/2014-x64/scripts')

# Import the module
import swap

# Reload if needed
reload(swap)

# Call the function
swap.printSomething()
