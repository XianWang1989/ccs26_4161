
import os
import sys

# Adding appLib and KB-GUI to PYTHONPATH
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Print PYTHONPATH for debugging
print("Current PYTHONPATH:", sys.path)

try:
    # Attempting to import the necessary components
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry

    print("Imports successful!")

except ImportError as e:
    print(f"ImportError: {e}")
