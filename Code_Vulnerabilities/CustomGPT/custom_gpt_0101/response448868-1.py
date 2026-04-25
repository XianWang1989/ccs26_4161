
import sys
# Check if the script path is correctly added
for pythonPath in sys.path:
    print(pythonPath)

# Example of importing your module
import swap
reload(swap)

# Call the function from your module
swap.printSomething()
