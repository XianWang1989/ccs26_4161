
import os
import sys

# Adjusting the sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)

# Debugging: print sys.path
print("Current sys.path:", sys.path)

# Importing from SlotMapper
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Import error: {e}")

# Importing other modules
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your main code or functions here
