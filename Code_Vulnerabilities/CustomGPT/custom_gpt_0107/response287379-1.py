
import os
import sys

# Define application library path
app_lib_path = os.path.join(os.getcwd(), 'appLib', 'KB-GUI')
sys.path.append(app_lib_path)

# Attempt to import
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print(f"Error importing SlotMap: {e}")
    # Optionally check contents of appLib
    print("Contents of appLib:", os.listdir(app_lib_path))

# Other imports
from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Your GUI code can go here...
