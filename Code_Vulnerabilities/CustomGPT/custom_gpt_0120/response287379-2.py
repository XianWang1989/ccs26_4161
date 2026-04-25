
import os
import sys

# Set the paths
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

print("Current Python Path:", sys.path)

try:
    # Attempt the imports
    from SlotMapper import SlotMap
    from ShelfTypeSelection import ShelfTypeSelector
    from PackTypeSelection import PackTypeSlotMappingSelector
    from EntryWidgets import EntryBase, ShelfSlotEntry
except ImportError as e:
    print("ImportError:", e)
    print("Available modules in SlotMapper:", dir())
