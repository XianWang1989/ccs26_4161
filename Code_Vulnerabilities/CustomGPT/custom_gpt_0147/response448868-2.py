
# Assuming this is your swap.py located at "C:/Users/.../Documents/maya/2014-x64/scripts/"

def printSomething():
    print("Hello from swap!")

# Test the following in Maya's script editor
import swap
reload(swap)  # Make sure to use it if you modify the script
swap.printSomething()  # This should output: Hello from swap!
