
import os
import sys

# Ensure the correct directories are in sys.path
app_lib_path = os.path.join(os.getcwd(), 'appLib')
gui_path = os.path.join(app_lib_path, 'KB-GUI')

sys.path.append(gui_path)
sys.path.append(app_lib_path)

# Check if SlotMap can be imported
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("Error importing SlotMap:", e)

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry

# Example usage of SlotMap (if it is imported successfully)
if 'SlotMap' in locals():
    print("SlotMap imported successfully!")
else:
    print("SlotMap not imported.")
