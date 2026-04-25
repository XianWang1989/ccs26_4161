
import os
import sys

# Add the directories to sys.path
sys.path.append(os.path.join(os.getcwd(), 'appLib', 'KB-GUI'))
sys.path.append(os.path.join(os.getcwd(), 'appLib'))

# Print sys.path for debugging
print(sys.path)

# Ensuring that SlotMap is defined in SlotMapper
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import Error: {e}")

# Proceed with other imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
