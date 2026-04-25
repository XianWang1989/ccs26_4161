
import os
import sys

# Add the appLib and KB-GUI directories to the path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Check the current PYTHONPATH
print("Current PYTHONPATH:", sys.path)

from SlotMapper import SlotMap  # This import should work now

# Example of using SlotMap (adjust as necessary)
def main():
    slot_map_instance = SlotMap()
    # Further logic here...

if __name__ == "__main__":
    main()
