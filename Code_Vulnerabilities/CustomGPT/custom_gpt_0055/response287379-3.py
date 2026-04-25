
import os
import sys

# Add directories to Python path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)
sys.path.append(os.path.join(app_lib_path, 'KB-GUI'))

# Print sys.path for debugging
print("Current sys.path:", sys.path)

# Attempt to import SlotMap after confirming paths
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"ImportError: {e}")

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
