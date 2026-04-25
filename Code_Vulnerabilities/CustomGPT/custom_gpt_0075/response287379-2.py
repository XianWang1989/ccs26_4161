
import os
import sys

# Adding paths to system path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Attempt to import SlotMap with error handling
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("Failed to import SlotMap:", e)

# Importing other modules
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
