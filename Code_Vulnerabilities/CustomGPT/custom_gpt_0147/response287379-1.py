
import os
import sys

# Debug current working directory
print("Current Directory: ", os.getcwd())

# Append necessary paths
app_lib_path = os.path.join(os.getcwd(), 'appLib')
sys.path.append(app_lib_path)
print("PYTHONPATH: ", sys.path)  # Adding debug print to check paths 

# Trying to import SlotMap and other modules
try:
    from SlotMapper import SlotMap
except ImportError as e:
    print("Import error occurred: ", e)

from ShelfTypeSelection import ShelfTypeSelector
from PackTypeSelection import PackTypeSlotMappingSelector
from EntryWidgets import EntryBase, ShelfSlotEntry
