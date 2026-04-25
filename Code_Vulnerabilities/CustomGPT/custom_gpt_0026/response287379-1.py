
import os
import sys

# Ensure the correct path is added
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Debug: Print the current sys.path
print("Current sys.path:", sys.path)

# Import statements
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print("ImportError occurred: ", e)

# Continue with your program logic
def main():
    # Example function using SlotMap
    slot_map_instance = SlotMap()
    # Your logic here...

if __name__ == "__main__":
    main()
