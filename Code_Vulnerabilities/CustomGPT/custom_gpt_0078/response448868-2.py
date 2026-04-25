
import sys
sys.path.append('C:/Users/.../Documents/maya/2014-x64/scripts')  # Ensure this path is appended

# Importing the package
import swapPackage.swap as swap  
reload(swap)  # Reloading to see changes if you modify the script
swap.printSomething()
