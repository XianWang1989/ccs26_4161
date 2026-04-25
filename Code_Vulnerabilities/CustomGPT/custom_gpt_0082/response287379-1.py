
import os
import sys

# Adding the necessary directories to sys.path
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(current_dir, 'appLib'))

# After modifying sys.path, ensure you're importing correctly
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")

# Example usage of SlotMap (assuming implementation exists in SlotMapper)
# slot_map_instance = SlotMap()  # Use this line if SlotMap is a class
