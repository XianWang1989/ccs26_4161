
import os
import sys

# Set the path to your appLib and KB-GUI directories
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir, 'appLib', 'KB-GUI'))

# Ensure you import after modifying sys.path
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")
