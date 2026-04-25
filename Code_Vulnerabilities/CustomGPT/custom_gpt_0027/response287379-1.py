
import os
import sys

# Correctly set the path to the appLib
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))

# Try importing your modules
try:
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print(f"ImportError: {e}")
